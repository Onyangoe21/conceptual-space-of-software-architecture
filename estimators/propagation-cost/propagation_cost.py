#!/usr/bin/env python3
#
# Copyright 2026 Edwin O Onyango
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Propagation cost over a Python repository's intra-project import graph.

Propagation cost is the density of the transitive closure of the dependency
matrix: the expected fraction of the system reachable from a randomly chosen
element. MacCormack, Rusnak and Baldwin (2006) derive it from a change cost
argument. Lakos (1996) derives the same quantity from a build cost argument and
calls it average cumulative component dependency. The paper treats that
agreement as its flagship convergence, and this estimator is the computable
half of that claim.

    python3 propagation_cost.py /path/to/repo
    python3 propagation_cost.py /path/to/repo --out result.json --per-file rows.csv

Standard library only. No network access at any point.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, NamedTuple

ESTIMATOR_NAME = "propagation-cost"
ESTIMATOR_VERSION = "1.0.0"

DEFAULT_EXCLUDES = (
    ".git",
    ".hg",
    ".svn",
    ".tox",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    "node_modules",
    "build",
    "dist",
    ".mypy_cache",
    ".pytest_cache",
)


class Graph(NamedTuple):
    """A dependency graph over source files, with stable node ordering."""

    nodes: list[str]
    edges: set[tuple[int, int]]
    unresolved: int


class Result(NamedTuple):
    propagation_cost: float
    direct_density: float
    node_count: int
    edge_count: int
    unresolved_imports: int
    visibility: list[int]
    nodes: list[str]


def discover_python_files(
    root: Path, excludes: Iterable[str] = DEFAULT_EXCLUDES, include_tests: bool = True
) -> list[Path]:
    """Return every .py file under root, excluding vendored and generated trees."""
    exclude_set = set(excludes)
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in exclude_set)
        for filename in sorted(filenames):
            if not filename.endswith(".py"):
                continue
            path = Path(dirpath) / filename
            rel = path.relative_to(root)
            if not include_tests and _looks_like_test(rel):
                continue
            found.append(path)
    return found


def _looks_like_test(rel: Path) -> bool:
    name = rel.name
    if name.startswith("test_") or name.endswith("_test.py"):
        return True
    return any(part in ("tests", "test") for part in rel.parts[:-1])


def module_names_for(rel: Path) -> list[str]:
    """Every dotted module name by which an in-repo file can be imported.

    A file may be addressable under more than one name because the import root
    is not knowable from the source tree alone. src/pkg/mod.py can be imported
    as pkg.mod when src/ is on the path, and as src.pkg.mod when the repository
    root is. Registering every suffix keeps resolution independent of a build
    configuration this estimator cannot see.
    """
    parts = list(rel.parts)
    if parts[-1] == "__init__.py":
        parts = parts[:-1]
    else:
        parts[-1] = parts[-1][: -len(".py")]
    if not parts:
        return []
    return [".".join(parts[i:]) for i in range(len(parts))]


def _imported_names(tree: ast.AST, rel: Path) -> tuple[set[str], int]:
    """Collect candidate module names imported by one file.

    Returns the candidate dotted names and a count of relative imports that
    climbed above the repository root, which are counted as unresolved rather
    than silently dropped.
    """
    names: set[str] = set()
    escaped = 0
    package_parts = list(rel.parts[:-1])

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                names.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0:
                if node.module:
                    names.add(node.module)
                    for alias in node.names:
                        names.add(f"{node.module}.{alias.name}")
                continue

            # A relative import resolves against the importing file's package.
            # level 1 is the current package, level 2 the parent, and so on.
            climb = node.level - 1
            if climb > len(package_parts):
                escaped += 1
                continue
            base_parts = package_parts[: len(package_parts) - climb] if climb else package_parts
            base = ".".join(base_parts)
            if node.module:
                base = f"{base}.{node.module}" if base else node.module
            if base:
                names.add(base)
            for alias in node.names:
                names.add(f"{base}.{alias.name}" if base else alias.name)

    return names, escaped


