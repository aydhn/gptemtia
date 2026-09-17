# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Blockers, Gaps, Warnings, and Findings."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_integration_blockers import (
    build_system_integration_blocker_registry,
)
from advanced_full_system_integration.system_integration_gaps import (
    build_system_integration_gap_registry,
)
from advanced_full_system_integration.system_integration_warnings import (
    build_system_integration_warning_registry,
)
from advanced_full_system_integration.system_integration_findings import (
    build_system_integration_findings_registry,
)


def test_blockers_registry():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_integration_blocker_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 15
    assert "blocker_id" in df.columns
    assert "is_active" in df.columns
    assert summary["active_profile"] == profile.profile_name
    assert summary["has_active_blockers"] is False
    assert summary["non_signal"] is True


def test_gaps_registry():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_integration_gap_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert summary["active_profile"] == profile.profile_name
    assert summary["non_signal"] is True


def test_warnings_registry():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_integration_warning_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert summary["active_profile"] == profile.profile_name
    assert summary["non_signal"] is True


def test_findings_registry():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_integration_findings_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert summary["active_profile"] == profile.profile_name
    assert summary["blocking_findings_count"] == 0
    assert summary["non_signal"] is True
