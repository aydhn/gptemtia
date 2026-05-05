import pytest
import pandas as pd
import numpy as np
from asset_profiles.correlation_features import (
    calculate_rolling_correlation,
    calculate_symbol_group_correlation,
    calculate_macro_correlation_features,
)


def test_calculate_rolling_correlation():
    idx = pd.date_range("2023-01-01", periods=10)
    s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=idx)
    s2 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=idx)

    corr = calculate_rolling_correlation(s1, s2, window=3)
    assert not corr.isna().all()
    # Perfect positive correlation
    assert np.isclose(corr.dropna().iloc[-1], 1.0)


def test_calculate_symbol_group_correlation():
    idx = pd.date_range("2023-01-01", periods=10)
    sym = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=idx)
    grp = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=idx)

    df = calculate_symbol_group_correlation(sym, grp, window=3)
    assert "corr_symbol_group_3" in df.columns


def test_calculate_macro_correlation_features():
    idx = pd.date_range("2023-01-01", periods=10)
    sym = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=idx)

    macro = pd.DataFrame(
        {
            "USDTRY=X_close": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            "gold_close": [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],
        },
        index=idx,
    )

    df = calculate_macro_correlation_features(sym, macro, window=3)
    assert "corr_symbol_usdtry_3" in df.columns
    assert "corr_symbol_gold_3" in df.columns

    # Gold is perfectly negatively correlated with index
    assert df["corr_symbol_gold_3"].dropna().iloc[-1] < -0.99
