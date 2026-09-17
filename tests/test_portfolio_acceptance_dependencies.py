# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Dependency Registry."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_dependencies import (
    DEPENDENCY_SOURCES,
    build_portfolio_acceptance_dependency_registry,
    summarize_portfolio_acceptance_dependencies,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    DEPENDENCY_ACCEPTANCE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_portfolio_acceptance_dependencies_structure():
    """Verify dependency registry builds valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_dependency_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(DEPENDENCY_SOURCES)

    expected_cols = {
        "dep_id",
        "source_phase",
        "source_module",
        "description",
        "satisfied",
        "current_phase",
        "status",
    }
    assert expected_cols.issubset(df.columns)
    assert all(df["satisfied"])
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)

    assert isinstance(summary, dict)
    assert summary["domain"] == DEPENDENCY_ACCEPTANCE_DOMAIN
    assert summary["total_dependencies"] == len(DEPENDENCY_SOURCES)
    assert summary["satisfied_dependencies"] == len(DEPENDENCY_SOURCES)
    assert summary["all_satisfied"] is True
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_portfolio_acceptance_dependencies_empty():
    """Verify summary with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_dependencies(empty_df)
    assert summary["total_dependencies"] == 0
    assert summary["all_satisfied"] is False
