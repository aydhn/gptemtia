# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Transaction Cost Components."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.transaction_cost_components import (
    build_transaction_cost_component_registry,
)


def test_build_transaction_cost_components():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_transaction_cost_component_registry(prof)
    assert not df.empty
    assert len(df) >= 8
    assert summary["total_components"] >= 8
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
