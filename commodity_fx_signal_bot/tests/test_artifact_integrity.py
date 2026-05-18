import pytest
from pathlib import Path
import pandas as pd
import json

from data.storage.data_lake import DataLake
from observability.artifact_integrity import (
    check_file_exists_and_nonempty,
    check_csv_readable,
    check_json_readable,
    check_parquet_readable,
    check_dataframe_schema,
    build_artifact_integrity_report
)

def test_check_file_exists_and_nonempty(tmp_path):
    f = tmp_path / "test.txt"

    assert check_file_exists_and_nonempty(f)["exists"] == False

    f.touch()
    assert check_file_exists_and_nonempty(f)["empty"] == True

    with open(f, 'w') as fh:
        fh.write("content")

    res = check_file_exists_and_nonempty(f)
    assert res["valid"] == True
    assert res["empty"] == False

def test_check_csv_readable(tmp_path):
    f = tmp_path / "test.csv"
    with open(f, 'w') as fh:
        fh.write("col1,col2\n1,2\n3,4")

    res = check_csv_readable(f)
    assert res["valid"] == True
    assert "col1" in res["columns"]

def test_check_json_readable(tmp_path):
    f = tmp_path / "test.json"

    # invalid json
    with open(f, 'w') as fh:
        fh.write("{invalid}")
    assert check_json_readable(f)["valid"] == False

    # valid json
    with open(f, 'w') as fh:
        fh.write('{"key": "value"}')
    assert check_json_readable(f)["valid"] == True

def test_check_parquet_readable(tmp_path):
    f = tmp_path / "test.parquet"
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    df.to_parquet(f)

    res = check_parquet_readable(f)
    assert res["valid"] == True
    assert res["num_rows"] == 2

def test_check_dataframe_schema():
    df = pd.DataFrame({"a": [1], "b": [2]})

    res1 = check_dataframe_schema(df, ["a", "b"])
    assert res1["valid"] == True

    res2 = check_dataframe_schema(df, ["a", "b", "c"])
    assert res2["valid"] == False
    assert "c" in res2["missing_columns"]

class MockPaths:
    def __init__(self, root: Path):
        self.lake_dir = root / "lake"
        self.LAKE_MANIFESTS_DIR = self.lake_dir / "manifests"
        self.LAKE_PROCESSED_OHLCV_DIR = self.lake_dir / "processed" / "ohlcv"
        self.LAKE_DIR = self.lake_dir

        self.LAKE_MANIFESTS_DIR.mkdir(parents=True, exist_ok=True)
        self.LAKE_PROCESSED_OHLCV_DIR.mkdir(parents=True, exist_ok=True)

def test_build_artifact_integrity_report(tmp_path):
    paths = MockPaths(tmp_path)
    lake = DataLake(paths)
    lake.paths = paths

    # Create some dummy artifacts
    (paths.LAKE_MANIFESTS_DIR / "test1.json").write_text('{"a": 1}')
    (paths.LAKE_MANIFESTS_DIR / "bad.json").write_text('{bad}')

    df, summary = build_artifact_integrity_report(lake)

    assert not df.empty
    assert summary["total_checked"] == 2
    assert summary["invalid_count"] == 1
    assert summary["valid_count"] == 1