def build_graph(root: Path, files: list[Path]) -> Graph:
    """Parse every file and resolve imports to other files in the same repository.

    Only intra-repository edges are recorded. An import of a third party or
    standard library module is not an edge, because propagation cost measures
    how much of *this* system a change reaches.
    """
    rel_paths = [f.relative_to(root) for f in files]
    nodes = [p.as_posix() for p in rel_paths]
    index = {name: i for i, name in enumerate(nodes)}

    # Map every dotted name a file answers to back to that file. Shorter names
    # are more specific to a plausible import root, so a longer registration
    # never displaces a shorter one.
    module_to_node: dict[str, int] = {}
    for i, rel in enumerate(rel_paths):
        for candidate in module_names_for(rel):
            module_to_node.setdefault(candidate, i)

    edges: set[tuple[int, int]] = set()
    unresolved = 0

    for i, path in enumerate(files):
        rel = rel_paths[i]
        try:
            source = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(source, filename=str(path))
        except (SyntaxError, ValueError, OSError):
            # A file that does not parse contributes no edges. It stays a node,
            # because it is still part of the system being measured.
            unresolved += 1
            continue

        names, escaped = _imported_names(tree, rel)
        unresolved += escaped

        for name in names:
            target = module_to_node.get(name)
            if target is None:
                # Walk up the dotted path: from pkg.mod import thing should
                # resolve to pkg/mod.py even though pkg.mod.thing is not a file.
                parts = name.split(".")
                while len(parts) > 1 and target is None:
                    parts.pop()
                    target = module_to_node.get(".".join(parts))
            if target is not None and target != i:
                edges.add((i, target))

    del index
    return Graph(nodes=nodes, edges=edges, unresolved=unresolved)


def compute(graph: Graph) -> Result:
    """Transitive closure by bitset, then density.

    The visibility matrix is the sum of all powers of the adjacency matrix
    starting at the zeroth, so every element is visible to itself and the
    diagonal is set. Cycles need no special handling: every member of a cycle
    reaches every other member, which is the same answer Lakos's build cost
    reading gives, since a cycle must be compiled as a unit.
    """
    n = len(graph.nodes)
    if n == 0:
        return Result(0.0, 0.0, 0, 0, graph.unresolved, [], [])

    successors: list[list[int]] = [[] for _ in range(n)]
    for src, dst in graph.edges:
        successors[src].append(dst)

    reach: list[int] = []
    for start in range(n):
        seen = 1 << start
        stack = [start]
        while stack:
            current = stack.pop()
            for nxt in successors[current]:
                bit = 1 << nxt
                if not seen & bit:
                    seen |= bit
                    stack.append(nxt)
        reach.append(seen)

    visibility = [bits.bit_count() for bits in reach]
    total_visible = sum(visibility)

    return Result(
        propagation_cost=total_visible / (n * n),
        direct_density=len(graph.edges) / (n * n),
        node_count=n,
        edge_count=len(graph.edges),
        unresolved_imports=graph.unresolved,
        visibility=visibility,
        nodes=graph.nodes,
    )


def _git(root: Path, *args: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", "-C", str(root), *args],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    return out.stdout.strip() or None


def git_commit(root: Path) -> str | None:
    return _git(root, "rev-parse", "HEAD")


def git_remote(root: Path) -> str | None:
    """The origin URL, which identifies the measured repository globally.

    An absolute filesystem path would identify it only on the machine that ran
    the estimator, and would churn the diff of any checked in result.
    """
    return _git(root, "config", "--get", "remote.origin.url")


def build_report(root: Path, result: Result, parameters: dict[str, object]) -> dict[str, object]:
    return {
        "metadata": {
            "estimator": ESTIMATOR_NAME,
            "version": ESTIMATOR_VERSION,
            "repository": root.resolve().name,
            "repository_url": git_remote(root),
            "commit": git_commit(root),
            "run_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "parameters": parameters,
        },
        "estimates": {
            "propagation_cost": round(result.propagation_cost, 6),
            "direct_density": round(result.direct_density, 6),
        },
        "graph": {
            "node_count": result.node_count,
            "edge_count": result.edge_count,
            "unresolved_imports": result.unresolved_imports,
        },
    }


def per_file_rows(result: Result) -> list[str]:
    rows = ["file,visibility,visibility_fraction"]
    n = result.node_count
    for name, visible in zip(result.nodes, result.visibility):
        rows.append(f"{name},{visible},{visible / n:.6f}" if n else f"{name},{visible},0")
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("repository", type=Path, help="path to a repository checkout")
    parser.add_argument("--out", type=Path, help="write the JSON report here instead of stdout")
    parser.add_argument("--per-file", type=Path, help="also write per file visibility as CSV")
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="directory name to skip, repeatable, added to the defaults",
    )
    parser.add_argument(
        "--no-tests",
        action="store_true",
        help="skip test files, which inflate visibility without being depended upon",
    )
    args = parser.parse_args(argv)

    root: Path = args.repository
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    excludes = tuple(DEFAULT_EXCLUDES) + tuple(args.exclude)
    files = discover_python_files(root, excludes, include_tests=not args.no_tests)
    graph = build_graph(root, files)
    result = compute(graph)

    parameters = {
        "excludes": sorted(set(excludes)),
        "include_tests": not args.no_tests,
        "language": "python",
        "granularity": "file",
    }
    report = build_report(root, result, parameters)
    rendered = json.dumps(report, indent=2, sort_keys=False)

    if args.out:
        args.out.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)

    if args.per_file:
        args.per_file.write_text("\n".join(per_file_rows(result)) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
