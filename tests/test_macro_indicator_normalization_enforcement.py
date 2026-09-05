import pandas as pd
from advanced_data_normalization.macro_indicator_normalization_enforcement import (
    normalize_macro_indicator_value,
    normalize_macro_indicator_dataframe,
    build_macro_indicator_normalization_enforcement_report,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalize_macro_indicator_value():
    assert normalize_macro_indicator_value("US10Y") == "US_10Y_YIELD"
    assert normalize_macro_indicator_value("FEDFUNDS") == "FED_POLICY_RATE"
    assert normalize_macro_indicator_value("CPI_US_YOY") == "US_CPI_YOY"
    assert normalize_macro_indicator_value("DXY") == "DXY_PLACEHOLDER"


def test_normalize_macro_indicator_dataframe():
    raw_df = pd.DataFrame([{"indicator": "US10Y"}, {"indicator": "FEDFUNDS"}])
    norm_df, findings = normalize_macro_indicator_dataframe(raw_df, field="indicator")

    assert "normalized_indicator" in norm_df.columns
    assert norm_df["normalized_indicator"].iloc[0] == "US_10Y_YIELD"
    assert norm_df["normalized_indicator"].iloc[1] == "FED_POLICY_RATE"


def test_macro_indicator_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_macro_indicator_normalization_enforcement_report(prof)
    assert not df.empty
    assert summary["total_mappings"] >= 5
