import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.frequency_unit_consistency_rules import (
    build_frequency_unit_consistency_rule_set,
    check_frequency_values,
    check_unit_values,
)


def test_frequency_unit_consistency_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_frequency_unit_consistency_rule_set(profile)
    assert len(df_rules) >= 2

    # Invalid frequency
    test_df = pd.DataFrame([{"freq": "daily"}, {"freq": "every_second_century"}])
    f_freq = check_frequency_values(test_df, "freq", ["daily", "monthly", "quarterly"], "dataset_macro_timeseries", "test_p")
    assert len(f_freq) == 1
    assert f_freq[0].finding_type == "finding_frequency_unit_mismatch"

    # Invalid unit
    unit_df = pd.DataFrame([{"unit": "unknown_random_unit"}])
    f_unit = check_unit_values(unit_df, "unit", ["usd", "percent", "index"], "dataset_macro_timeseries", "test_p")
    assert len(f_unit) == 1
