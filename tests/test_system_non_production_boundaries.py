# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 System Non-Production Boundaries."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_non_production_boundaries import (
    build_system_non_production_boundary_registry,
)


def test_system_non_production_boundaries():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_non_production_boundary_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 5
    assert "boundary_id" in df.columns
    assert "rule_name" in df.columns
    assert "is_allowed" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_rules"] == len(df)
    assert summary["prohibited_actions_count"] >= 5
    assert summary["non_signal"] is True
