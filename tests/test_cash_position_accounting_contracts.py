# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Cash and Position Accounting Contracts."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.cash_position_accounting_contracts import (
    build_cash_position_accounting_contract_registry,
)


def test_build_cash_position_accounting_contracts():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_cash_position_accounting_contract_registry(prof)
    assert not df.empty
    assert len(df) == 3
    assert summary["total_ledger_components"] == 3
    assert summary["zero_real_money_involved"] is True
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
