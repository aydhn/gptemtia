from advanced_feature_grid.feature_grid_warmup_nan_policy import (
    build_feature_grid_warmup_nan_policy_registry,
    estimate_grid_warmup_nan_count,
    summarize_feature_grid_warmup_nan_policy,
)


def test_feature_grid_warmup_nan_policy():
    df, summary = build_feature_grid_warmup_nan_policy_registry()
    assert not df.empty
    assert summary["auto_drop_allowed"] is False
    assert summary["forward_fill_allowed"] is False
    assert summary["policy"] == "preserve_warmup_nan"

    # Test estimation
    est_sma_20 = estimate_grid_warmup_nan_count("sma", {"window": 20})
    assert est_sma_20 == 19

    est_rsi_14 = estimate_grid_warmup_nan_count("rsi", {"window": 14})
    assert est_rsi_14 == 14

    est_sma_200 = estimate_grid_warmup_nan_count("sma", {"window": 200})
    assert est_sma_200 == 199
