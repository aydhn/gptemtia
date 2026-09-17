# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Model Profile Registry."""

from advanced_ensemble_model_registry.ensemble_model_profile_registry import (
    build_ensemble_model_profile_registry,
    validate_ensemble_model_profile_registry,
    summarize_ensemble_model_profiles,
)


def test_build_ensemble_model_profile_registry():
    df, summary = build_ensemble_model_profile_registry()
    assert not df.empty
    assert len(df) == 3
    assert summary["total_profiles"] == 3
    assert summary["all_dry_run"] is True
    assert summary["all_local_only"] is True
    assert summary["all_non_signal"] is True
    assert summary["real_training_allowed"] is False
    assert summary["ensemble_execution_allowed"] is False


def test_validate_ensemble_model_profile_registry():
    df, summary = build_ensemble_model_profile_registry()
    assert validate_ensemble_model_profile_registry(df, summary) is True
