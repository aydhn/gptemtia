from advanced_market_behavior_diagnostics.market_behavior_diagnostics_health import (
    build_market_behavior_diagnostics_health_check,
    summarize_market_behavior_diagnostics_health,
)


def test_market_behavior_diagnostics_health():
    df, summary = build_market_behavior_diagnostics_health_check()

    assert not df.empty
    assert summary["all_healthy"] is True
    assert summary["total_checks"] >= 10
    assert summary["non_signal"] is True
