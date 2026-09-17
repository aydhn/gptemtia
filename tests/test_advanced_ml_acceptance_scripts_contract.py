# -*- coding: utf-8 -*-
"""Test suite verifying all Phase 145 runner scripts conform to execution contracts."""

import importlib
import pytest

PHASE_145_SCRIPTS = [
    "scripts.run_advanced_ml_acceptance_profile_registry",
    "scripts.run_advanced_ml_component_acceptance",
    "scripts.run_advanced_ml_phase_acceptance",
    "scripts.run_advanced_ml_dependency_evidence",
    "scripts.run_advanced_ml_boundaries_findings",
    "scripts.run_advanced_ml_acceptance_manifest",
    "scripts.run_advanced_ml_acceptance_health_check",
    "scripts.run_advanced_ml_acceptance_validation_report",
    "scripts.run_advanced_ml_acceptance_status",
]


@pytest.mark.parametrize("script_module", PHASE_145_SCRIPTS)
def test_script_import_and_main_contract(script_module):
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main"), f"Module {script_module} missing main() function"
    assert callable(mod.main)
