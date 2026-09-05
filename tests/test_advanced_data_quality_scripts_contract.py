import pytest
import importlib

SCRIPTS = [
    "scripts.run_data_quality_profile_registry",
    "scripts.run_data_quality_rule_registry",
    "scripts.run_data_quality_provider_checks",
    "scripts.run_data_quality_asset_checks",
    "scripts.run_data_quality_news_checks",
    "scripts.run_data_quality_scoring",
    "scripts.run_data_quality_health_check",
    "scripts.run_data_quality_validation_report",
    "scripts.run_data_quality_status",
]


@pytest.mark.parametrize("script_mod", SCRIPTS)
def test_script_import_and_main(script_mod):
    mod = importlib.import_module(script_mod)
    assert hasattr(mod, "main"), f"{script_mod} missing main()"
    assert callable(mod.main)
