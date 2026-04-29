import numpy as np
import pandas as pd
import pytest

from core.exceptions import DataQualityError
from data.data_quality import (
    build_data_quality_report,
    is_dataframe_usable,
    validate_ohlcv_dataframe,
)


@pytest.fixture
def valid_df():
    dates = pd.date_range("2023-01-01", periods=5, tz="UTC")
    df = pd.DataFrame(
        {
            "open": [10.0, 11.0, 12.0, 11.5, 12.5],
            "high": [10.5, 11.5, 12.5, 12.0, 13.0],
            "low": [9.5, 10.5, 11.5, 11.0, 12.0],
            "close": [10.2, 11.2, 12.2, 11.8, 12.8],
            "adj_close": [10.2, 11.2, 12.2, 11.8, 12.8],
            "volume": [100, 200, 150, 300, 250],
        },
        index=dates,
    )
    return df


def test_validate_valid_df(valid_df):
    validate_ohlcv_dataframe(valid_df)  # Should not raise


def test_validate_missing_columns(valid_df):
    invalid_df = valid_df.drop(columns=["close"])
    with pytest.raises(DataQualityError, match="Missing required columns"):
        validate_ohlcv_dataframe(invalid_df)


def test_validate_duplicate_index(valid_df):
    df_dup = pd.concat([valid_df, valid_df.iloc[[0]]])
    with pytest.raises(DataQualityError, match="contains duplicates"):
        validate_ohlcv_dataframe(df_dup)


def test_validate_negative_prices(valid_df):
    invalid_df = valid_df.copy()
    invalid_df.loc[invalid_df.index[0], "low"] = -1.0
    with pytest.raises(DataQualityError, match="Negative prices found"):
        validate_ohlcv_dataframe(invalid_df)


def test_validate_high_less_than_low(valid_df):
    invalid_df = valid_df.copy()
    invalid_df.loc[invalid_df.index[0], "high"] = 9.0
    with pytest.raises(DataQualityError, match="high price is lower than low price"):
        validate_ohlcv_dataframe(invalid_df)


def test_validate_all_nan_column(valid_df):
    invalid_df = valid_df.copy()
    invalid_df["close"] = np.nan
    with pytest.raises(DataQualityError, match="contains entirely NaN values"):
        validate_ohlcv_dataframe(invalid_df)


def test_is_dataframe_usable(valid_df):
    # Valid but short
    assert is_dataframe_usable(valid_df, min_rows=10) == False

    # Valid and long enough
    assert is_dataframe_usable(valid_df, min_rows=3) == True

    # Too many NaNs
    nan_df = valid_df.copy()
    nan_df.loc[nan_df.index[0], "close"] = np.nan
    nan_df.loc[nan_df.index[1], "close"] = np.nan
    assert is_dataframe_usable(nan_df, min_rows=3) == False


def test_build_data_quality_report(valid_df):
    report = build_data_quality_report(valid_df)
    assert report["rows"] == 5
    assert report["duplicate_index_count"] == 0
    assert report["negative_price_count"] == 0
    assert report["high_low_error_count"] == 0
    assert report["missing_ratio_by_column"]["close"] == 0.0


from data.data_quality import compare_dataframes_basic, infer_quality_grade


def test_infer_quality_grade():
    assert infer_quality_grade({"rows": 0}) == "F"
    assert infer_quality_grade({"rows": 100, "error": "API failed"}) == "F"
    assert infer_quality_grade({"rows": 40}) == "D"
    assert infer_quality_grade({"rows": 100, "close_missing_ratio": 0.06}) == "D"
    assert infer_quality_grade({"rows": 100, "close_missing_ratio": 0.02}) == "C"
    assert infer_quality_grade({"rows": 100, "duplicate_index_count": 1}) == "C"
    assert infer_quality_grade({"rows": 100, "close_missing_ratio": 0.005}) == "B"
    assert (
        infer_quality_grade(
            {
                "rows": 100,
                "close_missing_ratio": 0.0,
                "duplicate_index_count": 0,
                "negative_price_count": 0,
                "high_low_error_count": 0,
            }
        )
        == "A"
    )


def test_compare_dataframes_basic(valid_df):
    # Same df
    res = compare_dataframes_basic(valid_df, valid_df)
    assert res["old_rows"] == 5
    assert res["new_rows"] == 5
    assert res["added_rows"] == 0
    assert res["overlap_rows_estimate"] == 5
    assert res["changed_last_close"] == False

    # New df has 1 more row
    dates = pd.date_range("2023-01-01", periods=6, tz="UTC")
    new_df = pd.DataFrame(
        {
            "open": [10.0, 11.0, 12.0, 11.5, 12.5, 13.0],
            "high": [10.5, 11.5, 12.5, 12.0, 13.0, 13.5],
            "low": [9.5, 10.5, 11.5, 11.0, 12.0, 12.5],
            "close": [10.2, 11.2, 12.2, 11.8, 12.8, 13.2],
            "adj_close": [10.2, 11.2, 12.2, 11.8, 12.8, 13.2],
            "volume": [100, 200, 150, 300, 250, 300],
        },
        index=dates,
    )
    res2 = compare_dataframes_basic(valid_df, new_df)
    assert res2["old_rows"] == 5
    assert res2["new_rows"] == 6
    assert res2["added_rows"] == 1
    assert res2["overlap_rows_estimate"] == 5
    assert res2["changed_last_close"] == True
