# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Manual Review Queue."""

from advanced_ensemble_model_registry.ensemble_manual_review import (
    build_ensemble_manual_review_queue,
    validate_ensemble_manual_review_queue,
    summarize_ensemble_manual_review_queue,
)


def test_ensemble_manual_review_queue():
    queue = build_ensemble_manual_review_queue()
    assert len(queue) == 3
    assert validate_ensemble_manual_review_queue(queue) is True

    summary = summarize_ensemble_manual_review_queue(queue)
    assert summary["total_items"] == 3
    assert summary["all_auto_fix_blocked"] is True
    assert summary["all_destructive_blocked"] is True
    assert summary["all_non_signal"] is True
