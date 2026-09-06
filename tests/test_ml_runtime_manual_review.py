"""Test suite for Phase 136 ML Runtime Manual Review Queue."""

import pytest
from advanced_gpu_ml_runtime.ml_runtime_manual_review import (
    build_ml_runtime_manual_review_queue,
)


def test_build_ml_runtime_manual_review_queue():
    df, summary = build_ml_runtime_manual_review_queue()
    assert isinstance(summary["total_review_items"], int)
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
