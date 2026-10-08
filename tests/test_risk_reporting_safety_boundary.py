"""Unit tests for Phase 155 Risk Reporting Safety Boundary."""

import pandas as pd

from advanced_risk_reporting.risk_reporting_config import get_risk_reporting_profile
from advanced_risk_reporting.risk_reporting_safety_boundary import (
    NO_GO_CONDITIONS,
    SAFE_GO_CONDITIONS,
    build_risk_reporting_no_go_conditions,
    build_risk_reporting_safe_go_conditions,
    build_risk_reporting_safety_boundary,
)


def test_build_risk_reporting_no_go_conditions():
    """Test building NO-GO conditions with default profile."""
    df, summary = build_risk_reporting_no_go_conditions()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(NO_GO_CONDITIONS)
    assert summary["no_go_count"] == len(NO_GO_CONDITIONS)
    assert summary["all_blocked"] is True

    # Check DataFrame columns
    expected_cols = [
        "condition",
        "status",
        "enforcement",
        "current_phase",
        "target_final_phase",
        "next_phase",
    ]
    for col in expected_cols:
        assert col in df.columns

    assert (df["status"] == "PROHIBITED").all()
    assert (df["enforcement"] == "HARD_BLOCK").all()


def test_build_risk_reporting_safe_go_conditions():
    """Test building SAFE-GO conditions with default profile."""
    df, summary = build_risk_reporting_safe_go_conditions()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(SAFE_GO_CONDITIONS)
    assert summary["safe_go_count"] == len(SAFE_GO_CONDITIONS)
    assert summary["all_contract_only"] is True

    # Check DataFrame columns
    expected_cols = [
        "condition",
        "status",
        "enforcement",
        "current_phase",
        "target_final_phase",
        "next_phase",
    ]
    for col in expected_cols:
        assert col in df.columns

    assert (df["status"] == "PERMITTED_CONTRACT_ONLY").all()
    assert (df["enforcement"] == "NON_EXECUTING_OFFLINE").all()


def test_build_risk_reporting_safety_boundary():
    """Test combined safety boundary report."""
    df, summary = build_risk_reporting_safety_boundary()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(NO_GO_CONDITIONS) + len(SAFE_GO_CONDITIONS)

    assert summary["no_go_count"] == len(NO_GO_CONDITIONS)
    assert summary["safe_go_count"] == len(SAFE_GO_CONDITIONS)
    assert summary["total_conditions"] == len(NO_GO_CONDITIONS) + len(
        SAFE_GO_CONDITIONS
    )
    assert summary["status"] == "SAFETY_BOUNDARY_ACTIVE"


def test_functions_with_custom_profile():
    """Test the functions passing a custom profile."""
    profile = get_risk_reporting_profile("strict_non_production_risk_reporting_safety")

    df_no, _sum_no = build_risk_reporting_no_go_conditions(profile)
    assert (df_no["current_phase"] == profile.current_phase).all()

    df_safe, _sum_safe = build_risk_reporting_safe_go_conditions(profile)
    assert (df_safe["current_phase"] == profile.current_phase).all()

    df_combined, sum_combined = build_risk_reporting_safety_boundary(profile)
    assert (df_combined["current_phase"] == profile.current_phase).all()
    assert sum_combined["current_phase"] == profile.current_phase
