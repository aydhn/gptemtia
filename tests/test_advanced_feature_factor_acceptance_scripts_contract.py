import importlib
import pytest

SCRIPTS = [
    "scripts.run_feature_factor_acceptance_profile_registry",
    "scripts.run_feature_engine_block_inventory",
    "scripts.run_feature_engine_block_acceptance_gates",
    "scripts.run_feature_engine_block_compliance",
    "scripts.run_feature_engine_block_contracts",
    "scripts.run_phase_116_125_acceptance_manifest",
    "scripts.run_feature_factor_acceptance_health_check",
    "scripts.run_feature_factor_acceptance_validation_report",
    "scripts.run_feature_factor_acceptance_status",
]

@pytest.mark.parametrize("script_module", SCRIPTS)
def test_script_import_and_main_callable(script_module):
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main")
    assert callable(mod.main)
