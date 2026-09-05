"""Tests for Phase 131 Cross-Asset Regime Configuration."""

import pytest
from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CROSS_ASSET_REGIME_PROFILES,
    get_cross_asset_regime_profile,
    get_default_cross_asset_regime_profile,
    list_cross_asset_regime_profiles,
    validate_cross_asset_regime_profiles,
)


def test_cross_asset_regime_config_profiles_exist():
    profiles = list_cross_asset_regime_profiles()
    assert len(profiles) >= 3
    assert "balanced_local_cross_asset_regime_context" in profiles
    assert "strict_non_signal_cross_asset_regime_safety" in profiles
    assert "dry_run_cross_asset_context_focus" in profiles


def test_cross_asset_regime_config_invariants():
    default_p = get_default_cross_asset_regime_profile()
    assert default_p.current_phase == 131
    assert default_p.target_final_phase == 160
    assert default_p.next_phase == 132
    assert default_p.dry_run_default is True
    assert default_p.local_only is True
    assert default_p.non_production is True
    assert default_p.research_only is True
    assert default_p.allow_live_trading is False
    assert default_p.allow_broker_integration is False
    assert default_p.allow_context_as_signal is False
    assert default_p.allow_correlation_as_signal is False
    assert default_p.allow_divergence_as_signal is False
    assert default_p.allow_directional_claim is False
    assert default_p.allow_clustering_execution is False
    assert default_p.allow_model_training is False
    assert default_p.allow_model_fit is False
    assert default_p.allow_model_predict is False
    assert default_p.allow_unsupervised_execution is False
    assert default_p.allow_target_label_generation is False
    assert default_p.allow_prediction_generation is False
    assert default_p.allow_source_overwrite is False
    assert default_p.allow_auto_imputation is False
    assert default_p.allow_auto_feature_drop is False


def test_validate_cross_asset_regime_profiles():
    assert validate_cross_asset_regime_profiles() is True


def test_unknown_cross_asset_profile_raises_key_error():
    with pytest.raises(KeyError):
        get_cross_asset_regime_profile("non_existent_profile")
