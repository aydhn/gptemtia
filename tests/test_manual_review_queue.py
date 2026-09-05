import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.quality_findings import create_quality_finding
from advanced_data_quality.manual_review_queue import (
    build_manual_review_queue,
    create_manual_review_item,
    summarize_manual_review_queue,
)


def test_manual_review_queue():
    profile = get_default_data_quality_profile()
    f = create_quality_finding(
        rule_id="r1",
        finding_type="finding_stale_data",
        dataset_type="dataset_macro_timeseries",
        provider_name="p1",
        field_name="timestamp",
        severity_label="quality_medium",
        message="Stale data found",
    )
    item = create_manual_review_item(f)
    assert item.destructive_action_allowed is False
    assert "Phase 113" in item.suggested_action

    findings_df = pd.DataFrame([f.to_dict()])
    queue_df, summary = build_manual_review_queue(findings_df, profile)
    assert len(queue_df) == 1
    assert summary["destructive_action_allowed_any"] is False
