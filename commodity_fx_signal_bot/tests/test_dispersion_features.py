import pytest
import pandas as pd
import numpy as np
from asset_profiles.dispersion_features import (
    calculate_group_dispersion,
    calculate_group_breadth,
    calculate_leader_laggard_spread,
    build_dispersion_feature_frame,
)


@pytest.fixture
def return_matrix():
    idx = pd.date_range("2023-01-01", periods=10)
    return pd.DataFrame(
        {
            "A": np.linspace(0.01, 0.1, 10),
            "B": np.linspace(0.005, 0.05, 10),
            "C": np.linspace(-0.01, -0.1, 10),
        },
        index=idx,
    )


def test_calculate_group_dispersion(return_matrix):
    disp = calculate_group_dispersion(return_matrix, window=3)
    assert "dispersion_3" in disp.columns
    assert not disp["dispersion_3"].isna().all()


def test_calculate_group_breadth(return_matrix):
    breadth = calculate_group_breadth(return_matrix, window=3)
    assert "breadth_positive_3" in breadth.columns
    # 2 positives, 1 negative -> breadth = 2/3
    val = breadth["breadth_positive_3"].dropna().iloc[-1]
    assert np.isclose(val, 2 / 3)


def test_calculate_leader_laggard_spread(return_matrix):
    spread = calculate_leader_laggard_spread(return_matrix, window=3)
    assert "leader_laggard_spread_3" in spread.columns
    # Spread should be positive
    assert spread["leader_laggard_spread_3"].dropna().iloc[-1] > 0


def test_build_dispersion_feature_frame(return_matrix):
    df, summary = build_dispersion_feature_frame("metals", return_matrix)
    assert not df.empty
    assert "group_metals_dispersion_63" in df.columns
    assert "group_metals_breadth_positive_21" in df.columns
    assert "group_metals_dispersion_high" in df.columns
