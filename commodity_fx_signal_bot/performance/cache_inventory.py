from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Optional
import os

from .cache_registry import infer_cache_type_from_path

def scan_cache_directory(cache_dir: Path) -> Tuple[pd.DataFrame, Dict]:
    records = []

    if cache_dir.exists() and cache_dir.is_dir():
        for item in cache_dir.rglob("*"):
            if item.is_file():
                stat = item.stat()
                records.append({
                    "file_name": item.name,
                    "path": str(item),
                    "cache_type": infer_cache_type_from_path(item),
                    "size_bytes": stat.st_size,
                    "modified_at": stat.st_mtime
                })

    df = pd.DataFrame(records)
    summary = calculate_cache_size_summary(df)
    return df, summary

def classify_cache_file(path: Path) -> str:
    return infer_cache_type_from_path(path)

def calculate_cache_size_summary(cache_df: pd.DataFrame) -> dict:
    if cache_df.empty:
        return {"total_files": 0, "total_size_mb": 0.0, "large_cache_warning": False}

    total_size = cache_df["size_bytes"].sum() if "size_bytes" in cache_df.columns else 0
    total_size_mb = total_size / (1024 * 1024)

    return {
        "total_files": len(cache_df),
        "total_size_mb": total_size_mb,
        "large_cache_warning": total_size_mb > 1024 # Warning if over 1GB overall
    }

def build_cache_hit_miss_report(cache_records_df: Optional[pd.DataFrame] = None) -> Tuple[pd.DataFrame, Dict]:
    # In a real system, we'd log hits and misses. Here we just mock it based on registry for demonstration.
    # We will assume statuses "hit" and "miss" might be recorded.

    if cache_records_df is None or cache_records_df.empty:
        df = pd.DataFrame(columns=["cache_key", "hits", "misses", "hit_rate"])
        return df, {"total_hits": 0, "total_misses": 0, "overall_hit_rate": 0.0}

    # Mock data generation based on whatever is passed in
    mock_stats = []
    total_hits = 0
    total_misses = 0

    for _, row in cache_records_df.iterrows():
        key = row.get("cache_key", "unknown")
        # Generate some mock stats
        hits = 5
        misses = 2

        mock_stats.append({
            "cache_key": key,
            "hits": hits,
            "misses": misses,
            "hit_rate": hits / (hits + misses) if (hits + misses) > 0 else 0
        })

        total_hits += hits
        total_misses += misses

    df = pd.DataFrame(mock_stats)
    summary = {
        "total_hits": total_hits,
        "total_misses": total_misses,
        "overall_hit_rate": total_hits / (total_hits + total_misses) if (total_hits + total_misses) > 0 else 0.0
    }

    return df, summary

def summarize_cache_inventory(cache_df: pd.DataFrame) -> dict:
    return calculate_cache_size_summary(cache_df)
