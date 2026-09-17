# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: CLI Scripts Execution Contract.

Verifies that all 11 Phase 149 scripts execute successfully, exit with code 0,
produce non-empty stdout, and preserve negative invariants.
"""

import sys
import subprocess
import pytest

SCRIPTS = [
    "scripts.run_monte_carlo_profile_registry",
    "scripts.run_monte_carlo_contracts",
    "scripts.run_monte_carlo_resampling_placeholders",
    "scripts.run_parameter_stability_contracts",
    "scripts.run_monte_carlo_metric_placeholders",
    "scripts.run_monte_carlo_dependencies_guards",
    "scripts.run_monte_carlo_disabled_execution_reports",
    "scripts.run_monte_carlo_findings_manifest",
    "scripts.run_monte_carlo_health_check",
    "scripts.run_monte_carlo_validation_report",
    "scripts.run_monte_carlo_status",
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
