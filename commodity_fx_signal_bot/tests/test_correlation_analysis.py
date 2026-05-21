import pandas as pd
import numpy as np
from portfolio_research.correlation_analysis import (
    calculate_correlation_matrix,
    calculate_rolling_average_correlation,
    calculate_pairwise_correlation_table,
    identify_high_correlation_pairs,
    calculate_average_correlation
)

def test_correlation_analysis():
    dates = pd.date_range("2023-01-01", periods=100)
    df = pd.DataFrame({
        "A": np.random.randn(100),
        "B": np.random.randn(100)
    }, index=dates)
    df["C"] = df["A"] * 0.9 + np.random.randn(100) * 0.1

    corr = calculate_correlation_matrix(df)
    assert corr.shape == (3, 3)

    roll = calculate_rolling_average_correlation(df, window=20)
    assert not roll.empty

    pair = calculate_pairwise_correlation_table(corr)
    # len for 3 items = 3 combinations
    assert len(pair) <= 3

    high = identify_high_correlation_pairs(pair, threshold=0.5)
    assert len(high) > 0

    avg = calculate_average_correlation(corr)
    assert avg is not None
