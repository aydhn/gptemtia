import pytest
import pandas as pd
import numpy as np
from asset_profiles.relative_strength import (
    calculate_relative_strength_vs_group,
    calculate_relative_strength_rank,
    build_relative_strength_features,
)


def test_calculate_relative_strength_vs_group():
    idx = pd.date_range("2023-01-01", periods=10)
    symbol_s = pd.Series(np.linspace(100, 110, 10), index=idx)
    group_idx = pd.Series(np.linspace(100, 105, 10), index=idx)

    rs = calculate_relative_strength_vs_group(symbol_s, group_idx, windows=(2, 4))
    assert "rs_vs_group_2" in rs.columns
    assert "rs_vs_group_4" in rs.columns


def test_calculate_relative_strength_rank():
    idx = pd.date_range("2023-01-01", periods=10)
    # A performs best, B medium, C worst
    returns = pd.DataFrame(
        {
            "A": np.linspace(0.01, 0.1, 10),
            "B": np.linspace(0.005, 0.05, 10),
            "C": np.linspace(-0.01, -0.1, 10),
        },
        index=idx,
    )

    ranks, percentiles = calculate_relative_strength_rank(returns, window=2)
    assert not ranks.empty

    # After window, C should be rank 3.0, A should be rank 1.0
    assert ranks["C"].iloc[-1] == 3.0
    assert ranks["A"].iloc[-1] == 1.0


def test_build_relative_strength_features():
    idx = pd.date_range("2023-01-01", periods=10)
    df = pd.DataFrame({"close": np.linspace(100, 110, 10)}, index=idx)
    group_idx = pd.Series(np.linspace(100, 105, 10), index=idx)

    returns = pd.DataFrame(
        {
            "TEST": np.linspace(0.01, 0.1, 10),
            "B": np.linspace(0.005, 0.05, 10),
            "C": np.linspace(-0.01, -0.1, 10),
        },
        index=idx,
    )

    features, summary = build_relative_strength_features("TEST", df, group_idx, returns)
    assert not features.empty
    assert "rs_vs_group_21" in features.columns
    assert "rs_is_group_leader" in features.columns
    assert summary["rows"] == 10
