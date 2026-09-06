"""Test suite verifying all Phase 135 runner scripts conform to execution contracts."""

import importlib
import pytest

PHASE_135_SCRIPTS = [
    "scripts.run_regime_acceptance_profile_registry",
    "scripts.run_regime_block_inventory",
    "scripts.run_regime_block_acceptance_gates",
    "scripts.run_regime_block_compliance",
    "scripts.run_regime_block_component_acceptance",
    "scripts.run_regime_block_contracts",
    "scripts.run_phase_126_135_acceptance_manifest",
    "scripts.run_regime_acceptance_health_check",
    "scripts.run_regime_acceptance_validation_report",
    "scripts.run_regime_acceptance_status",
]


@pytest.mark.parametrize("script_module", PHASE_135_SCRIPTS)
def test_script_import_and_main_contract(script_module):
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main"), f"Module {script_module} missing main() function"
    assert callable(mod.main)
