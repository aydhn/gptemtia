# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Warning Registry."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_warnings import (
    WARNING_ITEMS,
    build_portfolio_acceptance_warning_registry,
    summarize_portfolio_acceptance_warnings,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    WARNING_DOMAIN,
    SEVERITY_WARNING,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_warning_registry_structure():
    """Verify warning registry builds valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_warning_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(WARNING_ITEMS)

    expected_cols = {
        "warning_type",
        "message",
        "severity_label",
        "is_acknowledged",
        "current_phase",
        "status",
    }
    assert expected_cols.issubset(df.columns)
    assert all(df["is_acknowledged"])
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)

    assert isinstance(summary, dict)
    assert summary["domain"] == WARNING_DOMAIN
    assert summary["total_warnings"] == len(WARNING_ITEMS)
    assert summary["all_acknowledged"] is True
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_warning_empty():
    """Verify summarize with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_warnings(empty_df)
    assert summary["total_warnings"] == 0
    assert summary["all_acknowledged"] is False
