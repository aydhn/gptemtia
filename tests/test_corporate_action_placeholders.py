# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Corporate Action Placeholders."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.corporate_action_placeholders import (
    build_corporate_action_placeholder_registry,
)


def test_build_corporate_action_placeholders():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_corporate_action_placeholder_registry(prof)
    assert not df.empty
    assert len(df) >= 2
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
