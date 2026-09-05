from advanced_feature_store_integration.feature_store_factor_registry import (
    build_feature_store_factor_registry,
    summarize_feature_store_factor_registry,
)

def test_factor_registry():
    df, s = build_feature_store_factor_registry()
    assert not df.empty
    assert s["total_factors"] >= 6
    assert "technical" in s["factor_families"]
    assert "trend" in s["factor_families"]
    assert "volatility" in s["factor_families"]
    assert all(df["non_signal"])
    assert all(df["source_preserved"])
    assert not any(df["destructive_action_allowed"])
    summary = summarize_feature_store_factor_registry(df)
    assert summary["all_non_signal"] is True
