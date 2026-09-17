# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Safety Boundary."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_safety_boundary import (
    build_stress_testing_safety_boundary,
    build_stress_testing_no_go_conditions,
    build_stress_testing_safe_go_conditions,
)


def test_safety_boundary():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_testing_safety_boundary(prof)
    assert not df.empty
    assert summary["safety_status"] == "SECURE"
    assert summary["live_trading_prohibited"] is True
    assert summary["broker_execution_prohibited"] is True
    assert summary["non_signal"] is True

    no_go_df, _ = build_stress_testing_no_go_conditions(prof)
    assert len(no_go_df) >= 10
    safe_go_df, _ = build_stress_testing_safe_go_conditions(prof)
    assert len(safe_go_df) >= 5

