# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Manual Review Gates."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_manual_review_gates import (
    GATES,
    build_portfolio_acceptance_manual_review_gate_registry,
    summarize_portfolio_acceptance_manual_review_gates,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    MANUAL_REVIEW_GATE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_MANUAL_REVIEW_REQUIRED,
)


def test_manual_review_gates_structure():
    """Verify manual review gates registry builds valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_manual_review_gate_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(GATES)

    expected_cols = {
        "gate_id",
        "gate_name",
        "phase_ref",
        "title",
        "description",
        "action_required",
        "status",
        "current_phase",
    }
    assert expected_cols.issubset(df.columns)
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_MANUAL_REVIEW_REQUIRED)

    assert isinstance(summary, dict)
    assert summary["domain"] == MANUAL_REVIEW_GATE_DOMAIN
    assert summary["total_gates"] == len(GATES)
    assert summary["pending_review_count"] == len(GATES)
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_MANUAL_REVIEW_REQUIRED


def test_manual_review_gates_empty():
    """Verify summary with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_manual_review_gates(empty_df)
    assert summary["total_gates"] == 0
    assert summary["pending_review_count"] == 0
