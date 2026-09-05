"""Tests for Regime Transition Report Builder."""

import pandas as pd
from advanced_regime_transition.regime_transition_report_builder import (
    build_regime_transition_disclaimer,
    build_regime_transition_profile_markdown_report,
    build_state_sequence_contract_markdown_report,
    build_transition_metric_markdown_report,
    build_state_transition_diagnostics_markdown_report,
    build_regime_family_transition_markdown_report,
    build_macro_news_cross_asset_transition_markdown_report,
    build_transition_findings_markdown_report,
    build_transition_stability_score_markdown_report,
    build_transition_manifest_markdown_report,
    build_regime_transition_validation_markdown_report,
    build_regime_transition_safety_markdown_report,
    build_phase_131_handoff_markdown_report,
    build_regime_transition_health_markdown_report,
)


def test_regime_transition_report_builder_reports():
    summary = {
        "active_profile": "test_profile",
        "current_phase": 130,
        "next_phase": 131,
        "target_final_phase": 160,
        "stability_score": 0.82,
    }
    df = pd.DataFrame([{"col1": "val1", "col2": "val2"}])

    rep_prof = build_regime_transition_profile_markdown_report(summary, df)
    assert "Phase 130: Regime Transition Profile Registry Report" in rep_prof
    assert "val1" in rep_prof

    rep_cont = build_state_sequence_contract_markdown_report(summary, df)
    assert "State Sequence Contract" in rep_cont

    rep_met = build_transition_metric_markdown_report(summary, df)
    assert "Transition & Stability Metric Registry" in rep_met

    rep_diag = build_state_transition_diagnostics_markdown_report(summary, df)
    assert "State Transition Diagnostics" in rep_diag

    rep_fam = build_regime_family_transition_markdown_report(summary, df)
    assert "Regime Family Transition" in rep_fam

    rep_ctx = build_macro_news_cross_asset_transition_markdown_report(summary, df)
    assert "Macro, News & Cross-Asset" in rep_ctx

    rep_find = build_transition_findings_markdown_report(summary, df)
    assert "Transition Quality Findings" in rep_find

    rep_scr = build_transition_stability_score_markdown_report(summary, df)
    assert "Transition Stability Scoring" in rep_scr

    rep_man = build_transition_manifest_markdown_report(summary, df)
    assert "Transition Diagnostics Manifest" in rep_man

    rep_val = build_regime_transition_validation_markdown_report(summary, df)
    assert "Regime Transition Validation" in rep_val

    rep_sft = build_regime_transition_safety_markdown_report(summary, df)
    assert "Regime Transition Safety Boundary" in rep_sft

    rep_han = build_phase_131_handoff_markdown_report(summary, df)
    assert "Phase 131 Cross-Asset Regime Context Handoff" in rep_han

    rep_hlth = build_regime_transition_health_markdown_report(summary, df)
    assert "Regime Transition Health Check" in rep_hlth
