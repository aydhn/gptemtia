# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Scope Registry."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.full_system_integration_scope_registry import (
    build_full_system_integration_scope_registry,
)


def test_scope_registry():
    profile = get_default_full_system_integration_profile()
    df, summary = build_full_system_integration_scope_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 10
    assert "scope_id" in df.columns
    assert "scope_item" in df.columns
    assert "is_allowed" in df.columns
    assert "category" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_scope_items"] == len(df)
    assert summary["permitted_count"] > 0
    assert summary["prohibited_count"] > 0
    assert summary["non_signal"] is True
