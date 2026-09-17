# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Advanced Acceptance Rehearsal Checkpoints."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.advanced_acceptance_rehearsal_checkpoints import (
    build_advanced_acceptance_rehearsal_checkpoint_registry,
)


def test_acceptance_rehearsal_checkpoints():
    profile = get_default_full_system_integration_profile()
    df, summary = build_advanced_acceptance_rehearsal_checkpoint_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 8
    assert "checkpoint_id" in df.columns
    assert "checkpoint_name" in df.columns
    assert "passed" in df.columns
    assert "status" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_checkpoints"] == len(df)
    assert summary["all_passed"] is True
    assert summary["non_signal"] is True
