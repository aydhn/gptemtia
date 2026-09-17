# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: CLI Scripts Execution Contract.

Verifies that all 11 Phase 151 scripts execute successfully, exit with code 0,
produce non-empty stdout, and preserve negative invariants.
"""

import sys
import subprocess
import pytest

SCRIPTS = [
    "scripts.run_benchmark_evaluation_profile_registry",
    "scripts.run_benchmark_report_contracts",
    "scripts.run_strategy_evaluation_report_contracts",
    "scripts.run_evaluation_summary_placeholders",
    "scripts.run_evaluation_metric_placeholders",
    "scripts.run_evaluation_dependencies_guards",
    "scripts.run_evaluation_disabled_execution_reports",
    "scripts.run_benchmark_evaluation_findings_manifest",
    "scripts.run_benchmark_evaluation_health_check",
    "scripts.run_benchmark_evaluation_validation_report",
    "scripts.run_benchmark_evaluation_status",
]


@pytest.mark.parametrize("script_module", SCRIPTS)
def test_script_execution_contract(script_module: str):
    res = subprocess.run(
        [sys.executable, "-m", script_module],
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0, f"Script {script_module} failed with error:\n{res.stderr}"
    assert len(res.stdout.strip()) > 0, f"Script {script_module} produced empty stdout"
    assert "guaranteed return" not in res.stdout.lower()
    assert "live trading ready" not in res.stdout.lower()
