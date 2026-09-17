# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Non-Production Boundaries."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_non_production_boundaries import (
    NON_PROD_INVARIANTS,
    build_portfolio_acceptance_non_production_boundary_registry,
    summarize_portfolio_acceptance_non_production_boundaries,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    NON_PRODUCTION_BOUNDARY_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_non_production_boundaries_structure():
    """Verify non-production boundary registry builds valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_non_production_boundary_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(NON_PROD_INVARIANTS)

    expected_cols = {
        "invariant_id",
        "invariant_name",
        "enforced",
        "notes",
        "current_phase",
        "status",
    }
    assert expected_cols.issubset(df.columns)
    assert all(df["enforced"])
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)

    assert isinstance(summary, dict)
    assert summary["domain"] == NON_PRODUCTION_BOUNDARY_DOMAIN
    assert summary["total_invariants"] == len(NON_PROD_INVARIANTS)
    assert summary["all_enforced"] is True
    assert summary["production_ready_prohibited"] is True
    assert summary["broker_ready_prohibited"] is True
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_non_production_boundaries_empty():
    """Verify summary with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_non_production_boundaries(empty_df)
    assert summary["total_invariants"] == 0
    assert summary["all_enforced"] is False
