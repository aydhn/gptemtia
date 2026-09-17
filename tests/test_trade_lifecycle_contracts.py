# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Trade Lifecycle Contracts."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.trade_lifecycle_contracts import (
    build_trade_lifecycle_contract_registry,
)


def test_build_trade_lifecycle_contracts():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_trade_lifecycle_contract_registry(prof)
    assert not df.empty
    assert len(df) >= 7
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
