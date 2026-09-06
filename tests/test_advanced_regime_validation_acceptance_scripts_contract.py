"""Tests contract and importability for Phase 133 operational scripts."""

import importlib


def test_scripts_contract():
    script_names = [
        "scripts.run_regime_validation_acceptance_profile_registry",
        "scripts.run_regime_validation_gates",
        "scripts.run_regime_no_lookahead_acceptance",
        "scripts.run_regime_metadata_only_acceptance",
        "scripts.run_regime_component_acceptance_reports",
        "scripts.run_regime_validation_findings",
        "scripts.run_regime_validation_acceptance_manifest",
        "scripts.run_regime_validation_acceptance_health_check",
        "scripts.run_regime_validation_acceptance_validation_report",
        "scripts.run_regime_validation_acceptance_status",
    ]

    for s_name in script_names:
        mod = importlib.import_module(s_name)
        assert hasattr(mod, "main"), f"Script {s_name} lacks a main function!"
        assert callable(mod.main)
