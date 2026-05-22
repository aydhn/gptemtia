import pandas as pd
from synthetic_indices.relative_momentum import (
    calculate_multi_window_momentum,
    calculate_momentum_consistency,
    calculate_relative_momentum_score
)

def test_relative_momentum():
    dates = pd.date_range("2023-01-01", periods=30)
    # A has positive mom, B has negative
    retA = pd.Series([0.01]*30, index=dates)
    retB = pd.Series([-0.01]*30, index=dates)

    returns_df = pd.DataFrame({"A": retA, "B": retB})

    mom_df = calculate_multi_window_momentum(returns_df, (10, 20))
    assert mom_df.loc[mom_df["symbol"] == "A", "momentum_10"].iloc[0] > 0

    cons_df = calculate_momentum_consistency(mom_df)
    assert cons_df.loc[cons_df["symbol"] == "A", "momentum_consistency"].iloc[0] == 1.0 # 2 out of 2 positive
    assert cons_df.loc[cons_df["symbol"] == "B", "momentum_consistency"].iloc[0] == 0.0 # 0 out of 2 positive

    score_df = calculate_relative_momentum_score(cons_df)
    assert score_df.loc[score_df["symbol"] == "A", "momentum_rank"].iloc[0] == 1
    assert "momentum_label" in score_df.columns
