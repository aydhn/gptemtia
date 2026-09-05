"""Tests for Transition Diagnostics Manifest."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.transition_diagnostics_manifest import (
    build_transition_diagnostics_manifest,
    create_transition_diagnostics_manifest,
)


def test_build_transition_diagnostics_manifest():
    profile = get_default_regime_transition_profile()
    df, summary = build_transition_diagnostics_manifest(profile)

    assert not df.empty
    assert len(df) == 1
    assert "manifest_name" in df.columns
    assert "current_phase" in df.columns
    assert (df["current_phase"] == 130).all()
    assert (df["target_final_phase"] == 160).all()
    assert (df["next_phase"] == 131).all()
    assert (df["non_signal"] == True).all()
    assert (df["model_training_executed"] == False).all()
    assert (df["clustering_executed"] == False).all()

    assert summary["current_phase"] == 130
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 131
    assert summary["non_signal"] is True
    assert summary["is_valid"] is True
