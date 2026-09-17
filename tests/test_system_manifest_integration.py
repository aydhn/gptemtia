# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 System Manifest Integration."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_manifest_integration import (
    build_system_manifest_integration_registry,
)


def test_system_manifest():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_manifest_integration_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 10
    assert "manifest_integration_id" in df.columns
    assert "manifest_name" in df.columns
    assert "origin_phase" in df.columns
    assert "manifest_verified" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_manifests_integrated"] == len(df)
    assert summary["all_manifests_verified"] is True
    assert summary["non_signal"] is True
