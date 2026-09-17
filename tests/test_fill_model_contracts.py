# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Fill Model Contracts."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.fill_model_contracts import (
    build_fill_model_contract_registry,
)


def test_build_fill_model_contracts():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_fill_model_contract_registry(prof)
    assert not df.empty
    assert len(df) >= 4
    assert summary["total_fill_models"] >= 4
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
