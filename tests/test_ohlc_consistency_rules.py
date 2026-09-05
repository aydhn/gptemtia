import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.ohlc_consistency_rules import (
    build_ohlc_consistency_rule_contract,
    check_ohlc_consistency,
)


def test_ohlc_consistency_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_ohlc_consistency_rule_contract(profile)
    assert len(df_rules) >= 2

    # High < Low
    bad_hl = pd.DataFrame([
        {"open": 10.0, "high": 9.0, "low": 11.0, "close": 10.0}
    ])
    f_hl = check_ohlc_consistency(bad_hl, "dataset_fx_ohlcv", "test_p")
    assert any(f.finding_type == "finding_ohlc_inconsistency" for f in f_hl)

    # Open > High
    bad_oc = pd.DataFrame([
        {"open": 12.0, "high": 10.0, "low": 9.0, "close": 9.5}
    ])
    f_oc = check_ohlc_consistency(bad_oc, "dataset_fx_ohlcv", "test_p")
    assert any(f.field_name == "open_close" for f in f_oc)
