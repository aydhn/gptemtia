"""Test suite for Phase 135 Health Check."""

from pathlib import Path
from advanced_regime_acceptance.regime_acceptance_health import (
    build_regime_acceptance_health_check,
    summarize_regime_acceptance_health,
)


def test_health_check():
    root = Path(__file__).resolve().parent.parent
    df, summary = build_regime_acceptance_health_check(root)
    assert not df.empty
    assert summary["total_checks"] >= 15
    assert summary["all_healthy"] is True
    assert summary["non_signal"] is True

    s2 = summarize_regime_acceptance_health(df)
    assert s2["all_healthy"] is True
