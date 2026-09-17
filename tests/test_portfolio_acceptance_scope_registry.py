# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Scope Registry."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_scope_registry import (
    SCOPE_ITEMS,
    build_portfolio_acceptance_scope_registry,
    summarize_portfolio_acceptance_scope,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    PORTFOLIO_ACCEPTANCE_SCOPE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_scope_registry_structure():
    """Verify scope registry builds valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_scope_registry()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert len(df) == len(SCOPE_ITEMS)

    expected_cols = {"scope_id", "description", "in_scope", "notes", "current_phase", "status"}
    assert expected_cols.issubset(df.columns)

    assert isinstance(summary, dict)
    assert summary["domain"] == PORTFOLIO_ACCEPTANCE_SCOPE_DOMAIN
    assert summary["total_scope_items"] == len(SCOPE_ITEMS)
    assert summary["in_scope_count"] > 0
    assert summary["out_of_scope_count"] > 0
    assert summary["live_trading_excluded"] is True
    assert summary["portfolio_execution_excluded"] is True


def test_scope_registry_explicit_profile():
    """Verify custom profile propagation."""
    profile = get_portfolio_acceptance_profile()
    df, summary = build_portfolio_acceptance_scope_registry(profile)

    assert (df["current_phase"] == profile.current_phase).all()
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)


def test_summarize_empty_df():
    """Verify summarizing empty df behaves gracefully."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_scope(empty_df)
    assert summary["total_scope_items"] == 0
    assert summary["in_scope_count"] == 0
    assert summary["out_of_scope_count"] == 0
