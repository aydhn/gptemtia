import pytest
import pandas as pd
import numpy as np

from regimes.regime_features import safe_get_column, normalize_to_unit_interval, combine_scores, add_regime_base_features

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "col1": [1, 2, np.nan, 4, 5],
        "col2": [np.nan, np.nan, np.nan, np.nan, np.nan],
        "col3": [10, 20, 30, 40, 50]
    })

def test_safe_get_column(sample_df):
    assert safe_get_column(sample_df, ["col2", "col1"]) is not None
    assert safe_get_column(sample_df, ["col2"]) is None
    assert safe_get_column(sample_df, ["nonexistent"]) is None

def test_normalize_to_unit_interval():
    s = pd.Series([10, 20, 30, 40, 50])
    norm = normalize_to_unit_interval(s)
    # The last value should be 1.0 based on rolling logic
    assert norm.iloc[-1] == 1.0

    # Handle NaNs or flat
    s2 = pd.Series([10, 10, 10, 10])
    norm2 = normalize_to_unit_interval(s2)
    assert not norm2.isna().any()

def test_combine_scores():
    s1 = pd.Series([1, 2, np.nan, 4])
    s2 = pd.Series([3, 4, 5, np.nan])
    s3 = pd.Series([np.nan, np.nan, np.nan, np.nan])

    comb = combine_scores([s1, s2, s3])
    assert comb.iloc[0] == 2.0  # (1+3)/2
    assert comb.iloc[2] == 5.0  # (nan+5)/1

    comb_w = combine_scores([s1, s2], weights=[0.2, 0.8])
    assert comb_w.iloc[0] == (1*0.2 + 3*0.8)

def test_add_regime_base_features(sample_df):
    out, sum_dict = add_regime_base_features(sample_df)
    assert "regime_trend_strength_raw" in out.columns
    assert sum_dict["input_rows"] == 5
    assert len(sum_dict["columns_added"]) > 0
