import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.macro_quality_rules import (
    build_macro_quality_rule_set,
    check_macro_timeseries_quality,
    check_macro_release_metadata_quality,
)


def test_macro_quality_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_macro_quality_rule_set(profile)
    assert len(df_rules) >= 2

    # Missing macro timeseries required field
    macro_df = pd.DataFrame([{"indicator": "CPI", "value": 3.2}])
    f_macro = check_macro_timeseries_quality(macro_df, "macro_test_prov")
    assert any(f.field_name == "timestamp" for f in f_macro)

    # Missing revision status
    f_rel = check_macro_release_metadata_quality(macro_df, "macro_test_prov")
    assert any(f.field_name == "revision_status" for f in f_rel)
