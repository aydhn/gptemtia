import pytest
from advanced_feature_validation.feature_validation_manual_review_queue import (
    clear_manual_review_queue,
    add_to_manual_review_queue,
    get_manual_review_queue,
    get_manual_review_summary,
)


def test_feature_validation_manual_review_queue():
    clear_manual_review_queue()
    assert len(get_manual_review_queue()) == 0

    item = add_to_manual_review_queue(
        finding_id="FIND-101",
        column_name="questionable_metric",
        reason="Ambiguous naming format",
        recommended_action="Rename to explicit prefix",
    )
    assert item["finding_id"] == "FIND-101"
    assert len(get_manual_review_queue()) == 1

    summary = get_manual_review_summary()
    assert summary["total_items"] == 1
    assert summary["pending_review"] == 1
