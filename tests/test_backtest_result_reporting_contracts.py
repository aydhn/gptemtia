# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Result Reporting Contracts."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_result_reporting_contracts import (
    build_backtest_result_reporting_contract_registry,
    summarize_backtest_result_reporting_contracts,
    REPORTING_CONTRACTS,
)


def test_build_backtest_result_reporting_contracts():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_result_reporting_contract_registry(profile)

    assert not df.empty
    assert len(df) >= 5
    assert "contract_name" in df.columns
    assert (df["non_signal"] == True).all()
    assert (df["result_claim_allowed"] == False).all()
    assert (df["performance_claim_allowed"] == False).all()
    assert summary["all_claims_blocked"] is True
    assert len(REPORTING_CONTRACTS) >= 5
