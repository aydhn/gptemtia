# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Model Config."""

import pytest
from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_ensemble_model_profile,
    get_default_ensemble_model_profile,
    list_ensemble_model_profiles,
    validate_ensemble_model_profile,
    validate_ensemble_model_profiles,
    PROFILES,
)


def test_ensemble_model_profiles_exist():
    profiles = list_ensemble_model_profiles()
    assert len(profiles) == 3
    assert "balanced_local_ensemble_model_contracts" in profiles
    assert "strict_non_executing_ensemble_safety" in profiles
    assert "dry_run_candidate_registry_focus" in profiles


def test_get_ensemble_model_profile():
    p1 = get_ensemble_model_profile("balanced_local_ensemble_model_contracts")
    assert p1.name == "balanced_local_ensemble_model_contracts"
    assert p1.current_phase == 140
    assert p1.target_final_phase == 160
    assert p1.next_phase == 141

    default_p = get_default_ensemble_model_profile()
    assert default_p.name == "balanced_local_ensemble_model_contracts"


def test_validate_ensemble_model_profiles():
    assert validate_ensemble_model_profiles() is True
    for p in PROFILES.values():
        assert validate_ensemble_model_profile(p) is True
        assert p.dry_run_default is True
        assert p.local_only is True
        assert p.non_production is True
        assert p.research_only is True
        assert p.allow_live_trading is False
        assert p.allow_real_model_training is False
        assert p.allow_ensemble_execution is False
        assert p.allow_calibration_execution is False
        assert p.allow_artifact_persistence is False
        assert p.allow_model_registry_write is False
