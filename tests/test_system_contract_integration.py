# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 System Contract Integration."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_contract_integration import (
    build_system_contract_integration_registry,
)


def test_system_contracts():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_contract_integration_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 10
    assert "contract_id" in df.columns
    assert "subsystem_name" in df.columns
    assert "contract_type" in df.columns
    assert "zero_execution_guaranteed" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_contracts"] == len(df)
    assert summary["all_contract_only"] is True
    assert summary["all_non_production"] is True
    assert summary["all_zero_execution"] is True
    assert summary["non_signal"] is True
