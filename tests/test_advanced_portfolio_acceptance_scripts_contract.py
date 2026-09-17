# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Scripts Contract."""

import importlib
import pytest


SCRIPTS = [
    "scripts.run_portfolio_acceptance_profile_registry",
    "scripts.run_portfolio_acceptance_component_checkpoints",
    "scripts.run_portfolio_phase_acceptance",
    "scripts.run_portfolio_acceptance_dependencies_evidence",
    "scripts.run_portfolio_acceptance_boundaries_findings",
    "scripts.run_portfolio_acceptance_manifest",
    "scripts.run_portfolio_acceptance_health_check",
    "scripts.run_portfolio_acceptance_validation_report",
    "scripts.run_portfolio_acceptance_status",
]


@pytest.mark.parametrize("script_module", SCRIPTS)
def test_script_import_and_main_contract(script_module):
    """Verify that all Phase 157 scripts can be imported and expose a callable main."""
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main"), f"Script {script_module} does not define main()"
    assert callable(mod.main), f"main in {script_module} is not callable"
