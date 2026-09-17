# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Forbidden Column Policies."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_forbidden_column_policies import (
    build_stress_forbidden_column_policy_registry,
    validate_stress_forbidden_columns,
)


def test_forbidden_column_policies():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_forbidden_column_policy_registry(prof)
    assert not df.empty
    assert summary["guard_active"] is True
    assert summary["total_forbidden_columns"] >= 30
    assert summary["non_signal"] is True

    res = validate_stress_forbidden_columns(["timestamp", "close"])
    assert res["is_safe"] is True

    res_viol = validate_stress_forbidden_columns(["buy", "stressed_pnl"])
    assert res_viol["is_safe"] is False
