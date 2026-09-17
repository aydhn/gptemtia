# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Metric Claim Boundaries."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_metric_claim_boundaries import (
    build_backtest_metric_claim_boundary_registry,
    validate_metric_claim_request,
    summarize_backtest_metric_claim_boundaries,
)


def test_build_backtest_metric_claim_boundaries():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_metric_claim_boundary_registry(profile)

    assert not df.empty
    assert len(df) == 6
    assert "target_metric" in df.columns
    assert (df["is_blocked"] == True).all()
    assert (df["non_signal"] == True).all()
    assert summary["all_metrics_blocked"] is True
    assert summary["all_calculations_disabled"] is True
    assert summary["total_boundaries"] == 6


def test_validate_metric_claim_request():
    blocked_req = validate_metric_claim_request("calculate_sharpe for strategy A")
    assert blocked_req["is_allowed"] is False
    assert blocked_req["is_blocked"] is True
    assert "calculate_sharpe" in blocked_req["violating_tokens"]

    allowed_req = validate_metric_claim_request("review contract placeholder definitions")
    assert allowed_req["is_allowed"] is True
    assert allowed_req["is_blocked"] is False
