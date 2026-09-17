# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Partial Fill Placeholders."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.partial_fill_placeholders import (
    build_partial_fill_placeholder_registry,
)


def test_build_partial_fill_placeholders():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_partial_fill_placeholder_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
