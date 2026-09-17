# -*- coding: utf-8 -*-
"""Test suite verifying all Phase 146 runner scripts conform to execution contracts."""

import importlib
import pytest

PHASE_146_SCRIPTS = [
    "scripts.run_realistic_backtest_profile_registry",
    "scripts.run_backtest_engine_contracts",
    "scripts.run_backtest_execution_cost_models",
    "scripts.run_backtest_accounting_lifecycle",
    "scripts.run_backtest_bias_guards",
    "scripts.run_backtest_disabled_execution_reports",
    "scripts.run_backtest_findings_manifest",
    "scripts.run_realistic_backtest_health_check",
    "scripts.run_realistic_backtest_validation_report",
    "scripts.run_realistic_backtest_status",
]


@pytest.mark.parametrize("script_module", PHASE_146_SCRIPTS)
def test_script_import_and_main_contract(script_module):
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main"), f"Module {script_module} missing main() function"
    assert callable(mod.main)
