# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 System Component Registry."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_component_registry import (
    build_system_component_registry,
    summarize_system_components,
)


def test_system_component_registry():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_component_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 20
    assert "component_id" in df.columns
    assert "component_name" in df.columns
    assert "layer_name" in df.columns
    assert "module_name" in df.columns
    assert "contract_only" in df.columns

    assert summary["total_components"] == len(df)
    assert summary["all_contract_only"] is True
    assert summary["all_non_production"] is True
    assert summary["all_production_ready_false"] is True
    assert summary["all_broker_ready_false"] is True
    assert summary["all_live_ready_false"] is True
    assert summary["all_system_executed_false"] is True
    assert summary["non_signal"] is True
