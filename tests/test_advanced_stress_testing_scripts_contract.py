# -*- coding: utf-8 -*-
"""Test suite verifying all Phase 148 runner scripts conform to execution contracts."""

import importlib
import pytest

PHASE_148_SCRIPTS = [
    "scripts.run_stress_testing_profile_registry",
    "scripts.run_stress_scenario_contracts",
    "scripts.run_stress_shock_placeholders",
    "scripts.run_stress_metric_placeholders",
    "scripts.run_stress_dependencies_guards",
    "scripts.run_stress_disabled_execution_reports",
    "scripts.run_stress_findings_manifest",
    "scripts.run_stress_testing_health_check",
    "scripts.run_stress_testing_validation_report",
    "scripts.run_stress_testing_status",
]


@pytest.mark.parametrize("script_module", PHASE_148_SCRIPTS)
def test_script_import_and_main_contract(script_module):
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main"), f"Module {script_module} missing main() function"
    assert callable(mod.main)
