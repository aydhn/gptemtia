import pandas as pd
from advanced_data_normalization.numeric_type_normalization import (
    normalize_numeric_value,
    normalize_numeric_dataframe,
    build_numeric_type_normalization_registry,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalize_numeric_value():
    assert normalize_numeric_value("123.45") == 123.45
    assert normalize_numeric_value("1,234.56") == 1234.56
    assert normalize_numeric_value("15%") == 15.0
    assert normalize_numeric_value(42) == 42.0
    assert normalize_numeric_value("invalid_num") is None


def test_normalize_numeric_dataframe():
    raw_df = pd.DataFrame([{"val": "100.5"}, {"val": "corrupted"}])
    norm_df, findings = normalize_numeric_dataframe(raw_df, fields=["val"])

    # Source column is preserved
    assert "val" in norm_df.columns
    assert "normalized_val" in norm_df.columns
    assert norm_df["normalized_val"].iloc[0] == 100.5
    assert pd.isna(norm_df["normalized_val"].iloc[1])
    assert len(findings) == 1
    assert findings[0].manual_review_required is True


def test_numeric_type_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_numeric_type_normalization_registry(prof)
    assert not df.empty
