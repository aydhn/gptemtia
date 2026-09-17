# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 System Manual Review Gates."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_manual_review_gates import (
    build_system_manual_review_gate_registry,
)


def test_system_manual_review_gates():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_manual_review_gate_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 10
    assert "item_id" in df.columns
    assert "gate_name" in df.columns
    assert "title" in df.columns
    assert "status" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_review_gates"] == len(df)
    assert summary["pending_review_count"] == len(df)
    assert summary["non_signal"] is True
