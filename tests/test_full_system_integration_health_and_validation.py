# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Health, Validation, and Safety Boundary."""

from pathlib import Path
import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.full_system_integration_health import (
    build_full_system_integration_health_check,
)
from advanced_full_system_integration.full_system_integration_validation import (
    build_full_system_integration_validation_report,
)
from advanced_full_system_integration.full_system_integration_safety_boundary import (
    build_full_system_integration_safety_boundary,
    build_full_system_integration_no_go_conditions,
    build_full_system_integration_safe_go_conditions,
)
from advanced_full_system_integration.full_system_integration_profile_registry import (
    build_full_system_integration_profile_registry,
)
from advanced_full_system_integration.system_component_checkpoints import (
    build_system_component_checkpoint_registry,
)
from advanced_full_system_integration.system_contract_integration import (
    build_system_contract_integration_registry,
)
from advanced_full_system_integration.advanced_acceptance_rehearsal import (
    build_advanced_acceptance_rehearsal_registry,
)
from advanced_full_system_integration.full_system_integration_manifest import (
    build_full_system_integration_manifest,
)


def test_health_check():
    profile = get_default_full_system_integration_profile()
    project_root = Path(".")
    df, summary = build_full_system_integration_health_check(project_root, profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 20
    assert summary["active_profile"] == profile.profile_name
    assert summary["all_healthy"] is True
    assert summary["missing_count"] == 0
    assert summary["non_signal"] is True


def test_validation_report():
    profile = get_default_full_system_integration_profile()
    df_prof, _ = build_full_system_integration_profile_registry(profile)
    df_chk, _ = build_system_component_checkpoint_registry(profile)
    df_cnt, _ = build_system_contract_integration_registry(profile)
    df_reh, _ = build_advanced_acceptance_rehearsal_registry(profile)
    df_mnf, _ = build_full_system_integration_manifest(profile)

    eval_tables = {
        "profiles": df_prof,
        "checkpoints": df_chk,
        "contracts": df_cnt,
        "rehearsal": df_reh,
        "manifest": df_mnf,
        "summary": {"active_profile": profile.profile_name},
    }
    df, summary = build_full_system_integration_validation_report(eval_tables, profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 6
    assert summary["all_passed"] is True
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["non_signal"] is True


def test_safety_boundary():
    profile = get_default_full_system_integration_profile()
    df, summary = build_full_system_integration_safety_boundary(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 25
    assert summary["active_profile"] == profile.profile_name
    assert summary["no_go_count"] >= 20
    assert summary["safe_go_count"] >= 5
    assert summary["non_signal"] is True

    no_go = build_full_system_integration_no_go_conditions(profile)
    assert len(no_go) >= 20

    safe_go = build_full_system_integration_safe_go_conditions(profile)
    assert len(safe_go) >= 5
