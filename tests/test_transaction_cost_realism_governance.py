# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Transaction Cost Realism Governance."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.transaction_cost_realism_governance import (
    build_transaction_cost_realism_governance_registry,
    COST_REALISM_RULES,
)


def test_build_transaction_cost_realism_governance():
    profile = get_default_backtest_governance_profile()
    df, summary = build_transaction_cost_realism_governance_registry(profile)

    assert not df.empty
    assert len(df) == 4
    assert "rule_id" in df.columns
    assert "rule_name" in df.columns
    assert (df["zero_cost_allowed"] == False).all()
    assert (df["broker_execution_allowed"] == False).all()
    assert (df["status"] == "ENFORCED").all()
    assert summary["total_rules"] == 4
    assert len(COST_REALISM_RULES) == 4
