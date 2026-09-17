# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Slippage Model Contracts."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.slippage_model_contracts import (
    build_slippage_model_contract_registry,
)


def test_build_slippage_models():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_slippage_model_contract_registry(prof)
    assert not df.empty
    assert len(df) == 6
    assert summary["total_slippage_models"] == 6
    assert summary["non_signal"] is True
    assert (df["real_slippage_calculated"] == False).all()
    assert (df["performance_guaranteed"] == False).all()
    assert (df["non_signal"] == True).all()
