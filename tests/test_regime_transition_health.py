"""Tests for Regime Transition Health Check."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_health import (
    build_regime_transition_health_check,
    summarize_regime_transition_health,
)


def test_build_regime_transition_health_check():
    profile = get_default_regime_transition_profile()
    df, summary = build_regime_transition_health_check(profile=profile)

    assert not df.empty
    assert len(df) >= 14
    assert "check_item" in df.columns
    assert "status" in df.columns

    assert summary["health_status"] == "HEALTHY"
    assert summary["failed_checks"] == 0
    assert summary["is_healthy"] is True
    assert summary["non_signal"] is True
