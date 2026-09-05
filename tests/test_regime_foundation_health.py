from advanced_regime_foundation.regime_foundation_health import (
    build_regime_foundation_health_check,
    summarize_regime_foundation_health,
)


def test_regime_foundation_health():
    df, summary = build_regime_foundation_health_check()
    assert not df.empty
    assert summary["health_status"] == "HEALTHY"
    assert summary["unhealthy_checks"] == 0
    assert summary["non_signal"] is True

    summ = summarize_regime_foundation_health(df)
    assert summ["all_healthy"] is True
    assert summ["non_signal"] is True
