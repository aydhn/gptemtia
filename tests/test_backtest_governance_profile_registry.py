# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Governance Profile Registry."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_profile_registry import (
    build_backtest_governance_profile_registry,
    summarize_backtest_governance_profiles,
)


def test_build_backtest_governance_profile_registry():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_governance_profile_registry(profile)

    assert not df.empty
    assert len(df) >= 3
    assert "profile_name" in df.columns
    assert (df["current_phase"] == 150).all()
    assert (df["target_final_phase"] == 160).all()
    assert (df["local_only"] == True).all()
    assert (df["non_signal"] == True).all()
    assert (df["allow_live_trading"] == False).all()
    assert (df["allow_backtest_execution"] == False).all()

    assert summary["all_local_only"] is True
    assert summary["all_executions_disabled"] is True
    assert summary["all_live_trading_disabled"] is True
    assert summary["non_signal"] is True
    assert summary["total_profiles"] >= 3
