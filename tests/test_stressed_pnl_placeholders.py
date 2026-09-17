# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Stressed PnL Placeholders."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stressed_pnl_placeholders import (
    build_stressed_pnl_placeholder_registry,
)


def test_stressed_pnl_placeholders():
    prof = get_default_stress_testing_profile()
    df, summary = build_stressed_pnl_placeholder_registry(prof)
    assert not df.empty
    assert summary["all_calculation_blocked"] is True
    assert summary["non_signal"] is True
