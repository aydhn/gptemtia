# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift No-Lookahead Guards."""

import pytest
from advanced_model_drift_monitoring.drift_no_lookahead_guards import (
    build_drift_no_lookahead_guards,
    validate_window_temporal_ordering,
)


def test_no_lookahead_guards():
    guards = build_drift_no_lookahead_guards()
    assert len(guards) == 2
    for g in guards:
        assert g.is_active is True


def test_window_temporal_ordering():
    # Valid causal order
    res_valid = validate_window_temporal_ordering("2024-01-01", "2024-01-02")
    assert res_valid["valid"] is True

    # Same timestamp allowed
    res_same = validate_window_temporal_ordering("2024-01-01", "2024-01-01")
    assert res_same["valid"] is True

    # Forward violation
    res_invalid = validate_window_temporal_ordering("2024-01-05", "2024-01-01")
    assert res_invalid["valid"] is False
