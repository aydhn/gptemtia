import pytest
from advanced_factor_metadata.regime_prep_factor_placeholders import (
    build_regime_prep_factor_placeholder_registry,
    summarize_regime_prep_factor_placeholders,
)


def test_build_regime_prep_factor_placeholder_registry():
    df, summary = build_regime_prep_factor_placeholder_registry()
    assert not df.empty
    assert summary["total_factors"] >= 4
    assert summary["placeholder_factors"] == len(df)
    assert summary["non_signal"] is True
    assert "target_regime_phases" in summary

    names = list(df["factor_name"])
    assert "factor_regime_volatility_prep_placeholder" in names
    assert "factor_regime_trend_prep_placeholder" in names
    assert "factor_regime_macro_context_prep_placeholder" in names
    assert "factor_regime_event_context_prep_placeholder" in names

    stats = summarize_regime_prep_factor_placeholders(df)
    assert stats["total_factors"] == len(df)
    assert stats["manual_review_required"] is True
    assert stats["non_signal"] is True
