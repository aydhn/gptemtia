# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Gap Registry."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_gaps import (
    KNOWN_GAP_TYPES,
    build_portfolio_acceptance_gap_registry,
    summarize_portfolio_acceptance_gaps,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    GAP_DOMAIN,
    SEVERITY_WARNING,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_gap_registry_structure():
    """Verify gap registry builds valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_gap_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(KNOWN_GAP_TYPES)

    expected_cols = {
        "gap_type",
        "description",
        "severity_label",
        "is_open",
        "current_phase",
        "status",
    }
    assert expected_cols.issubset(df.columns)

    # In clean default state, zero open gaps
    assert not any(df["is_open"])
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)

    assert isinstance(summary, dict)
    assert summary["domain"] == GAP_DOMAIN
    assert summary["total_monitored_gap_types"] == len(KNOWN_GAP_TYPES)
    assert summary["open_gaps_count"] == 0
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_gap_empty():
    """Verify summarize with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_gaps(empty_df)
    assert summary["total_monitored_gap_types"] == 0
    assert summary["open_gaps_count"] == 0
