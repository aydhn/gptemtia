import importlib
import pytest

SCRIPTS = [
    "scripts.run_regime_rule_free_profile_registry",
    "scripts.run_rule_free_labeling_contracts",
    "scripts.run_candidate_state_schemas",
    "scripts.run_unsupervised_prep_contracts",
    "scripts.run_candidate_state_input_registries",
    "scripts.run_candidate_state_integrity_manifest",
    "scripts.run_regime_rule_free_health_check",
    "scripts.run_regime_rule_free_validation_report",
    "scripts.run_regime_rule_free_status",
]


@pytest.mark.parametrize("script_module", SCRIPTS)
def test_script_import_and_main_callable(script_module):
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main")
    assert callable(mod.main)
