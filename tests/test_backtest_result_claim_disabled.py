# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Result Claim Disabled."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_result_claim_disabled import (
    build_backtest_result_claim_disabled_report,
    validate_no_result_claim_request,
)


def test_build_backtest_result_claim_disabled():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_result_claim_disabled_report(profile)

    assert not df.empty
    assert len(df) == 4
    assert (df["claim_permitted"] == False).all()
    assert summary["all_claims_disabled"] is True
    assert summary["total_disabled_claims"] == 4


def test_validate_no_result_claim_request():
    blocked = validate_no_result_claim_request("performance_claim on out-of-sample test")
    assert blocked["is_allowed"] is False
    assert blocked["is_blocked"] is True

    allowed = validate_no_result_claim_request("review contract boundary definitions")
    assert allowed["is_allowed"] is True
    assert allowed["is_blocked"] is False
