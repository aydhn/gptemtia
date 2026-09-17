# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Event Driven Backtest Contracts."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.event_driven_backtest_contracts import (
    build_event_driven_backtest_contract_registry,
)


def test_build_event_driven_contracts():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_event_driven_backtest_contract_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
