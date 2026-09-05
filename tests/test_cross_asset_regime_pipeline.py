"""Tests for Cross-Asset Regime Pipeline."""

from advanced_cross_asset_regime_context.cross_asset_regime_pipeline import (
    CrossAssetRegimePipeline,
)


def test_cross_asset_regime_pipeline_run_all():
    pipeline = CrossAssetRegimePipeline()
    results = pipeline.run_all(save=False)
    dfs = results["dataframes"]
    summaries = results["summaries"]

    assert len(dfs) >= 30
    assert "profiles" in dfs
    assert "pairs" in dfs
    assert "fx_commodity" in dfs
    assert "volatility_linkage" in dfs
    assert "contracts" in dfs
    assert "manifest" in dfs
    assert "health" in dfs
    assert "validation" in dfs
    assert "safety" in dfs
    assert "handoff" in dfs

    s_pipe = summaries["pipeline"]
    assert s_pipe["current_phase"] == 131
    assert s_pipe["next_phase"] == 132
    assert s_pipe["target_final_phase"] == 160
    assert s_pipe["non_signal"] is True
    assert s_pipe["official_approval"] is False
    assert s_pipe["production_ready"] is False
