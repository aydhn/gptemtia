# -*- coding: utf-8 -*-
"""Phase 150: Dedicated Unit Test Runner.

Discovers and executes all Phase 150 test files that test advanced_backtest_governance.
"""

import os
import sys
import glob
import pytest


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tests_dir = os.path.join(repo_root, "tests")

    phase_150_tests = []
    for test_file in glob.glob(os.path.join(tests_dir, "test_*.py")):
        try:
            with open(test_file, "r", encoding="utf-8") as f:
                content = f.read()
                if "advanced_backtest_governance" in content or "Phase 150" in content:
                    phase_150_tests.append(test_file)
        except Exception:
            pass

    phase_150_tests.sort()
    print(f"Found {len(phase_150_tests)} Phase 150 test files.")
    for t in phase_150_tests:
        print(f"  - {os.path.basename(t)}")

    args = ["-v", "-s", "--no-header", "--tb=short"] + phase_150_tests
    ret = pytest.main(args)
    sys.exit(ret)


if __name__ == "__main__":
    main()
