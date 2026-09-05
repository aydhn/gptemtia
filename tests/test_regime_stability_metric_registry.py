"""Tests for Regime Stability Metric Registry."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_stability_metric_registry import (
    build_regime_stability_metric_registry,
    summarize_regime_stability_metrics,
    STABILITY_METRIC_DEFINITIONS,
)


def test_build_regime_stability_metric_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_regime_stability_metric_registry(profile)

    assert not df.empty
    assert len(df) == 8
    assert "metric_name" in df.columns
    assert "metric_family" in df.columns
    assert (df["non_signal"] == True).all()
    assert (df["source_preserved"] == True).all()

    assert summary["total_metrics"] == 8
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_regime_stability_metrics():
    profile = get_default_regime_transition_profile()
    df, _ = build_regime_stability_metric_registry(profile)
    summary = summarize_regime_stability_metrics(df)
    assert summary["total_metrics"] == 8
    assert summary["all_source_preserved"] is True
