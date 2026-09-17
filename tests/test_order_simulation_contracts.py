# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Order Simulation Contracts."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.order_simulation_contracts import (
    build_order_simulation_contract_registry,
)


def test_build_order_simulation_contracts():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_order_simulation_contract_registry(prof)
    assert not df.empty
    assert len(df) == 6
    assert summary["total_order_types"] == 6
    assert summary["non_signal"] is True
    assert (df["broker_order_sent"] == False).all()
    assert (df["live_order_sent"] == False).all()
    assert (df["non_signal"] == True).all()
