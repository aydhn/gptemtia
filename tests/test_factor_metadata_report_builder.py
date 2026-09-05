import pytest
from advanced_factor_metadata.factor_metadata_report_builder import (
    build_factor_contract_markdown_report,
    build_factor_dependency_markdown_report,
    build_factor_family_markdown_report,
    build_factor_health_markdown_report,
    build_factor_manifest_markdown_report,
    build_factor_metadata_disclaimer,
    build_factor_metadata_profile_markdown_report,
    build_factor_safety_markdown_report,
    build_factor_validation_markdown_report,
    build_macro_event_news_factor_markdown_report,
    build_phase_123_handoff_markdown_report,
    build_technical_factor_markdown_report,
)


def test_factor_metadata_report_builder_reports():
    disclaimer = build_factor_metadata_disclaimer()
    assert "Phase 122 Factor Metadata" in disclaimer
    assert "kesin AL/SAT" in disclaimer

    dummy_summary = {
        "active_profile": "balanced",
        "total_profiles": 3,
        "current_phase": 122,
        "target_final_phase": 160,
        "next_phase": 123,
        "dry_run_default": True,
        "non_signal": True,
        "status": "factor_ready",
        "total_families": 12,
        "total_contracts": 12,
        "total_dependencies": 15,
        "total_manifest_items": 12,
        "total_factors": 4,
        "health_status": "HEALTHY",
        "safety_status": "SECURE",
        "handoff_status": "READY",
    }

    rep_prof = build_factor_metadata_profile_markdown_report(dummy_summary)
    assert "# Phase 122: Factor Metadata Profile Report" in rep_prof

    rep_fam = build_factor_family_markdown_report(dummy_summary)
    assert "# Phase 122: Factor Family Taxonomy Report" in rep_fam

    rep_cntr = build_factor_contract_markdown_report(dummy_summary)
    assert "# Phase 122: Factor Contract Registry Report" in rep_cntr

    rep_dep = build_factor_dependency_markdown_report(dummy_summary)
    assert "# Phase 122: Factor Dependency Registry Report" in rep_dep

    rep_manf = build_factor_manifest_markdown_report(dummy_summary)
    assert "# Phase 122: Factor Metadata Manifest Report" in rep_manf

    rep_tech = build_technical_factor_markdown_report(dummy_summary)
    assert "# Phase 122: Technical Factor Families Report" in rep_tech

    rep_macro = build_macro_event_news_factor_markdown_report(dummy_summary)
    assert "# Phase 122: Macro, Calendar Event & News Factor Families Report" in rep_macro

    rep_val = build_factor_validation_markdown_report(dummy_summary)
    assert "# Phase 122: Factor Validation Report" in rep_val

    rep_health = build_factor_health_markdown_report(dummy_summary)
    assert "# Phase 122: Factor Metadata Health Check Report" in rep_health

    rep_safety = build_factor_safety_markdown_report(dummy_summary)
    assert "# Phase 122: Factor Safety Boundary Report" in rep_safety

    rep_ho = build_phase_123_handoff_markdown_report(dummy_summary)
    assert "# Phase 122 to Phase 123: Feature Quality & Drift Handoff Report" in rep_ho
