import pytest
import pandas as pd
from pathlib import Path
import tempfile
from performance.cache_inventory import (
    scan_cache_directory,
    classify_cache_file,
    calculate_cache_size_summary,
    build_cache_hit_miss_report,
    summarize_cache_inventory
)

def test_scan_cache_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        p = Path(tmpdir) / "test.parquet"
        p.write_text("dummy")

        df, summary = scan_cache_directory(Path(tmpdir))
        assert not df.empty
        assert summary["total_files"] == 1
        assert summary["total_size_mb"] > 0

def test_classify_cache_file():
    assert classify_cache_file(Path("test.csv")) == "csv"

def test_build_cache_hit_miss_report():
    # Empty
    df, summary = build_cache_hit_miss_report(None)
    assert df.empty
    assert summary["overall_hit_rate"] == 0.0

    # Mock data
    records = pd.DataFrame([{"cache_key": "k1"}])
    df, summary = build_cache_hit_miss_report(records)
    assert not df.empty
    assert summary["total_hits"] > 0
