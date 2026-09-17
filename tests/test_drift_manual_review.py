# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Manual Review Workflows."""

import pytest
from advanced_model_drift_monitoring.drift_manual_review import (
    build_drift_manual_review_items,
    summarize_drift_manual_reviews,
)


def test_drift_manual_reviews():
    items = build_drift_manual_review_items()
    assert len(items) == 3
    summary = summarize_drift_manual_reviews(items)
    assert summary["total_reviews"] == 3
    assert summary["pending_count"] == 3
    assert summary["all_approved"] is False
