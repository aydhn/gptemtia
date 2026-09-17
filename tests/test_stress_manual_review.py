# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Manual Review Queue."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_manual_review import (
    build_stress_manual_review_queue,
)


def test_manual_review_queue():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_manual_review_queue(prof)
    assert not df.empty
    assert summary["total_review_items"] == len(df)
    assert summary["all_destructive_actions_blocked"] is True
    assert summary["non_signal"] is True
