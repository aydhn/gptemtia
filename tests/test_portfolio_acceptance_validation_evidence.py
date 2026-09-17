# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Validation Evidence Registry."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_validation_evidence import (
    EVIDENCE_ITEMS,
    build_portfolio_acceptance_validation_evidence_registry,
    summarize_portfolio_acceptance_validation_evidence,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    VALIDATION_EVIDENCE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_validation_evidence_structure():
    """Verify validation evidence registry builds valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_validation_evidence_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(EVIDENCE_ITEMS)

    expected_cols = {
        "evidence_id",
        "phase_number",
        "evidence_type",
        "target_module",
        "description",
        "evidence_present",
        "current_phase",
        "status",
    }
    assert expected_cols.issubset(df.columns)
    assert all(df["evidence_present"])
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)

    assert isinstance(summary, dict)
    assert summary["domain"] == VALIDATION_EVIDENCE_DOMAIN
    assert summary["total_evidence_items"] == len(EVIDENCE_ITEMS)
    assert summary["present_evidence_items"] == len(EVIDENCE_ITEMS)
    assert summary["all_evidence_present"] is True
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_validation_evidence_empty():
    """Verify summary with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_validation_evidence(empty_df)
    assert summary["total_evidence_items"] == 0
    assert summary["all_evidence_present"] is False
