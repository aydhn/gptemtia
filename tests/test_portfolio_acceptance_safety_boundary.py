# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Safety Boundary."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    SAFETY_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)
from advanced_portfolio_acceptance.portfolio_acceptance_safety_boundary import (
    NO_GO_CONDITIONS,
    SAFE_GO_CONDITIONS,
    build_portfolio_acceptance_no_go_conditions,
    build_portfolio_acceptance_safe_go_conditions,
    build_portfolio_acceptance_safety_boundary,
)


def test_no_go_conditions_structure():
    """Verify NO-GO conditions build valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_no_go_conditions()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(NO_GO_CONDITIONS)
    assert summary["total_no_go"] == len(NO_GO_CONDITIONS)
    assert summary["all_enforced"] is True
    assert (df["type"] == "NO-GO").all()
    assert (df["enforced"] == True).all()


def test_safe_go_conditions_structure():
    """Verify SAFE-GO conditions build valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_safe_go_conditions()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(SAFE_GO_CONDITIONS)
    assert summary["total_safe_go"] == len(SAFE_GO_CONDITIONS)
    assert summary["all_permitted"] is True
    assert (df["type"] == "SAFE-GO").all()
    assert (df["permitted"] == True).all()


def test_combined_safety_boundary_structure():
    """Verify unified safety boundary table and summary."""
    df, summary = build_portfolio_acceptance_safety_boundary()

    assert isinstance(df, pd.DataFrame)
    total_conditions = len(NO_GO_CONDITIONS) + len(SAFE_GO_CONDITIONS)
    assert len(df) == total_conditions

    assert isinstance(summary, dict)
    assert summary["domain"] == SAFETY_DOMAIN
    assert summary["total_rules"] == total_conditions
    assert summary["no_go_count"] == len(NO_GO_CONDITIONS)
    assert summary["safe_go_count"] == len(SAFE_GO_CONDITIONS)
    assert summary["safety_status"] == "SAFETY_BOUNDARY_ENFORCED"
    assert summary["live_trading_prohibited"] is True
    assert summary["broker_execution_prohibited"] is True
    assert summary["portfolio_execution_prohibited"] is True
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY
