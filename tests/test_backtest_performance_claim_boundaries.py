# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Performance Claim Boundaries."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_performance_claim_boundaries import (
    build_backtest_performance_claim_boundary_registry,
    validate_performance_claim_request,
    summarize_backtest_performance_claim_boundaries,
)


def test_build_backtest_performance_claim_boundaries():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_performance_claim_boundary_registry(profile)

    assert not df.empty
    assert len(df) == 6
    assert "target_claim" in df.columns
    assert (df["is_blocked"] == True).all()
    assert (df["approval_allowed"] == False).all()
    assert summary["all_claims_blocked"] is True


def test_validate_performance_claim_request():
    blocked_req = validate_performance_claim_request("strategy approved for production deployment")
    assert blocked_req["is_allowed"] is False
    assert blocked_req["is_blocked"] is True
    assert "strategy approved" in blocked_req["violating_tokens"]

    allowed_req = validate_performance_claim_request("pure contract metadata check")
    assert allowed_req["is_allowed"] is True
    assert allowed_req["is_blocked"] is False
