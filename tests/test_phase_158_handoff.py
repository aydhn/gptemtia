# -*- coding: utf-8 -*-
"""Tests for Phase 157: Phase 158 Full-System Integration and Advanced Acceptance Rehearsal Handoff."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    PHASE_158_HANDOFF_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)
from advanced_portfolio_acceptance.phase_158_handoff import (
    HANDOFF_PREREQUISITES,
    build_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report,
    summarize_phase_158_handoff,
)


def test_phase_158_handoff_structure():
    """Verify Phase 158 handoff report DataFrame and summary."""
    df, summary = build_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(HANDOFF_PREREQUISITES)

    expected_cols = {
        "item_id",
        "topic",
        "description",
        "satisfied",
        "current_phase",
        "target_final_phase",
        "next_phase",
        "status",
        "non_signal",
        "non_production",
        "local_only",
    }
    assert expected_cols.issubset(df.columns)
    assert all(df["satisfied"])
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)

    # Invariant checks
    assert (df["current_phase"] == 157).all()
    assert (df["target_final_phase"] == 160).all()
    assert (df["next_phase"] == 158).all()
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()

    assert isinstance(summary, dict)
    assert summary["domain"] == PHASE_158_HANDOFF_DOMAIN
    assert summary["current_phase"] == 157
    assert summary["next_phase"] == 158
    assert summary["target_final_phase"] == 160
    assert summary["total_prerequisites"] == len(HANDOFF_PREREQUISITES)
    assert summary["all_satisfied"] is True
    assert summary["handoff_ready"] is True
    assert summary["status"] == "ACCEPTED"


def test_phase_158_handoff_empty():
    """Verify summarize with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_phase_158_handoff(empty_df)
    assert summary["prerequisite_count"] == 0
    assert summary["all_satisfied"] is False
    assert summary["handoff_ready"] is True
