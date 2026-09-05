import pandas as pd
from advanced_data_normalization.frequency_normalization import (
    normalize_frequency_value,
    normalize_frequency_dataframe,
    build_frequency_normalization_registry,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalize_frequency_value():
    assert normalize_frequency_value("daily") == "1d"
    assert normalize_frequency_value("1d") == "1d"
    assert normalize_frequency_value("weekly") == "1w"
    assert normalize_frequency_value("monthly") == "1mo"
    assert normalize_frequency_value("quarterly") == "1q"
    assert normalize_frequency_value("yearly") == "1y"


def test_normalize_frequency_dataframe():
    raw_df = pd.DataFrame([{"frequency": "daily"}, {"frequency": "monthly"}])
    norm_df, findings = normalize_frequency_dataframe(raw_df, field="frequency")

    assert "normalized_frequency" in norm_df.columns
    assert norm_df["normalized_frequency"].iloc[0] == "1d"
    assert norm_df["normalized_frequency"].iloc[1] == "1mo"


def test_frequency_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_frequency_normalization_registry(prof)
    assert not df.empty
    assert summary["total_mappings"] >= 5
