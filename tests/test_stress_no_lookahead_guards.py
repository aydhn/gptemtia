# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: No-Lookahead Guards."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_no_lookahead_guards import (
    build_stress_no_lookahead_guard_registry,
    validate_stress_no_lookahead_columns,
)


def test_no_lookahead_guards():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_no_lookahead_guard_registry(prof)
    assert not df.empty
    assert summary["guard_active"] is True
    assert summary["non_signal"] is True

    res = validate_stress_no_lookahead_columns(["timestamp_utc", "close"])
    assert res["is_safe"] is True
