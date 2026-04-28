import pytest
import pandas as pd
from pathlib import Path
from data.storage.cache_manager import CacheManager


@pytest.fixture
def cache_dir(tmp_path):
    return tmp_path / "cache"


@pytest.fixture
def sample_df():
    dates = pd.date_range("2023-01-01", periods=3, tz="UTC")
    df = pd.DataFrame(
        {
            "open": [10.0, 11.0, 12.0],
            "high": [10.5, 11.5, 12.5],
            "low": [9.5, 10.5, 11.5],
            "close": [10.2, 11.2, 12.2],
            "adj_close": [10.2, 11.2, 12.2],
            "volume": [100, 200, 150],
        },
        index=dates,
    )
    return df


def test_build_cache_path(cache_dir):
    manager = CacheManager(cache_dir)
    path = manager.build_cache_path("GC=F", "1d", period="1y", format_ext="parquet")

    assert str(cache_dir) in str(path)
    assert "GCF" in str(path)  # = is removed
    assert "1d" in str(path)
    assert "1y" in str(path)
    assert ".parquet" in str(path)


def test_save_and_load_parquet(cache_dir, sample_df):
    manager = CacheManager(cache_dir)
    path = manager.build_cache_path("TEST", "1d", period="1mo", format_ext="parquet")

    manager.save_dataframe(sample_df, path)
    assert manager.exists(path)

    loaded_df = manager.load_dataframe(path)
    # Compare while ignoring freq attribute of the DatetimeIndex
    pd.testing.assert_frame_equal(sample_df, loaded_df, check_freq=False)


def test_clear_cache(cache_dir, sample_df):
    manager = CacheManager(cache_dir)
    path1 = manager.build_cache_path("TEST1", "1d", period="1mo", format_ext="parquet")
    path2 = manager.build_cache_path("TEST2", "1d", period="1mo", format_ext="parquet")

    manager.save_dataframe(sample_df, path1)
    manager.save_dataframe(sample_df, path2)

    assert manager.exists(path1)
    assert manager.exists(path2)

    manager.clear_cache()

    assert not manager.exists(path1)
    assert not manager.exists(path2)
