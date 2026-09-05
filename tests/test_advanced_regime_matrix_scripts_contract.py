import importlib
import pytest

SCRIPTS = [
    "scripts.run_regime_matrix_profile_registry",
    "scripts.run_regime_feature_matrix_contracts",
    "scripts.run_regime_state_dataset_contracts",
    "scripts.run_regime_matrix_input_registries",
    "scripts.run_regime_matrix_alignment_guards",
    "scripts.run_regime_matrix_integrity_manifest",
    "scripts.run_regime_matrix_health_check",
    "scripts.run_regime_matrix_validation_report",
    "scripts.run_regime_matrix_status",
]


@pytest.mark.parametrize("script_module", SCRIPTS)
def test_script_import_and_main_callable(script_module):
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main")
    assert callable(mod.main)
