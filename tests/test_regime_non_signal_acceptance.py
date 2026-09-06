"""Tests for Regime Non-Signal Acceptance."""

from advanced_regime_validation_acceptance.regime_non_signal_acceptance import (
    build_regime_non_signal_acceptance_report,
    validate_non_signal_text,
    summarize_non_signal_acceptance,
    FORBIDDEN_SIGNAL_CLAIMS,
)


def test_non_signal_acceptance():
    df, summary = build_regime_non_signal_acceptance_report()
    assert not df.empty
    assert summary["non_signal_certified"] is True

    s_df = summarize_non_signal_acceptance(df)
    assert s_df["non_signal"] is True

    # Validate clean descriptive text
    clean_text = "This report evaluates historical market volatility regimes using offline statistical metrics."
    assert validate_non_signal_text(clean_text)["passed"] is True

    # Validate forbidden claims
    for claim in FORBIDDEN_SIGNAL_CLAIMS:
        dirty_text = f"Notice: {claim} in current regime."
        res = validate_non_signal_text(dirty_text)
        assert res["passed"] is False
        assert len(res["violations_found"]) >= 1
