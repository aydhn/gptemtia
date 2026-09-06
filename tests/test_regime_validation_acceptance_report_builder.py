"""Tests for Regime Validation Acceptance Report Builder."""

import pandas as pd
from advanced_regime_validation_acceptance.regime_validation_acceptance_report_builder import (
    build_regime_validation_acceptance_disclaimer,
    build_regime_validation_acceptance_profile_markdown_report,
    build_regime_validation_gate_markdown_report,
    build_no_lookahead_acceptance_markdown_report,
    build_metadata_only_news_acceptance_markdown_report,
    build_component_acceptance_markdown_report,
    build_dependency_acceptance_markdown_report,
    build_regime_validation_findings_markdown_report,
    build_regime_acceptance_score_markdown_report,
    build_regime_validation_acceptance_manifest_markdown_report,
    build_regime_validation_acceptance_validation_markdown_report,
    build_regime_validation_acceptance_safety_markdown_report,
    build_phase_134_handoff_markdown_report,
)


def test_report_builder():
    disc = build_regime_validation_acceptance_disclaimer()
    assert "Phase 133 Regime Validation and No-Lookahead Acceptance" in disc
    assert "Canlı emir" in disc
    assert "kesin AL/SAT" in disc
    assert "yatırım tavsiyesi" in disc

    dummy_summary = {"current_phase": 133, "next_phase": 134, "target_final_phase": 160}
    dummy_df = pd.DataFrame([{"col1": "val1"}])

    rep_prof = build_regime_validation_acceptance_profile_markdown_report(dummy_summary, dummy_df)
    assert "# Phase 133: Regime Validation Acceptance Profile Registry Report" in rep_prof

    rep_gate = build_regime_validation_gate_markdown_report(dummy_summary)
    assert "# Phase 133: Regime Validation Gates Report" in rep_gate

    rep_nl = build_no_lookahead_acceptance_markdown_report(dummy_summary)
    assert "# Phase 133: Regime No-Lookahead Acceptance Report" in rep_nl

    rep_news = build_metadata_only_news_acceptance_markdown_report(dummy_summary)
    assert "# Phase 133: Regime Metadata-Only News Acceptance Report" in rep_news

    rep_comp = build_component_acceptance_markdown_report(dummy_summary)
    assert "# Phase 133: Regime Component Acceptance Report" in rep_comp

    rep_dep = build_dependency_acceptance_markdown_report(dummy_summary)
    assert "# Phase 133: Regime Dependency Acceptance Report" in rep_dep

    rep_find = build_regime_validation_findings_markdown_report(dummy_summary)
    assert "# Phase 133: Regime Validation Findings Report" in rep_find

    rep_score = build_regime_acceptance_score_markdown_report(dummy_summary)
    assert "# Phase 133: Regime Acceptance Score Report" in rep_score

    rep_mani = build_regime_validation_acceptance_manifest_markdown_report(dummy_summary)
    assert "# Phase 133: Regime Validation Acceptance Manifest" in rep_mani

    rep_val = build_regime_validation_acceptance_validation_markdown_report(dummy_summary)
    assert "# Phase 133: Regime Validation Acceptance Integrity Report" in rep_val

    rep_safe = build_regime_validation_acceptance_safety_markdown_report(dummy_summary)
    assert "# Phase 133: Regime Validation Acceptance Safety Boundary Report" in rep_safe

    rep_hand = build_phase_134_handoff_markdown_report(dummy_summary)
    assert "# Phase 133 -> Phase 134 Handoff Report" in rep_hand
