# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Safety Boundary Registry."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_safety_boundary_registry import (
    SAFETY_RULES,
    build_portfolio_acceptance_safety_boundary_registry,
    summarize_portfolio_acceptance_safety_boundaries,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    SAFETY_BOUNDARY_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_safety_boundary_registry_structure():
    """Verify safety boundary registry builds valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_safety_boundary_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(SAFETY_RULES)

    expected_cols = {
        "boundary_id",
        "rule_name",
        "description",
        "is_allowed",
        "notes",
        "current_phase",
        "status",
    }
    assert expected_cols.issubset(df.columns)
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)

    assert isinstance(summary, dict)
    assert summary["domain"] == SAFETY_BOUNDARY_DOMAIN
    assert summary["total_rules"] == len(SAFETY_RULES)
    assert summary["prohibited_actions_count"] > 0
    assert summary["allowed_actions_count"] > 0
    assert summary["all_prohibited_enforced"] is True
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_safety_boundary_empty():
    """Verify summary with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_safety_boundaries(empty_df)
    assert summary["total_rules"] == 0
    assert summary["all_prohibited_enforced"] is True
