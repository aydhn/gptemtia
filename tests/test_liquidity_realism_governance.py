# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Liquidity Realism Governance."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.liquidity_realism_governance import (
    build_liquidity_realism_governance_registry,
    LIQUIDITY_REALISM_RULES,
)


def test_build_liquidity_realism_governance():
    profile = get_default_backtest_governance_profile()
    df, summary = build_liquidity_realism_governance_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "rule_id" in df.columns
    assert "rule_name" in df.columns
    assert (df["perfect_liquidity_allowed"] == False).all()
    assert (df["broker_execution_allowed"] == False).all()
    assert (df["status"] == "ENFORCED").all()
    assert summary["total_rules"] == 3
    assert len(LIQUIDITY_REALISM_RULES) == 3
