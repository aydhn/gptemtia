import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.stale_data_rules import (
    build_stale_data_rule_set,
    check_stale_timestamp,
)


def test_stale_data_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_stale_data_rule_set(profile)
    assert len(df_rules) >= 1

    # Old date should trigger stale finding
    test_df = pd.DataFrame([{"timestamp": "2020-01-01T00:00:00Z"}])
    findings = check_stale_timestamp(test_df, "timestamp", max_age_days=30, dataset_type="test_ds", provider_name="test_p")
    assert len(findings) == 1
    assert findings[0].finding_type == "finding_stale_data"

from unittest import mock

def test_stale_data_rules_error_path():
    # Test that exception handling in check_stale_timestamp returns a finding of type finding_timestamp_issue
    test_df = pd.DataFrame([{"timestamp": "invalid_date"}])
    with mock.patch("advanced_data_quality.stale_data_rules.pd.to_datetime", side_effect=Exception("Mocked parsing error")):
        findings = check_stale_timestamp(test_df, "timestamp", max_age_days=30, dataset_type="test_ds", provider_name="test_p")

    assert len(findings) == 1
    assert findings[0].finding_type == "finding_timestamp_issue"
    assert "rule_stale_data_parse_err" in findings[0].finding_id
    assert "Mocked parsing error" in findings[0].message
