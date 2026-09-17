# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 System Component Dependencies."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_component_dependencies import (
    build_system_component_dependency_registry,
)


def test_system_component_dependencies():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_component_dependency_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 25
    assert "dependency_id" in df.columns
    assert "source_component" in df.columns
    assert "target_component" in df.columns
    assert "dependency_type" in df.columns
    assert "status" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_dependencies"] == len(df)
    assert summary["hard_dependencies"] > 0
    assert summary["soft_dependencies"] > 0
    assert summary["all_contract_only"] is True
    assert summary["all_non_production"] is True
    assert summary["non_signal"] is True
