import pytest
import importlib

SCRIPTS = [
    "scripts.run_regime_featurestore_profile_registry",
    "scripts.run_regime_featurestore_contracts",
    "scripts.run_regime_featurestore_schema_catalogs",
    "scripts.run_regime_component_store_catalogs",
    "scripts.run_regime_accepted_reference_registries",
    "scripts.run_regime_featurestore_policies_manifest",
    "scripts.run_regime_featurestore_health_check",
    "scripts.run_regime_featurestore_validation_report",
    "scripts.run_regime_featurestore_status",
]


@pytest.mark.parametrize("module_name", SCRIPTS)
def test_script_contract_has_main(module_name):
    mod = importlib.import_module(module_name)
    assert hasattr(mod, "main"), f"Module {module_name} must have a main() function"
    assert callable(mod.main), f"main in {module_name} must be callable"
