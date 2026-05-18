import pytest
import time
import pandas as pd
from datetime import datetime, timedelta, timezone
from pathlib import Path

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from observability.data_freshness import (
    calculate_file_age_hours,
    check_dataframe_freshness,
    check_feature_file_freshness,
    build_data_freshness_report
)

def test_calculate_file_age_hours(tmp_path):
    # Non-existent file
    assert calculate_file_age_hours(tmp_path / "does_not_exist.txt") is None

    # Newly created file
    f = tmp_path / "test.txt"
    f.touch()
    age = calculate_file_age_hours(f)
    assert age is not None
    assert 0 <= age < 0.1 # Should be very close to 0

def test_check_dataframe_freshness():
    # Empty df
    assert not check_dataframe_freshness(pd.DataFrame())["fresh"]

    # Fresh df
    now = datetime.now(timezone.utc)
    df_fresh = pd.DataFrame({"val": [1, 2]}, index=[now - timedelta(hours=1), now])
    res1 = check_dataframe_freshness(df_fresh, max_stale_hours=2.0)
    assert res1["fresh"] == True
    assert res1["age_hours"] < 1.0 # The max index is 'now', so age is ~0

    # Stale df
    old = now - timedelta(hours=10)
    df_stale = pd.DataFrame({"val": [1, 2]}, index=[old - timedelta(hours=1), old])
    res2 = check_dataframe_freshness(df_stale, max_stale_hours=2.0)
    assert res2["fresh"] == False
    assert res2["age_hours"] > 9.0

def test_check_feature_file_freshness(tmp_path):
    f = tmp_path / "test.parquet"

    # Missing
    res1 = check_feature_file_freshness(f, max_stale_hours=24.0)
    assert res1["exists"] == False
    assert res1["status"] == "missing"

    # Present and fresh
    f.touch()
    res2 = check_feature_file_freshness(f, max_stale_hours=24.0)
    assert res2["exists"] == True
    assert res2["stale"] == False
    assert res2["status"] == "fresh"

class MockPaths:
    def __init__(self, root: Path):
        self.lake_dir = root / "lake"
        self.LAKE_PROCESSED_OHLCV_DIR = self.lake_dir / "processed" / "ohlcv"
        self.LAKE_FEATURES_TECHNICAL_DIR = self.lake_dir / "features" / "technical"
        self.LAKE_DIR = self.lake_dir

@pytest.fixture
def mock_data_lake(tmp_path):
    paths = MockPaths(tmp_path)
    lake = DataLake(paths)
    lake.paths = paths
    return lake

def test_build_data_freshness_report(mock_data_lake):
    spec = SymbolSpec(symbol="GC=F", name="Gold", asset_class="metals", sub_class="precious", currency="USD", data_source="yahoo")

    df, summary = build_data_freshness_report(mock_data_lake, [spec], "1d", max_stale_hours=24.0)

    assert not df.empty
    assert summary["missing_count"] > 0
    assert summary["status"] == "degraded"
