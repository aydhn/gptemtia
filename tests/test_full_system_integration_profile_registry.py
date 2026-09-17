# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Profile Registry."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.full_system_integration_profile_registry import (
    build_full_system_integration_profile_registry,
    summarize_full_system_integration_profiles,
)


def test_profile_registry():
    profile = get_default_full_system_integration_profile()
    df, summary = build_full_system_integration_profile_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 3
    assert "profile_name" in df.columns
    assert "non_signal" in df.columns
    assert "dry_run" in df.columns
    assert "non_production" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["current_phase"] == 158
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 159
    assert summary["all_non_signal"] is True
    assert summary["all_dry_run"] is True
    assert summary["all_non_production"] is True
    assert summary["all_broker_ready_false"] is True


def test_summarize_profiles():
    profile = get_default_full_system_integration_profile()
    df, _ = build_full_system_integration_profile_registry(profile)
    summary = summarize_full_system_integration_profiles(df, profile)
    assert summary["total_profiles"] == len(df)
