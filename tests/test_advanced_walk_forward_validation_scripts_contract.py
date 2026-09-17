# -*- coding: utf-8 -*-
"""Test suite verifying all Phase 147 runner scripts conform to execution contracts."""

import importlib
import pytest

PHASE_147_SCRIPTS = [
    "scripts.run_walk_forward_profile_registry",
    "scripts.run_walk_forward_split_contracts",
    "scripts.run_oos_benchmark_contracts",
    "scripts.run_validation_metric_placeholders",
    "scripts.run_validation_bias_guards",
    "scripts.run_validation_disabled_execution_reports",
    "scripts.run_walk_forward_findings_manifest",
    "scripts.run_walk_forward_health_check",
    "scripts.run_walk_forward_validation_report",
    "scripts.run_walk_forward_status",
]


@pytest.mark.parametrize("script_module", PHASE_147_SCRIPTS)
def test_script_import_and_main_contract(script_module):
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main"), f"Module {script_module} missing main() function"
    assert callable(mod.main)
