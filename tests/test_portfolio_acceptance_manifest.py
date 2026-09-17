# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Master Manifest."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    MANIFEST_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)
from advanced_portfolio_acceptance.portfolio_acceptance_manifest import (
    build_portfolio_acceptance_manifest,
    summarize_portfolio_acceptance_manifest,
)


def test_manifest_structure():
    """Verify master manifest structure and non-production invariants."""
    df, summary = build_portfolio_acceptance_manifest()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1

    row = df.iloc[0]
    assert int(row["current_phase"]) == 157
    assert int(row["target_final_phase"]) == 160
    assert int(row["next_phase"]) == 158
    assert bool(row["portfolio_block_completed"]) is True
    assert row["status"] == PORTFOLIO_ACCEPTANCE_READY

    # Strict negative invariants
    assert bool(row["non_production"]) is True
    assert bool(row["research_only"]) is True
    assert bool(row["dry_run"]) is True
    assert bool(row["production_ready"]) is False
    assert bool(row["broker_ready"]) is False
    assert bool(row["live_trading_ready"]) is False
    assert bool(row["portfolio_constructed"]) is False
    assert bool(row["position_sizing_generated"]) is False
    assert bool(row["portfolio_optimized"]) is False
    assert bool(row["capital_allocation_generated"]) is False
    assert bool(row["rebalance_generated"]) is False
    assert bool(row["orders_generated"]) is False
    assert bool(row["risk_report_generated"]) is False
    assert bool(row["scenario_executed"]) is False
    assert bool(row["drawdown_control_executed"]) is False
    assert bool(row["broker_order_sent"]) is False
    assert bool(row["model_deployed"]) is False
    assert bool(row["phase_158_handoff_ready"]) is True

    assert isinstance(summary, dict)
    assert summary["domain"] == MANIFEST_DOMAIN
    assert summary["current_phase"] == 157
    assert summary["next_phase"] == 158
    assert summary["portfolio_block_completed"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_manifest_empty():
    """Verify summarize with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_manifest(empty_df)
    assert summary["current_phase"] == 157
    assert summary["production_ready"] is False
