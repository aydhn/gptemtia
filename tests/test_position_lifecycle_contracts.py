# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Position Lifecycle Contracts."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.position_lifecycle_contracts import (
    build_position_lifecycle_contract_registry,
)


def test_build_position_lifecycle_contracts():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_position_lifecycle_contract_registry(prof)
    assert not df.empty
    assert len(df) >= 6
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
