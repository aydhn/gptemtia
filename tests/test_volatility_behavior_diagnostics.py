from advanced_market_behavior_diagnostics.volatility_behavior_diagnostics import (
    build_volatility_behavior_diagnostics_report,
    summarize_volatility_behavior_diagnostics,
)


def test_volatility_behavior_diagnostics():
    df, summary = build_volatility_behavior_diagnostics_report()

    assert not df.empty
    assert "context_name" in df.columns
    assert summary["all_ready"] is True
    assert summary["dependencies_passed"] is True
    assert summary["non_signal"] is True
