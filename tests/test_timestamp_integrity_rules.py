import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.timestamp_integrity_rules import (
    build_timestamp_integrity_rule_set,
    check_timestamp_parseability,
    check_timestamp_ordering,
)


def test_timestamp_integrity_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_timestamp_integrity_rule_set(profile)
    assert len(df_rules) >= 2

    # Unparseable timestamp
    test_df = pd.DataFrame([{"timestamp": "not_a_date"}])
    findings = check_timestamp_parseability(test_df, "timestamp", "test_ds", "test_p")
    assert len(findings) == 1
    assert findings[0].finding_type == "finding_timestamp_issue"

    # Non-monotonic ordering
    bad_order_df = pd.DataFrame([
        {"timestamp": "2026-09-02"},
        {"timestamp": "2026-09-01"},
    ])
    f_order = check_timestamp_ordering(bad_order_df, "timestamp", [], "test_ds", "test_p")
    assert len(f_order) == 1
