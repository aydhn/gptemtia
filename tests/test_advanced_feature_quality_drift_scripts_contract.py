"""Phase 123 scripts contract and backward compatibility test."""

import importlib
import pytest


def test_scripts_importable():
    script_modules = [
        "scripts.run_feature_quality_drift_profile_registry",
        "scripts.run_feature_quality_metric_registry",
        "scripts.run_feature_quality_diagnostics",
        "scripts.run_feature_drift_diagnostics",
        "scripts.run_factor_quality_drift_reports",
        "scripts.run_macro_cross_asset_quality_reports",
        "scripts.run_feature_quality_drift_findings",
        "scripts.run_feature_quality_drift_health_check",
        "scripts.run_feature_quality_drift_validation_report",
        "scripts.run_feature_quality_drift_status",
    ]
    for mod_name in script_modules:
        mod = importlib.import_module(mod_name)
        assert hasattr(mod, "main"), f"Module {mod_name} missing main function"


def test_previous_phase_modules_intact():
    # Verify Phase 116-122 packages remain intact and importable
    prev_modules = [
        "advanced_feature_engine",
        "advanced_technical_indicators",
        "advanced_feature_grid",
        "advanced_cross_asset_alignment",
        "advanced_feature_fusion",
        "advanced_feature_validation",
        "advanced_factor_metadata",
        "advanced_feature_quality_drift",
    ]
    for pmod in prev_modules:
        mod = importlib.import_module(pmod)
        assert mod is not None
