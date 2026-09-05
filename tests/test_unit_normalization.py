import pandas as pd
from advanced_data_normalization.unit_normalization import (
    normalize_unit_value,
    normalize_unit_dataframe,
    build_unit_normalization_registry,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalize_unit_value():
    assert normalize_unit_value("percent") == "percent"
    assert normalize_unit_value("%") == "percent"
    assert normalize_unit_value("bps") == "bps"
    assert normalize_unit_value("USD/barrel") == "usd_per_barrel"
    assert normalize_unit_value("USD/oz") == "usd_per_oz"


def test_normalize_unit_dataframe():
    raw_df = pd.DataFrame([{"unit": "%"}, {"unit": "USD/barrel"}])
    norm_df, findings = normalize_unit_dataframe(raw_df, field="unit")

    assert "normalized_unit" in norm_df.columns
    assert norm_df["normalized_unit"].iloc[0] == "percent"
    assert norm_df["normalized_unit"].iloc[1] == "usd_per_barrel"


def test_unit_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_unit_normalization_registry(prof)
    assert not df.empty
    assert summary["total_mappings"] >= 5
