import pandas as pd
from synthetic_indices.relative_strength import (
    calculate_relative_return,
    calculate_relative_strength_table,
    rank_relative_strength,
    infer_relative_strength_label
)

def test_relative_strength():
    dates = pd.date_range("2023-01-01", periods=10)
    # A outperforms, B underperforms benchmark
    bench = pd.Series([0.01]*10, index=dates)
    retA = pd.Series([0.02]*10, index=dates)
    retB = pd.Series([-0.01]*10, index=dates)

    returns_df = pd.DataFrame({"A": retA, "B": retB})

    rs_df = calculate_relative_strength_table(returns_df, bench, (5,))

    # Check relative returns
    assert float(rs_df.loc[rs_df["symbol"] == "A", "relative_return_5"].iloc[0]) > 0
    assert rs_df.loc[rs_df["symbol"] == "B", "relative_return_5"].iloc[0] < 0

    ranked = rank_relative_strength(rs_df)

    # A should be ranked 1
    assert ranked.loc[ranked["symbol"] == "A", "relative_rank"].iloc[0] == 1
    # B should be laggard
    assert ranked.loc[ranked["symbol"] == "B", "relative_strength_label"].iloc[0] in ["strong_laggard", "moderate_laggard", "insufficient_data", "neutral_relative_strength"]

def test_infer_relative_strength_label():
    assert infer_relative_strength_label(0.9) == "strong_leader"
    assert infer_relative_strength_label(0.1) == "strong_laggard"
    assert infer_relative_strength_label(None) == "insufficient_data"
