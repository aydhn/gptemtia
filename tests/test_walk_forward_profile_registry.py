# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: Walk-Forward Profile Registry."""

from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_profile_registry import (
    build_walk_forward_profile_registry,
    summarize_walk_forward_profiles,
)


def test_build_walk_forward_profile_registry():
    prof = get_default_walk_forward_profile()
    df, summary = build_walk_forward_profile_registry(prof)
    assert not df.empty
    assert len(df) == 3
    assert "profile_name" in df.columns
    assert (df["current_phase"] == 147).all()
    assert (df["target_final_phase"] == 160).all()
    assert (df["next_phase"] == 148).all()
    assert (df["allow_live_trading"] == False).all()
    assert (df["allow_broker_integration"] == False).all()

    assert summary["total_profiles"] == 3
    assert summary["current_phase"] == 147
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 148
    assert summary["all_local_only"] is True
    assert summary["zero_live_trading"] is True


def test_summarize_walk_forward_profiles():
    prof = get_default_walk_forward_profile()
    df, _ = build_walk_forward_profile_registry(prof)
    summary = summarize_walk_forward_profiles(df, prof)
    assert summary["active_profile"] == prof.profile_name
    assert summary["total_profiles"] == 3
