"""Test suite for Phase 139 GPU Training Manual Review Queue."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_manual_review import (
    build_gpu_training_manual_review_queue,
    summarize_gpu_training_manual_review_queue,
)


def test_build_gpu_training_manual_review_queue():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_manual_review_queue(profile)

    assert len(df) == 8
    assert summary["total_review_items"] == 8
    assert summary["all_non_destructive"] is True
    assert summary["high_priority_count"] >= 4
    assert summary["non_signal"] is True


def test_summarize_gpu_training_manual_review_queue():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_gpu_training_manual_review_queue(profile)
    summary = summarize_gpu_training_manual_review_queue(df)

    assert summary["total_review_items"] == 8
    assert summary["all_non_destructive"] is True
    assert summary["non_signal"] is True
