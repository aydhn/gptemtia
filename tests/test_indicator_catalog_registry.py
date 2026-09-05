from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.indicator_catalog_registry import (
    build_indicator_catalog_registry,
    summarize_indicator_catalog_registry,
)


def test_indicator_catalog_registry():
    profile = get_default_feature_engine_profile()
    df, summary = build_indicator_catalog_registry(profile)

    assert not df.empty
    assert len(df) >= 30
    assert "indicator_name" in df.columns
    assert "indicator_family" in df.columns
    assert "non_signal_usage_note" in df.columns

    families = set(df["indicator_family"].unique())
    assert "price" in families
    assert "trend" in families
    assert "momentum" in families
    assert "volatility" in families
    assert "mean_reversion" in families
    assert summary["all_non_signal"] is True
