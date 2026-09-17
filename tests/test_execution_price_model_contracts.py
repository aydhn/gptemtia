# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Execution Price Model Contracts."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.execution_price_model_contracts import (
    build_execution_price_model_contract_registry,
)


def test_build_execution_price_model_contracts():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_execution_price_model_contract_registry(prof)
    assert not df.empty
    assert len(df) >= 3
    assert summary["total_price_models"] >= 3
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
