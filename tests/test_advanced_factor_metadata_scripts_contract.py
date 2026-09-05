import importlib
import pytest


def test_scripts_importable():
    script_modules = [
        "scripts.run_factor_metadata_profile_registry",
        "scripts.run_factor_family_registry",
        "scripts.run_factor_contracts",
        "scripts.run_factor_dependency_registry",
        "scripts.run_technical_factor_families",
        "scripts.run_macro_event_news_factor_families",
        "scripts.run_factor_metadata_manifest",
        "scripts.run_factor_metadata_health_check",
        "scripts.run_factor_metadata_validation_report",
        "scripts.run_factor_metadata_status",
    ]
    for mod_name in script_modules:
        mod = importlib.import_module(mod_name)
        assert hasattr(mod, "main"), f"Module {mod_name} missing main function"


def test_previous_phase_modules_intact():
    # Verify Phase 116-121 packages remain intact and importable
    prev_modules = [
        "advanced_feature_engine",
        "advanced_technical_indicators",
        "advanced_feature_grid",
        "advanced_cross_asset_alignment",
        "advanced_feature_fusion",
        "advanced_feature_validation",
    ]
    for pmod in prev_modules:
        mod = importlib.import_module(pmod)
        assert mod is not None
