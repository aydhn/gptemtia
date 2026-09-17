# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Component Checkpoints."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_component_checkpoints import (
    CHECKPOINTS,
    build_portfolio_acceptance_component_checkpoint_registry,
    validate_portfolio_acceptance_component_checkpoint,
    summarize_portfolio_acceptance_component_checkpoints,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    COMPONENT_CHECKPOINT_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_component_checkpoints_structure():
    """Verify component checkpoints evaluate all checkpoints correctly."""
    df, summary = build_portfolio_acceptance_component_checkpoint_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(CHECKPOINTS)
    assert len(df) == 5  # Phases 153 to 157

    expected_cols = {
        "checkpoint_id",
        "component_name",
        "expected_module",
        "contract_only",
        "non_production",
        "manual_review_required",
        "production_ready",
        "broker_ready",
        "live_ready",
        "signal_ready",
        "strategy_approved",
        "portfolio_approved",
        "status",
    }
    assert expected_cols.issubset(df.columns)

    # Invariants
    assert all(df["contract_only"])
    assert all(df["non_production"])
    assert all(df["manual_review_required"])
    assert not any(df["production_ready"])
    assert not any(df["broker_ready"])
    assert not any(df["live_ready"])
    assert not any(df["portfolio_approved"])
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)

    assert isinstance(summary, dict)
    assert summary["domain"] == COMPONENT_CHECKPOINT_DOMAIN
    assert summary["total_checkpoints"] == 5
    assert summary["all_contract_only"] is True
    assert summary["all_non_production"] is True
    assert summary["none_production_ready"] is True
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_validate_component_checkpoint():
    """Verify individual checkpoint validation."""
    valid_chk = {
        "checkpoint_id": "CHK-TEST",
        "component_name": "test_component",
        "contract_only": True,
        "non_production": True,
        "production_ready": False,
        "broker_ready": False,
        "live_ready": False,
        "signal_ready": False,
        "portfolio_approved": False,
    }
    res = validate_portfolio_acceptance_component_checkpoint(valid_chk)
    assert res["is_valid"] is True
    assert res["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_component_checkpoints_summary_empty():
    """Verify summarizing empty df."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_component_checkpoints(empty_df)
    assert summary["total_checkpoints"] == 0
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY
