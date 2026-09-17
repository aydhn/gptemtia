# -*- coding: utf-8 -*-
"""Tests for Phase 158: Full System Integration Scripts Contract."""

import importlib
import pytest


SCRIPTS = [
    "scripts.run_full_system_integration_profile_registry",
    "scripts.run_system_component_registry",
    "scripts.run_system_contract_integration",
    "scripts.run_advanced_acceptance_rehearsal",
    "scripts.run_system_boundaries",
    "scripts.run_system_disabled_execution_reports",
    "scripts.run_system_integration_findings_manifest",
    "scripts.run_full_system_integration_health_check",
    "scripts.run_full_system_integration_validation_report",
    "scripts.run_full_system_integration_status",
]


@pytest.mark.parametrize("script_module", SCRIPTS)
def test_script_import_and_main_contract(script_module):
    """Verify that all Phase 158 scripts can be imported and expose a callable main."""
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main"), f"Script {script_module} does not define main()"
    assert callable(mod.main), f"main in {script_module} is not callable"
