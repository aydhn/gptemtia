"""Test suite for Phase 137 ML Dataset Manual Review Queue."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_manual_review import (
    build_ml_dataset_manual_review_queue,
    summarize_ml_dataset_manual_review_queue,
)


def test_build_manual_review_queue():
    df, summary = build_ml_dataset_manual_review_queue()
    assert not df.empty
    assert summary["total_review_items"] >= 8
    assert summary["auto_fix_allowed"] is False
    assert summary["auto_materialize_allowed"] is False
    assert summary["auto_train_allowed"] is False
