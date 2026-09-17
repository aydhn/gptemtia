# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: PnL Accounting Contracts."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.pnl_accounting_contracts import (
    build_pnl_accounting_contract_registry,
)


def test_build_pnl_accounting_contracts():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_pnl_accounting_contract_registry(prof)
    assert not df.empty
    assert len(df) == 2
    assert summary["total_pnl_contracts"] == 2
    assert summary["zero_real_pnl_calculated"] is True
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
