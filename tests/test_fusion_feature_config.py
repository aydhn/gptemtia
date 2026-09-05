"""Tests for Fusion Feature Configuration."""

import pytest
from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_fusion_feature_profile,
    list_fusion_feature_profiles,
    validate_fusion_feature_profile,
    validate_fusion_feature_profiles,
    get_default_fusion_feature_profile,
)


def test_default_profile():
    prof = get_default_fusion_feature_profile()
    assert prof.name == "balanced_local_macro_calendar_news_fusion"
    assert prof.current_phase == 120
    assert prof.target_final_phase == 160
    assert prof.next_phase == 121
    assert prof.local_only is True
    assert prof.dry_run_default is True
    assert prof.allow_live_trading is False
    assert prof.allow_fusion_feature_as_signal is False


def test_list_profiles():
    profiles = list_fusion_feature_profiles()
    names = [p.name for p in profiles]
    assert len(profiles) >= 3
    assert "balanced_local_macro_calendar_news_fusion" in names
    assert "strict_metadata_only_no_signal_fusion_safety" in names
    assert "dry_run_fusion_contract_focus" in names


def test_validate_profiles():
    assert validate_fusion_feature_profiles() is True


def test_invalid_profile():
    bad_prof = FusionFeatureProfile(
        name="bad_profile",
        description="test",
        current_phase=999,
    )
    with pytest.raises(ValueError):
        validate_fusion_feature_profile(bad_prof)
