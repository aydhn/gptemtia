# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Portfolio Readiness Scoring."""

import pandas as pd
import pytest

from advanced_portfolio_construction.portfolio_construction_config import (
    get_default_portfolio_construction_profile,
)
from advanced_portfolio_construction.portfolio_readiness_scoring import (
    classify_portfolio_readiness_score,
    calculate_portfolio_readiness_score,
    build_portfolio_readiness_score_report,
)


def test_classify_portfolio_readiness_score():
    assert classify_portfolio_readiness_score(0.10) == "blocked"
    assert classify_portfolio_readiness_score(0.35) == "incomplete"
    assert classify_portfolio_readiness_score(0.60) == "contract_ready_with_manual_review"
    assert classify_portfolio_readiness_score(0.90) == "portfolio_construction_contract_ready_non_production"

    with pytest.raises(ValueError):
        classify_portfolio_readiness_score(1.5)


def test_calculate_portfolio_readiness_score_clean():
    profile = get_default_portfolio_construction_profile()
    score = calculate_portfolio_readiness_score(findings_df=None, profile=profile)
    assert score.overall_score == 1.0
    assert score.meets_threshold is True
    assert score.classification == "portfolio_construction_contract_ready_non_production"
    assert score.production_ready is False


def test_calculate_portfolio_readiness_score_with_critical():
    profile = get_default_portfolio_construction_profile()
    findings_df = pd.DataFrame([
        {"severity": "CRITICAL", "message": "Issue 1"},
        {"severity": "CRITICAL", "message": "Issue 2"},
    ])
    score = calculate_portfolio_readiness_score(findings_df=findings_df, profile=profile)
    assert score.overall_score == 0.20
    assert score.classification == "blocked"
    assert score.critical_count == 2


def test_build_portfolio_readiness_score_report():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_portfolio_readiness_score_report(profile=profile)
    assert len(df) == 1
    assert summary["overall_score"] == 1.0
    assert summary["meets_threshold"] is True
