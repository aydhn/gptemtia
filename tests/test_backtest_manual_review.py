# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Manual Review Queue."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_manual_review import (
    build_backtest_manual_review_queue,
)


def test_build_manual_review_queue():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_manual_review_queue(prof)
    assert not df.empty
    assert len(df) == 8
    assert summary["zero_destructive_actions_allowed"] is True
    assert summary["human_review_required"] is True
    assert summary["non_signal"] is True
    assert (df["destructive_action_allowed"] == False).all()
