# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Rejected Order Placeholders."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.rejected_order_placeholders import (
    build_rejected_order_placeholder_registry,
)


def test_build_rejected_order_placeholders():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_rejected_order_placeholder_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
