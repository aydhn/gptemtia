"""Unit tests for Phase 119 cross-asset alignment configuration."""

import pytest
from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_cross_asset_alignment_profile,
    get_default_cross_asset_alignment_profile,
    list_available_cross_asset_alignment_profiles,
    validate_cross_asset_alignment_profile,
)


def test_default_profile_attributes():
    profile = get_default_cross_asset_alignment_profile()
    assert profile.name == "balanced_local_cross_asset_alignment"
    assert profile.current_phase == 119
    assert profile.target_final_phase == 160
    assert profile.next_phase == 120
    assert profile.dry_run_default is True
    assert profile.future_data_allowed is False
    assert profile.non_signal is True
    assert profile.local_only is True
    assert profile.research_only is True


def test_list_and_get_profiles():
    names = list_available_cross_asset_alignment_profiles()
    assert len(names) >= 3
    assert "balanced_local_cross_asset_alignment" in names
    assert "strict_no_signal_cross_asset_safety" in names
    assert "dry_run_cross_asset_alignment_focus" in names

    for name in names:
        p = get_cross_asset_alignment_profile(name)
        assert p.name == name
        assert validate_cross_asset_alignment_profile(p) is True


def test_unknown_profile_fallback():
    p = get_cross_asset_alignment_profile("non_existent_profile")
    assert p.name == "balanced_local_cross_asset_alignment"
