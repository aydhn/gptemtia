import pandas as pd
from advanced_regime_foundation.regime_foundation_report_builder import (
    build_regime_foundation_profile_markdown_report,
    build_market_behavior_taxonomy_markdown_report,
    build_regime_state_taxonomy_markdown_report,
    build_regime_family_markdown_report,
    build_regime_context_markdown_report,
    build_regime_contract_dependency_markdown_report,
    build_regime_manifest_markdown_report,
    build_regime_health_markdown_report,
    build_regime_validation_markdown_report,
    build_regime_safety_markdown_report,
    build_phase_127_handoff_markdown_report,
    build_regime_foundation_disclaimer,
)


def test_regime_foundation_report_builder():
    disclaimer = build_regime_foundation_disclaimer()
    assert "Phase 126" in disclaimer
    assert "Canlı emir" in disclaimer
    assert "kesin AL/SAT" in disclaimer

    sample_summary = {
        "active_profile": "balanced_local_regime_foundation",
        "current_phase": 126,
        "next_phase": 127,
        "target_final_phase": 160,
        "total_profiles": 3,
        "total_behaviors": 12,
        "total_states": 11,
        "total_families": 9,
        "foundation_name": "advanced_regime_foundation",
        "health_status": "HEALTHY",
        "validation_status": "VALIDATION_PASS",
        "safety_status": "SECURE",
        "handoff_status": "READY",
        "all_non_signal": True,
        "all_local_only": True,
        "all_model_training_disabled": True,
        "all_clustering_disabled": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }

    dummy_df = pd.DataFrame([{"col1": "val1", "col2": "val2"}])

    md_prof = build_regime_foundation_profile_markdown_report(sample_summary, dummy_df)
    assert "# Phase 126: Regime Foundation Profile Registry Report" in md_prof
    assert disclaimer in md_prof

    md_beh = build_market_behavior_taxonomy_markdown_report(sample_summary, dummy_df)
    assert "# Phase 126: Market Behavior Taxonomy Report" in md_beh

    md_state = build_regime_state_taxonomy_markdown_report(sample_summary, dummy_df)
    assert "# Phase 126: Regime State Taxonomy Report" in md_state

    md_fam = build_regime_family_markdown_report(sample_summary, dummy_df)
    assert "# Phase 126: Master Regime Family Registry Report" in md_fam

    md_ctx = build_regime_context_markdown_report(sample_summary, dummy_df)
    assert "# Phase 126: Regime Environmental Contexts Report" in md_ctx

    md_dep = build_regime_contract_dependency_markdown_report(sample_summary, dummy_df)
    assert "# Phase 126: Regime Contracts and Dependencies Report" in md_dep

    md_man = build_regime_manifest_markdown_report(sample_summary, dummy_df)
    assert "# Phase 126: Regime Foundation Manifest Report" in md_man

    md_health = build_regime_health_markdown_report(sample_summary, dummy_df)
    assert "# Phase 126: Regime Foundation Health Check Report" in md_health

    md_val = build_regime_validation_markdown_report(sample_summary, dummy_df)
    assert "# Phase 126: Regime Foundation Validation Report" in md_val

    md_safety = build_regime_safety_markdown_report(sample_summary, dummy_df)
    assert "# Phase 126: Regime Foundation Safety Boundary Report" in md_safety

    md_hand = build_phase_127_handoff_markdown_report(sample_summary, dummy_df)
    assert "# Phase 126: Phase 127 Regime Feature Matrix Handoff Report" in md_hand
