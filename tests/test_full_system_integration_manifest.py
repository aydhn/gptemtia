# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Full System Integration Manifest."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.full_system_integration_manifest import (
    build_full_system_integration_manifest,
)


def test_full_system_integration_manifest():
    profile = get_default_full_system_integration_profile()
    df, summary = build_full_system_integration_manifest(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert "manifest_id" in df.columns
    assert "full_system_integration_completed" in df.columns
    assert "production_ready" in df.columns

    assert summary["manifest_id"] == "MNF-158-FULL-SYSTEM-INTEGRATION-001"
    assert summary["current_phase"] == 158
    assert summary["full_system_integration_completed"] is True
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["live_trading_ready"] is False
