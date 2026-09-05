from advanced_data_normalization.data_normalization_report_builder import (
    build_data_normalization_disclaimer,
    build_data_normalization_profile_markdown_report,
    build_normalization_rule_registry_markdown_report,
    build_symbol_normalization_markdown_report,
    build_data_normalization_health_markdown_report,
)


def test_report_builder_and_disclaimer():
    disc = build_data_normalization_disclaimer()
    assert "YASAL UYARI VE GÜVENLİK SINIRI" in disc
    assert "kesin AL/SAT" in disc
    assert "destructive cleaning" in disc

    prof_md = build_data_normalization_profile_markdown_report({"total_profiles": 3})
    assert "# Phase 113 — Data Normalization Profile Registry Report" in prof_md

    rule_md = build_normalization_rule_registry_markdown_report({"total_rules": 10, "domains": ["fx"]})
    assert "# Phase 113 — Normalization Rule Registry Report" in rule_md

    sym_md = build_symbol_normalization_markdown_report({"total_rules": 5})
    assert "# Phase 113 — Symbol & Indicator Normalization Enforcement Report" in sym_md

    h_md = build_data_normalization_health_markdown_report({"total_checks": 10, "overall_status": "PASS"})
    assert "# Phase 113 — Data Normalization Health Check Report" in h_md
