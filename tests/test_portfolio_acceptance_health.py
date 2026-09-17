# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Health Check."""

from pathlib import Path
import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    HEALTH_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)
from advanced_portfolio_acceptance.portfolio_acceptance_health import (
    HEALTH_CHECKS,
    build_portfolio_acceptance_health_check,
    summarize_portfolio_acceptance_health,
)


def test_health_check_structure():
    """Verify health check inspects required modules and subsystems."""
    df, summary = build_portfolio_acceptance_health_check()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(HEALTH_CHECKS)

    expected_cols = {
        "check_id",
        "description",
        "status",
        "passed",
        "current_phase",
    }
    assert expected_cols.issubset(df.columns)

    # In our repository, all required modules should exist
    assert all(df["passed"])
    assert all(df["status"] == "PASS")

    assert isinstance(summary, dict)
    assert summary["domain"] == HEALTH_DOMAIN
    assert summary["total_checks"] == len(HEALTH_CHECKS)
    assert summary["passed_checks"] == len(HEALTH_CHECKS)
    assert summary["all_passed"] is True
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_health_check_empty():
    """Verify summarize with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_health(empty_df)
    assert summary["total_checks"] == 0
    assert summary["all_passed"] is False
