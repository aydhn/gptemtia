"""
Artifact integrity diagnostics.
"""

import json
from pathlib import Path
from typing import Dict, Any, Tuple, List, Optional

import pandas as pd

from data.storage.data_lake import DataLake


def check_file_exists_and_nonempty(path: Path) -> Dict[str, Any]:
    """Check if a file exists and has content."""
    if not path.exists():
        return {"valid": False, "exists": False, "empty": True, "error": "File does not exist"}

    if not path.is_file():
        return {"valid": False, "exists": True, "empty": True, "error": "Path is not a regular file"}

    size = path.stat().st_size
    if size == 0:
        return {"valid": False, "exists": True, "empty": True, "error": "File is empty (0 bytes)"}

    return {"valid": True, "exists": True, "empty": False, "size_bytes": size}


def check_csv_readable(path: Path) -> Dict[str, Any]:
    """Check if a CSV file is structurally readable."""
    base_check = check_file_exists_and_nonempty(path)
    if not base_check["valid"]:
        return base_check

    try:
        # Just read a few rows to verify basic format
        df = pd.read_csv(path, nrows=5)
        if df.empty:
            return {"valid": False, "exists": True, "empty": True, "error": "CSV contains no data rows (header only?)"}
        return {"valid": True, "exists": True, "empty": False, "columns": list(df.columns)}
    except Exception as e:
        return {"valid": False, "exists": True, "empty": False, "error": f"Failed to parse CSV: {str(e)}"}


def check_json_readable(path: Path) -> Dict[str, Any]:
    """Check if a JSON file is structurally valid."""
    base_check = check_file_exists_and_nonempty(path)
    if not base_check["valid"]:
        return base_check

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not data:
            return {"valid": False, "exists": True, "empty": True, "error": "JSON is empty or null"}

        return {"valid": True, "exists": True, "empty": False, "type": type(data).__name__}
    except Exception as e:
        return {"valid": False, "exists": True, "empty": False, "error": f"Failed to parse JSON: {str(e)}"}


def check_parquet_readable(path: Path) -> Dict[str, Any]:
    """Check if a Parquet file is structurally readable."""
    base_check = check_file_exists_and_nonempty(path)
    if not base_check["valid"]:
        return base_check

    try:
        # Read just metadata/schema if possible to save memory, or head
        import pyarrow.parquet as pq
        meta = pq.read_metadata(path)

        if meta.num_rows == 0:
            return {"valid": False, "exists": True, "empty": True, "error": "Parquet file has 0 rows"}

        return {
            "valid": True,
            "exists": True,
            "empty": False,
            "num_rows": meta.num_rows,
            "num_columns": meta.num_columns
        }
    except ImportError:
        try:
            df = pd.read_parquet(path)
            if df.empty:
                return {"valid": False, "exists": True, "empty": True, "error": "Parquet file has 0 rows"}
            return {"valid": True, "exists": True, "empty": False, "num_rows": len(df), "num_columns": len(df.columns)}
        except Exception as e:
            return {"valid": False, "exists": True, "empty": False, "error": f"Failed to read parquet via pandas: {str(e)}"}
    except Exception as e:
        return {"valid": False, "exists": True, "empty": False, "error": f"Failed to read parquet metadata: {str(e)}"}


def check_dataframe_schema(df: pd.DataFrame, required_columns: List[str]) -> Dict[str, Any]:
    """Check if a dataframe contains required columns and has no duplicates."""
    if df.empty:
        return {"valid": False, "error": "DataFrame is empty"}

    missing = [c for c in required_columns if c not in df.columns]

    # Check for duplicate column names
    duplicates = df.columns[df.columns.duplicated()].tolist()

    if missing or duplicates:
        errs = []
        if missing:
            errs.append(f"Missing columns: {missing}")
        if duplicates:
            errs.append(f"Duplicate columns: {duplicates}")

        return {
            "valid": False,
            "error": "; ".join(errs),
            "missing_columns": missing,
            "duplicate_columns": duplicates
        }

    return {"valid": True, "missing_columns": [], "duplicate_columns": []}


def build_artifact_integrity_report(data_lake: DataLake, artifact_paths: Optional[List[Path]] = None) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a report on the integrity of key artifacts."""

    if not artifact_paths:
        # Discover some key artifacts automatically if none provided
        artifact_paths = []

        # Add some sample manifests or journals
        if hasattr(data_lake.paths, 'LAKE_MANIFESTS_DIR'):
            artifact_paths.extend(list(data_lake.paths.LAKE_MANIFESTS_DIR.rglob("*.json"))[:10])

        if hasattr(data_lake.paths, 'LAKE_PROCESSED_OHLCV_DIR'):
            # Grab a few parquet files across timeframes
            for tf_dir in data_lake.paths.LAKE_PROCESSED_OHLCV_DIR.iterdir():
                if tf_dir.is_dir():
                    artifact_paths.extend(list(tf_dir.glob("*.parquet"))[:5])

    rows = []

    for path in artifact_paths:
        ext = path.suffix.lower()

        if ext == '.csv':
            result = check_csv_readable(path)
        elif ext == '.json':
            result = check_json_readable(path)
        elif ext in ['.parquet', '.pq']:
            result = check_parquet_readable(path)
        else:
            result = check_file_exists_and_nonempty(path)

        rows.append({
            "path": str(path),
            "filename": path.name,
            "extension": ext,
            "valid": result.get("valid", False),
            "exists": result.get("exists", False),
            "empty": result.get("empty", True),
            "error": result.get("error", "")
        })

    df = pd.DataFrame(rows)

    if df.empty:
        summary = {
            "total_checked": 0,
            "valid_count": 0,
            "invalid_count": 0,
            "status": "unknown"
        }
        return df, summary

    valid_count = int(sum(df["valid"]))
    invalid_count = len(df) - valid_count

    overall_status = "healthy" if invalid_count == 0 else "critical"

    summary = {
        "total_checked": len(df),
        "valid_count": valid_count,
        "invalid_count": invalid_count,
        "missing_count": int(sum(~df["exists"])),
        "empty_count": int(sum(df["empty"] & df["exists"])),
        "status": overall_status
    }

    return df, summary
