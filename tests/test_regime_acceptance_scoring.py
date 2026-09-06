"""Tests for Regime Acceptance Scoring."""

import pandas as pd
from advanced_regime_validation_acceptance.regime_acceptance_scoring import (
    calculate_regime_acceptance_score,
    build_regime_acceptance_score_report,
    classify_regime_acceptance_score,
    summarize_regime_acceptance_scores,
)


def test_acceptance_scoring():
    df, summary = build_regime_acceptance_score_report()
    assert not df.empty
    assert summary["overall_score"] == 1.0
    assert summary["non_signal"] is True

    s_df = summarize_regime_acceptance_scores(df)
    assert s_df["overall_score"] == 1.0
    assert s_df["non_signal"] is True

    # Test scoring penalty logic
    empty_findings = pd.DataFrame()
    score_clean = calculate_regime_acceptance_score(empty_findings)
    assert score_clean.overall_score == 1.0
    assert score_clean.manual_review_required is False

    critical_findings = pd.DataFrame([{"severity_label": "acceptance_critical"}])
    score_crit = calculate_regime_acceptance_score(critical_findings)
    assert score_crit.overall_score == 0.50
    assert score_crit.manual_review_required is True

    # Classification
    assert classify_regime_acceptance_score(0.95) == "high_acceptance_integrity"
    assert classify_regime_acceptance_score(0.50) == "acceptable_local_integrity"
    assert classify_regime_acceptance_score(0.30) == "marginal_acceptance_review_required"
    assert classify_regime_acceptance_score(0.10) == "acceptance_rejected"
