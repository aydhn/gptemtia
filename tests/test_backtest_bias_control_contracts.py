# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Bias Control Contracts."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_bias_control_contracts import (
    build_backtest_bias_control_contract_registry,
    summarize_backtest_bias_control_contracts,
    BIAS_CONTROLS,
)


def test_build_backtest_bias_control_contracts():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_bias_control_contract_registry(profile)

    assert not df.empty
    assert len(df) == 11
    assert "bias_type" in df.columns
    assert (df["claim_blocked"] == True).all()
    assert (df["execution_allowed"] == False).all()
    assert (df["lookahead_free_verified"] == True).all()
    assert summary["all_claims_blocked"] is True
    assert summary["all_executions_disabled"] is True
    assert len(BIAS_CONTROLS) == 11
