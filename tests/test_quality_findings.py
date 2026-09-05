import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.quality_findings import (
    create_quality_finding,
    build_quality_finding_registry,
    summarize_quality_findings,
)


def test_quality_findings():
    profile = get_default_data_quality_profile()
    f = create_quality_finding(
        rule_id="rule_test",
        finding_type="finding_schema_mismatch",
        dataset_type="dataset_fx_quote",
        provider_name="prov_x",
        field_name="bid",
        severity_label="quality_high",
        message="Test message",
    )
    assert f.finding_id.startswith("find_rule_test_")
    assert f.manual_review_required is True

    df, summary = build_quality_finding_registry([f], profile)
    assert len(df) == 1
    assert summary["total_findings"] == 1
    assert summary["high_count"] == 1
