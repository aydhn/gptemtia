import importlib
import pytest

SCRIPTS = [
    "scripts.run_regime_foundation_profile_registry",
    "scripts.run_market_behavior_taxonomy",
    "scripts.run_regime_family_registry",
    "scripts.run_regime_context_registries",
    "scripts.run_regime_contracts_dependencies",
    "scripts.run_regime_foundation_manifest",
    "scripts.run_regime_foundation_health_check",
    "scripts.run_regime_foundation_validation_report",
    "scripts.run_regime_foundation_status",
]


@pytest.mark.parametrize("script_module", SCRIPTS)
def test_script_import_and_main_callable(script_module):
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main")
    assert callable(mod.main)
