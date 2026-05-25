import pytest
import pandas as pd
from pathlib import Path
import tempfile
from performance.performance_models import CacheRecord, build_cache_id
from performance.cache_registry import (
    CacheRegistry,
    build_cache_key,
    build_source_signature,
    infer_cache_type_from_path,
    cache_records_to_dataframe
)

def test_build_cache_key():
    key1 = build_cache_key("mod", "op", {"a": 1})
    key2 = build_cache_key("mod", "op", {"a": 1})
    assert key1 == key2
    assert len(key1) <= 16

def test_build_source_signature():
    sig = build_source_signature([], {"b": 2})
    assert len(sig) <= 16

def test_infer_cache_type():
    assert infer_cache_type_from_path(Path("data.parquet")) == "parquet"
    assert infer_cache_type_from_path(Path("data.csv")) == "csv"

def test_cache_registry():
    with tempfile.TemporaryDirectory() as tmpdir:
        registry = CacheRegistry(Path(tmpdir))

        record = CacheRecord(
            cache_id="c1",
            cache_key="key1",
            cache_type="parquet",
            path="/tmp/test",
            size_bytes=100,
            created_at_utc="now",
            expires_at_utc="later",
            status="active",
            source_signature="sig",
            warnings=[]
        )

        registry.add_cache_record(record)
        df = registry.load_cache_records()
        assert len(df) == 1

        summary = registry.summarize()
        assert summary["total_records"] == 1

        found = registry.get_cache_record("key1")
        assert found is not None
        assert found["cache_id"] == "c1"

        registry.mark_cache_status("key1", "invalid")
        updated = registry.get_cache_record("key1")
        assert updated["status"] == "invalid"
