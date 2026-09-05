from advanced_technical_indicators.technical_indicator_report_builder import (
    build_technical_indicator_disclaimer,
    build_technical_indicator_profile_markdown_report,
    build_technical_indicator_catalog_markdown_report,
    build_indicator_family_markdown_report,
    build_indicator_rehearsal_markdown_report,
    build_indicator_validation_markdown_report,
    build_technical_indicator_health_markdown_report,
    build_technical_indicator_safety_markdown_report,
    build_phase_118_handoff_markdown_report,
)


def test_technical_indicator_report_builder():
    disc = build_technical_indicator_disclaimer()
    assert "Phase 117" in disc
    assert "Canlı emir" in disc

    md_prof = build_technical_indicator_profile_markdown_report({"total_profiles": 3})
    assert "# Phase 117 Technical Indicator Profile Registry Report" in md_prof

    md_cat = build_technical_indicator_catalog_markdown_report({"total_indicators": 50})
    assert "Catalog Expansion" in md_cat

    md_reh = build_indicator_rehearsal_markdown_report({"total_rehearsals": 62, "all_passed": True})
    assert "Computation Rehearsal" in md_reh

    md_ho = build_phase_118_handoff_markdown_report({"handoff_status": "READY", "next_phase": 118})
    assert "Phase 118" in md_ho
