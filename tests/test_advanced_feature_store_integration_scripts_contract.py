import importlib
import pytest

SCRIPTS = [
    "scripts.run_feature_store_integration_profile_registry",
    "scripts.run_feature_store_contracts",
    "scripts.run_feature_store_catalogs",
    "scripts.run_feature_store_metadata_manifest",
    "scripts.run_feature_store_quality_drift_catalog",
    "scripts.run_feature_store_validation_catalog",
    "scripts.run_feature_store_policy_registries",
    "scripts.run_feature_store_integration_health_check",
    "scripts.run_feature_store_integration_validation_report",
    "scripts.run_feature_store_integration_status",
]

@pytest.mark.parametrize("script_module", SCRIPTS)
def test_script_import_and_main_callable(script_module):
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main")
    assert callable(mod.main)
