# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Readiness Scoring."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    READINESS_SCORE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)
from advanced_portfolio_acceptance.portfolio_acceptance_readiness_scoring import (
    classify_portfolio_acceptance_readiness_score,
    calculate_portfolio_acceptance_readiness_score,
    build_portfolio_acceptance_readiness_score_report,
)
from advanced_portfolio_acceptance.portfolio_acceptance_findings import (
    create_portfolio_acceptance_finding,
)


def test_classify_scores():
    """Verify readiness score classification categories."""
    assert classify_portfolio_acceptance_readiness_score(0.1) == "blocked"
    assert classify_portfolio_acceptance_readiness_score(0.4) == "incomplete"
    assert classify_portfolio_acceptance_readiness_score(0.65) == "contract_ready_with_manual_review"
    assert classify_portfolio_acceptance_readiness_score(0.95) == "portfolio_acceptance_contract_ready_non_production"


def test_calculate_readiness_clean_findings():
    """Verify readiness calculation with default findings (no blockers)."""
    profile = get_portfolio_acceptance_profile()
    findings_df = pd.DataFrame([
        {"is_blocking": False, "severity_label": "WARNING"},
    ])
    score = calculate_portfolio_acceptance_readiness_score(findings_df, profile)

    assert score.overall_score > 0.8
    assert score.meets_threshold is True
    assert score.blocker_count == 0
    assert score.non_production is True
    assert score.production_ready is False
    assert score.live_trading_ready is False


def test_calculate_readiness_with_blocker():
    """Verify readiness calculation drops to 0 when blockers exist."""
    profile = get_portfolio_acceptance_profile()
    findings_df = pd.DataFrame([
        {"is_blocking": True, "severity_label": "CRITICAL"},
    ])
    score = calculate_portfolio_acceptance_readiness_score(findings_df, profile)

    assert score.overall_score == 0.0
    assert score.classification == "blocked"
    assert score.meets_threshold is False
    assert score.blocker_count == 1


def test_build_readiness_score_report():
    """Verify build_portfolio_acceptance_readiness_score_report structure."""
    df, summary = build_portfolio_acceptance_readiness_score_report()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert bool(df.iloc[0]["meets_threshold"]) is True
    assert bool(df.iloc[0]["production_ready"]) is False
    assert int(df.iloc[0]["current_phase"]) == 157

    assert isinstance(summary, dict)
    assert summary["domain"] == READINESS_SCORE_DOMAIN
    assert summary["meets_threshold"] is True
    assert summary["is_production_ready"] is False
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY
