# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 System Safety Boundaries."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_safety_boundaries import (
    build_system_safety_boundary_registry,
)


def test_system_safety_boundaries():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_safety_boundary_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 15
    assert "boundary_id" in df.columns
    assert "rule_name" in df.columns
    assert "is_allowed" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_rules"] == len(df)
    assert summary["prohibited_actions_count"] > 10
    assert summary["allowed_actions_count"] > 0
    assert summary["non_signal"] is True
