# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Transaction Cost Models."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.transaction_cost_models import (
    build_transaction_cost_model_registry,
)


def test_build_transaction_cost_models():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_transaction_cost_model_registry(prof)
    assert not df.empty
    assert len(df) == 3
    assert summary["total_cost_models"] == 3
    assert summary["non_signal"] is True
    assert (df["real_cost_calculated"] == False).all()
    assert (df["non_signal"] == True).all()
