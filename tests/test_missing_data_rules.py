import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.missing_data_rules import (
    build_missing_data_rule_set,
    check_missing_required_fields,
    check_missing_values,
)


def test_missing_data_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_missing_data_rule_set(profile)
    assert len(df_rules) >= 2

    # Test missing fields
    test_df = pd.DataFrame([{"a": 1, "b": None}])
    f_missing_field = check_missing_required_fields(test_df, ["a", "c"], "test_type", "test_prov")
    assert len(f_missing_field) == 1
    assert f_missing_field[0].field_name == "c"

    # Test missing values (NaN)
    f_missing_val = check_missing_values(test_df, ["a", "b"], "test_type", "test_prov")
    assert len(f_missing_val) == 1
    assert f_missing_val[0].field_name == "b"
