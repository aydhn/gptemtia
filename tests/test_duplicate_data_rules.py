import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.duplicate_data_rules import (
    build_duplicate_data_rule_set,
    check_duplicate_records,
)


def test_duplicate_data_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_duplicate_data_rule_set(profile)
    assert len(df_rules) >= 1

    test_df = pd.DataFrame([
        {"id": 1, "val": 10},
        {"id": 1, "val": 20}, # duplicate id
    ])
    findings = check_duplicate_records(test_df, ["id"], "dataset_sample", "test_p")
    assert len(findings) == 1
    assert findings[0].finding_type == "finding_duplicate_record"
