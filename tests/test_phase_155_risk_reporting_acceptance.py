# -*- coding: utf-8 -*-
"""Tests for Phase 157: Phase 155 Risk Reporting Acceptance Registry."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.phase_155_risk_reporting_acceptance import (
    PHASE_155_ITEMS,
    build_phase_155_risk_reporting_acceptance_registry,
    summarize_phase_155_risk_reporting_acceptance,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    PHASE_155_RISK_REPORTING_ACCEPTANCE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_phase_155_acceptance_structure():
    """Verify Phase 155 acceptance evaluation registry."""
    df, summary = build_phase_155_risk_reporting_acceptance_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(PHASE_155_ITEMS)
    assert len(df) == 10

    expected_cols = {
        "item_id",
        "phase_number",
        "phase_title",
        "criterion",
        "description",
        "satisfied",
        "contract_only",
        "non_production",
        "dry_run",
        "current_phase",
        "status",
    }
    assert expected_cols.issubset(df.columns)
    assert all(df["satisfied"])
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)

    assert isinstance(summary, dict)
    assert summary["domain"] == PHASE_155_RISK_REPORTING_ACCEPTANCE_DOMAIN
    assert summary["phase_number"] == 155
    assert summary["total_criteria"] == 10
    assert summary["all_satisfied"] is True
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_phase_155_acceptance_empty():
    """Verify summary with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_phase_155_risk_reporting_acceptance(empty_df)
    assert summary["total_criteria"] == 0
    assert summary["all_satisfied"] is False
