import pytest
import pandas as pd
from validation.time_splits import (
    create_train_test_split,
    create_walk_forward_splits,
    validate_time_splits,
    filter_dataframe_by_split
)
from validation.validation_models import TimeSplit

@pytest.fixture
def sample_index():
    return pd.date_range(start="2020-01-01", periods=1000, freq="D")

def test_create_train_test_split(sample_index):
    split = create_train_test_split(sample_index, train_ratio=0.7)
    assert "train_start" in split
    assert split["train_bars"] == 700
    assert split["test_bars"] == 300

def test_create_walk_forward_splits(sample_index):
    splits = create_walk_forward_splits(
        sample_index,
        train_window_bars=200,
        test_window_bars=50,
        step_bars=50
    )
    assert len(splits) > 0
    assert splits[0].train_bars == 200
    assert splits[0].test_bars == 50
    assert splits[1].train_bars == 200

def test_expanding_window(sample_index):
    splits = create_walk_forward_splits(
        sample_index,
        train_window_bars=200,
        test_window_bars=50,
        step_bars=50,
        expanding_window=True
    )
    assert splits[0].train_start == splits[1].train_start
    assert splits[1].train_bars > splits[0].train_bars

def test_validate_time_splits():
    split1 = TimeSplit("id1", "2020-01-01", "2020-06-30", "2020-07-01", "2020-12-31", 180, 180, 0)
    split2 = TimeSplit("id2", "2020-07-01", "2020-12-31", "2021-01-01", "2021-06-30", 180, 180, 1)

    validation = validate_time_splits([split1, split2])
    assert validation["valid"] is True

    split3 = TimeSplit("id3", "2020-01-01", "2020-06-30", "2020-05-01", "2020-12-31", 180, 180, 0)
    validation_overlap = validate_time_splits([split3])
    assert validation_overlap["valid"] is False

def test_filter_dataframe(sample_index):
    df = pd.DataFrame({"value": range(1000)}, index=sample_index)
    split = TimeSplit("id1", "2020-01-01", "2020-01-10", "2020-01-11", "2020-01-20", 10, 10, 0)

    train_df = filter_dataframe_by_split(df, split, "train")
    test_df = filter_dataframe_by_split(df, split, "test")

    assert len(train_df) == 10
    assert len(test_df) == 10
