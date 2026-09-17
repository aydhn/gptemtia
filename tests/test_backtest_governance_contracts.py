# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Governance Contracts."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_contracts import (
    build_backtest_governance_contract_registry,
    summarize_backtest_governance_contracts,
    CONTRACT_DEFINITIONS,
)


def test_build_backtest_governance_contracts():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_governance_contract_registry(profile)

    assert not df.empty
    assert len(df) == 7
    assert "contract_name" in df.columns
    assert (df["backtest_execution_allowed"] == False).all()
    assert (df["benchmark_execution_allowed"] == False).all()
    assert (df["metric_calculation_allowed"] == False).all()
    assert (df["result_claim_allowed"] == False).all()
    assert (df["performance_claim_allowed"] == False).all()
    assert (df["live_trading_allowed"] == False).all()
    assert (df["non_signal"] == True).all()

    assert summary["all_executions_blocked"] is True
    assert summary["all_contracts_valid"] is True
    assert len(CONTRACT_DEFINITIONS) == 7
