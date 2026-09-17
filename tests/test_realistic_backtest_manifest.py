# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Backtest Manifest."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.realistic_backtest_manifest import (
    build_realistic_backtest_manifest,
)


def test_build_realistic_backtest_manifest():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_realistic_backtest_manifest(prof)
    assert not df.empty
    assert summary["current_phase"] == 146
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 147
    assert summary["all_invariants_valid"] is True
    assert summary["phase_147_handoff_ready"] is True
    assert summary["non_signal"] is True

    # Check negative invariants in df
    val_map = dict(zip(df["property"], df["value"]))
    assert val_map["backtest_executed"] is False
    assert val_map["broker_order_sent"] is False
    assert val_map["live_order_sent"] is False
    assert val_map["production_ready"] is False
    assert val_map["broker_ready"] is False
