"""Tests for Regime Validation Acceptance Health Check."""

from advanced_regime_validation_acceptance.regime_validation_acceptance_health import (
    build_regime_validation_acceptance_health_check,
    summarize_regime_validation_acceptance_health,
)


def test_validation_acceptance_health():
    df, summary = build_regime_validation_acceptance_health_check()
    assert not df.empty
    assert summary["total_subsystems"] == len(df)
    assert summary["all_healthy"] is True
    assert summary["health_status"] == "HEALTHY"

    s_df = summarize_regime_validation_acceptance_health(df)
    assert s_df["all_healthy"] is True
