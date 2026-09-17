# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Advanced Acceptance Rehearsal."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.advanced_acceptance_rehearsal import (
    build_advanced_acceptance_rehearsal_registry,
)


def test_acceptance_rehearsal():
    profile = get_default_full_system_integration_profile()
    df, summary = build_advanced_acceptance_rehearsal_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 10
    assert "rehearsal_id" in df.columns
    assert "rehearsal_name" in df.columns
    assert "is_satisfied" in df.columns
    assert "zero_execution_verified" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_rehearsals"] == len(df)
    assert summary["all_satisfied"] is True
    assert summary["all_zero_execution_verified"] is True
    assert summary["non_signal"] is True
