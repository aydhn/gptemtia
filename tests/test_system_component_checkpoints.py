# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 System Component Checkpoints."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_component_checkpoints import (
    build_system_component_checkpoint_registry,
    validate_system_component_checkpoint,
)


def test_system_component_checkpoints():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_component_checkpoint_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 10
    assert "checkpoint_id" in df.columns
    assert "component_name" in df.columns
    assert "contract_only" in df.columns
    assert "dry_run" in df.columns
    assert "non_production" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_checkpoints"] == len(df)
    assert summary["all_contract_only"] is True
    assert summary["all_non_production"] is True
    assert summary["all_production_ready_false"] is True
    assert summary["all_broker_ready_false"] is True
    assert summary["all_live_ready_false"] is True
    assert summary["non_signal"] is True


def test_validate_checkpoint():
    valid_chk = {
        "production_ready": False,
        "broker_ready": False,
        "live_ready": False,
        "signal_ready": False,
        "contract_only": True,
    }
    res = validate_system_component_checkpoint(valid_chk)
    assert res["is_valid"] is True

    invalid_chk = {"production_ready": True, "broker_ready": False}
    res_inv = validate_system_component_checkpoint(invalid_chk)
    assert res_inv["is_valid"] is False
