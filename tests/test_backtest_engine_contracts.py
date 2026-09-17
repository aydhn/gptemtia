# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Engine Contracts."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_engine_contracts import (
    build_backtest_engine_contract_registry,
)


def test_build_backtest_engine_contracts():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_engine_contract_registry(prof)
    assert not df.empty
    assert len(df) == 6
    assert summary["total_contracts"] == 6
    assert summary["all_execution_blocked"] is True
    assert summary["all_live_trading_blocked"] is True
    assert summary["all_broker_blocked"] is True
    assert summary["non_signal"] is True
    assert (df["backtest_execution_allowed"] == False).all()
    assert (df["live_trading_allowed"] == False).all()
    assert (df["broker_execution_allowed"] == False).all()
