"""Tests for Regime Transition Source Phases."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_source_phases import (
    build_regime_transition_source_phase_registry,
    summarize_regime_transition_source_phases,
    SOURCE_PHASES,
)


def test_build_regime_transition_source_phase_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_regime_transition_source_phase_registry(profile)

    assert not df.empty
    assert len(df) == 7
    assert "source_phase" in df.columns

    assert summary["total_source_phases"] == 7
    assert summary["all_source_preserved"] is True
    assert summary["all_read_only"] is True


def test_summarize_regime_transition_source_phases():
    profile = get_default_regime_transition_profile()
    df, _ = build_regime_transition_source_phase_registry(profile)
    summary = summarize_regime_transition_source_phases(df)
    assert summary["total_source_phases"] == 7
    assert summary["all_source_preserved"] is True
