# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Master Manifest."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_manifest import (
    build_benchmark_evaluation_manifest,
)


def test_manifest():
    profile = get_default_benchmark_evaluation_profile()
    df, s = build_benchmark_evaluation_manifest(profile)

    assert not df.empty
    assert len(df) >= 15
    assert "property" in df.columns
    assert "value" in df.columns

    prop_dict = dict(zip(df["property"], df["value"]))
    assert prop_dict["current_phase"] == 151
    assert prop_dict["next_phase"] == 152
    assert prop_dict["target_final_phase"] == 160
    assert prop_dict["live_trading_ready"] is False
    assert prop_dict["benchmark_report_executed"] is False
    assert s["non_signal"] is True
