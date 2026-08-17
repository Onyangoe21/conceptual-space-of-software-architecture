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

"""Tests for the propagation cost estimator.

The cases that matter are the hand computable ones, where the closure density
can be checked against arithmetic done on paper, and the resolution cases,
where an import either becomes an intra-repository edge or correctly does not.

    python3 test_propagation_cost.py

No network, no third party dependencies.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import propagation_cost as pc


def build(files: dict[str, str], root: Path) -> None:
    for name, body in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")


def measure(files: dict[str, str], **kwargs) -> pc.Result:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        build(files, root)
        discovered = pc.discover_python_files(root, **kwargs)
        return pc.compute(pc.build_graph(root, discovered))


def approx(a: float, b: float, tol: float = 1e-9) -> bool:
    return abs(a - b) < tol


CASES: list[tuple[str, bool]] = []


def check(label: str, condition: bool) -> None:
    CASES.append((label, condition))


def test_hand_computable_shapes() -> None:
    # A chain a -> b -> c. Reachability including self: a sees 3, b sees 2,
    # c sees 1. Total 6 over 3 squared.
    chain = measure(
        {
            "a.py": "import b\n",
            "b.py": "import c\n",
            "c.py": "x = 1\n",
        }
    )
    check("chain of three has propagation cost 6/9", approx(chain.propagation_cost, 6 / 9))
    check("chain of three has three nodes", chain.node_count == 3)
    check("chain of three has two edges", chain.edge_count == 2)

    # A two cycle. Every member reaches every member, so the closure is full.
    cycle = measure({"a.py": "import b\n", "b.py": "import a\n"})
    check("a cycle saturates the closure", approx(cycle.propagation_cost, 1.0))

    # No edges at all. Only the diagonal is set.
    isolated = measure({"a.py": "x = 1\n", "b.py": "y = 2\n"})
    check("two isolated files give 2/4", approx(isolated.propagation_cost, 0.5))

    single = measure({"a.py": "x = 1\n"})
    check("a single file sees only itself, 1/1", approx(single.propagation_cost, 1.0))

    empty = measure({})
    check("an empty repository is zero rather than a division error", empty.propagation_cost == 0.0)

    # A diamond: a -> b, a -> c, b -> d, c -> d. a sees 4, b sees 2, c sees 2,
    # d sees 1. Total 9 over 16.
    diamond = measure(
        {
            "a.py": "import b\nimport c\n",
            "b.py": "import d\n",
            "c.py": "import d\n",
            "d.py": "x = 1\n",
        }
    )
    check("diamond gives 9/16", approx(diamond.propagation_cost, 9 / 16))


def test_edges_are_intra_repository_only() -> None:
    external = measure({"a.py": "import os\nimport json\nimport numpy\n"})
    check("standard library and third party imports are not edges", external.edge_count == 0)
    check("a file importing only externals still sees itself", approx(external.propagation_cost, 1.0))

    shadow = measure({"a.py": "import json\n", "json.py": "x = 1\n"})
    check("an in-repo module shadowing a stdlib name does become an edge", shadow.edge_count == 1)


def test_import_forms_resolve() -> None:
    from_import = measure(
        {
            "pkg/__init__.py": "",
            "pkg/mod.py": "value = 1\n",
            "app.py": "from pkg.mod import value\n",
        }
    )
    check("from pkg.mod import name resolves to pkg/mod.py", from_import.edge_count >= 1)

    relative = measure(
        {
            "pkg/__init__.py": "",
            "pkg/one.py": "from . import two\n",
            "pkg/two.py": "x = 1\n",
        }
    )
    check("a relative import inside a package is an edge", relative.edge_count >= 1)

    parent_relative = measure(
        {
            "pkg/__init__.py": "",
            "pkg/sub/__init__.py": "",
            "pkg/sub/deep.py": "from ..top import thing\n",
            "pkg/top.py": "thing = 1\n",
        }
    )
    check("a parent relative import resolves upward", parent_relative.edge_count >= 1)

    escaped = measure({"a.py": "from ....way.up import thing\n"})
    check("a relative import above the root is counted unresolved", escaped.unresolved_imports >= 1)

    aliased = measure({"a.py": "import b as bee\n", "b.py": "x = 1\n"})
    check("an aliased import is still an edge", aliased.edge_count == 1)


def test_self_import_is_not_an_edge() -> None:
    result = measure({"a.py": "import a\n"})
    check("a file importing itself adds no edge", result.edge_count == 0)
    check("a self import leaves the diagonal only", approx(result.propagation_cost, 1.0))


def test_unparseable_file_is_still_a_node() -> None:
    broken = measure({"a.py": "def (((\n", "b.py": "x = 1\n"})
    check("a file that does not parse remains a node", broken.node_count == 2)
    check("a file that does not parse is counted unresolved", broken.unresolved_imports >= 1)


def test_module_name_candidates() -> None:
    names = pc.module_names_for(Path("src/pkg/mod.py"))
    check("every import root suffix is registered", set(names) == {"src.pkg.mod", "pkg.mod", "mod"})

    package = pc.module_names_for(Path("src/pkg/__init__.py"))
    check("an __init__ answers to its package name", set(package) == {"src.pkg", "pkg"})


def test_test_exclusion() -> None:
    files = {
        "a.py": "x = 1\n",
        "test_a.py": "import a\n",
        "tests/test_b.py": "import a\n",
    }
    with_tests = measure(files)
    without_tests = measure(files, include_tests=False)
    check("tests are included by default", with_tests.node_count == 3)
    check("--no-tests drops test files", without_tests.node_count == 1)


def test_excluded_directories() -> None:
    result = measure(
        {
            "a.py": "x = 1\n",
            "node_modules/pkg/b.py": "y = 2\n",
            "__pycache__/c.py": "z = 3\n",
        }
    )
    check("vendored and generated trees are skipped", result.node_count == 1)


def test_report_carries_the_metadata_block() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        build({"a.py": "import b\n", "b.py": "x = 1\n"}, root)
        files = pc.discover_python_files(root)
        result = pc.compute(pc.build_graph(root, files))
        report = pc.build_report(root, result, {"language": "python"})

    payload = json.loads(json.dumps(report))
    meta = payload["metadata"]
    required = {
        "estimator",
        "version",
        "repository",
        "repository_url",
        "commit",
        "run_at",
        "parameters",
    }
    check("the metadata block has every required field", required <= set(meta))
    check(
        "no absolute local path leaks into the report",
        "repository_path" not in meta and str(root) not in json.dumps(payload),
    )
    check("the estimator names itself", meta["estimator"] == pc.ESTIMATOR_NAME)
    check("the report carries estimates", "propagation_cost" in payload["estimates"])
    check("the report carries graph size", payload["graph"]["node_count"] == 2)


def test_per_file_rows() -> None:
    result = measure({"a.py": "import b\n", "b.py": "x = 1\n"})
    rows = pc.per_file_rows(result)
    check("csv has a header and one row per file", len(rows) == 3)
    check("csv header names the columns", rows[0] == "file,visibility,visibility_fraction")


def main() -> int:
    groups = [
        ("Hand computable shapes", test_hand_computable_shapes),
        ("Edge scope", test_edges_are_intra_repository_only),
        ("Import forms", test_import_forms_resolve),
        ("Self imports", test_self_import_is_not_an_edge),
        ("Unparseable files", test_unparseable_file_is_still_a_node),
        ("Module name candidates", test_module_name_candidates),
        ("Test exclusion", test_test_exclusion),
        ("Directory exclusion", test_excluded_directories),
        ("Report shape", test_report_carries_the_metadata_block),
        ("Per file output", test_per_file_rows),
    ]

    failures = 0
    for title, fn in groups:
        start = len(CASES)
        fn()
        print(f"\n{title}:")
        for label, ok in CASES[start:]:
            print(f"  {'pass' if ok else 'FAIL'}  {label}")
            if not ok:
                failures += 1

    print()
    if failures:
        print(f"{failures} of {len(CASES)} checks failed.")
        return 1
    print(f"All {len(CASES)} checks hold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
