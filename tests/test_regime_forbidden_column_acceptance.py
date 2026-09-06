"""Tests for Regime Forbidden Column Acceptance."""

from advanced_regime_validation_acceptance.regime_forbidden_column_acceptance import (
    build_regime_forbidden_column_acceptance_report,
    validate_forbidden_regime_columns,
    summarize_regime_forbidden_column_acceptance,
    FORBIDDEN_REGIME_COLUMNS,
)


def test_forbidden_column_acceptance():
    df, summary = build_regime_forbidden_column_acceptance_report()
    assert not df.empty
    assert summary["all_rules_active"] is True

    s_df = summarize_regime_forbidden_column_acceptance(df)
    assert s_df["all_rules_active"] is True

    # Validate clean columns
    clean_cols = ["asset_id", "timestamp", "volatility_regime", "trend_strength", "liquidity_index"]
    assert validate_forbidden_regime_columns(clean_cols)["passed"] is True

    # Validate forbidden columns
    for forbidden in ["signal", "buy", "sell", "target", "label", "prediction", "future_return", "full_text", "sentiment", "embedding"]:
        res = validate_forbidden_regime_columns(["asset_id", forbidden])
        assert res["passed"] is False
        assert len(res["forbidden_found"]) >= 1
