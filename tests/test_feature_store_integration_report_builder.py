from advanced_feature_store_integration.feature_store_integration_report_builder import (
    build_feature_store_integration_disclaimer,
    build_feature_store_integration_profile_markdown_report,
    build_feature_store_contract_markdown_report,
    build_feature_store_catalog_markdown_report,
    build_feature_store_manifest_markdown_report,
    build_feature_store_policy_markdown_report,
    build_feature_store_health_markdown_report,
    build_feature_store_validation_markdown_report,
    build_feature_store_safety_markdown_report,
    build_phase_125_handoff_markdown_report,
)

def test_report_builders():
    disclaimer = build_feature_store_integration_disclaimer()
    assert "Phase 124 Feature Store Integration Expansion" in disclaimer
    assert "Canli emir" in disclaimer or "Canlı emir" in disclaimer

    summary = {"active_profile": "test", "total_profiles": 1, "current_phase": 124}
    rep = build_feature_store_integration_profile_markdown_report(summary)
    assert "Phase 124 Feature Store Integration Profile Report" in rep

    hnd = build_phase_125_handoff_markdown_report({"handoff_status": "READY", "source_phase": 124, "next_phase": 125})
    assert "Phase 125" in hnd
