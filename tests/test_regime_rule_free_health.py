from advanced_regime_rule_free.regime_rule_free_health import (
    build_regime_rule_free_health_check,
    summarize_regime_rule_free_health,
    HEALTH_CHECKS,
)


def test_build_regime_rule_free_health_check():
    df, summary = build_regime_rule_free_health_check()
    assert len(df) == 12
    assert summary["total_checks"] == 12
    assert summary["passed_checks"] == 12
    assert summary["failed_checks"] == 0
    assert summary["all_healthy"] is True
    assert summary["health_status"] == "HEALTHY"

    assert len(HEALTH_CHECKS) == 12


def test_summarize_regime_rule_free_health():
    df, _ = build_regime_rule_free_health_check()
    sum_res = summarize_regime_rule_free_health(df)
    assert sum_res["all_healthy"] is True
