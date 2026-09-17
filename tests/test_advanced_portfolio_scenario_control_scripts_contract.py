# -*- coding: utf-8 -*-
import subprocess
import sys
import pytest

SCRIPTS = [
    "run_portfolio_scenario_control_profile_registry.py",
    "run_portfolio_scenario_testing_contracts.py",
    "run_drawdown_control_contracts.py",
    "run_portfolio_control_placeholders.py",
    "run_scenario_control_outputs_metrics.py",
    "run_scenario_control_dependencies_guards.py",
    "run_scenario_control_disabled_execution_reports.py",
    "run_portfolio_scenario_findings_manifest.py",
    "run_portfolio_scenario_control_health_check.py",
    "run_portfolio_scenario_control_validation_report.py",
    "run_portfolio_scenario_control_status.py",
]

@pytest.mark.parametrize("script_name", SCRIPTS)
def test_script_execution_contract(script_name):
    res = subprocess.run([sys.executable, f"scripts/{script_name}"], capture_output=True, text=True)
    assert res.returncode == 0, f"Script {script_name} failed with: {res.stderr}"
    assert "PHASE 156" in res.stdout
