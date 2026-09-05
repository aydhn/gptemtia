import pytest
from advanced_factor_metadata.mean_reversion_factor_families import (
    build_mean_reversion_factor_family_registry,
    summarize_mean_reversion_factor_family,
)


def test_build_mean_reversion_factor_family_registry():
    df, summary = build_mean_reversion_factor_family_registry()
    assert not df.empty
    assert summary["total_factors"] >= 4
    assert summary["non_signal"] is True

    names = list(df["factor_name"])
    assert "factor_mean_reversion_zscore_context" in names
    assert "factor_mean_reversion_distance_to_ma_context" in names
    assert "factor_mean_reversion_percentile_placeholder" in names
    assert "factor_mean_reversion_bollinger_context" in names

    stats = summarize_mean_reversion_factor_family(df)
    assert stats["total_factors"] == len(df)
    assert stats["non_signal"] is True
