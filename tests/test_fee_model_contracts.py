# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Fee Model Contracts."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.fee_model_contracts import (
    build_fee_model_contract_registry,
)


def test_build_fee_models():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_fee_model_contract_registry(prof)
    assert not df.empty
    assert len(df) >= 2
    assert summary["total_fee_models"] >= 2
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
