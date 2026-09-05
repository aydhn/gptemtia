from advanced_market_behavior_diagnostics.cross_asset_behavior_diagnostics import (
    build_cross_asset_behavior_diagnostics_report,
    summarize_cross_asset_behavior_diagnostics,
)


def test_cross_asset_behavior_diagnostics():
    df, summary = build_cross_asset_behavior_diagnostics_report()

    assert not df.empty
    assert "context_name" in df.columns
    assert summary["all_ready"] is True
    assert summary["dependencies_passed"] is True
    assert summary["non_signal"] is True
