# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 System Validation Evidence."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_validation_evidence import (
    build_system_validation_evidence_registry,
)


def test_system_validation_evidence():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_validation_evidence_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 8
    assert "evidence_id" in df.columns
    assert "evidence_type" in df.columns
    assert "evidence_present" in df.columns
    assert "status" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_evidence_items"] == len(df)
    assert summary["all_evidence_present"] is True
    assert summary["non_signal"] is True
