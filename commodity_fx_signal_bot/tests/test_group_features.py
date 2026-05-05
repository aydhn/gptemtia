import pytest
import pandas as pd
import numpy as np
from asset_profiles.group_features import (
    build_group_price_matrix,
    build_group_return_matrix,
    build_equal_weight_group_index,
    calculate_group_momentum,
    build_group_feature_frame,
)


@pytest.fixture
def mock_data():
    idx = pd.date_range("2023-01-01", periods=10)
    return {
        "A": pd.DataFrame(
            {"close": [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]}, index=idx
        ),
        "B": pd.DataFrame(
            {"close": [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]}, index=idx
        ),
    }


def test_build_group_price_matrix(mock_data):
    matrix = build_group_price_matrix(mock_data)
    assert matrix.shape == (10, 2)
    assert "A" in matrix.columns
    assert "B" in matrix.columns


def test_build_group_return_matrix(mock_data):
    matrix = build_group_price_matrix(mock_data)
    ret = build_group_return_matrix(matrix)
    assert ret.shape == (10, 2)
    assert pd.isna(ret.iloc[0]).all()
    assert not pd.isna(ret.iloc[1]).any()


def test_build_equal_weight_group_index(mock_data):
    matrix = build_group_price_matrix(mock_data)
    idx = build_equal_weight_group_index(matrix)
    assert len(idx) in (9, 10)
    assert idx.iloc[0] > 100.0
    assert idx.iloc[-1] > 100.0


def test_calculate_group_momentum(mock_data):
    matrix = build_group_price_matrix(mock_data)
    idx = build_equal_weight_group_index(matrix)
    mom = calculate_group_momentum(idx, windows=(2, 4))
    assert "momentum_2" in mom.columns
    assert "momentum_4" in mom.columns
    assert pd.isna(mom["momentum_2"].iloc[0])


def test_build_group_feature_frame(mock_data):
    features, summary = build_group_feature_frame("metals", mock_data)
    assert not features.empty
    assert "group_metals_index" in features.columns
    assert "group_metals_member_count" in features.columns
    assert summary["rows"] == 10
    assert "A" in summary["members"]
