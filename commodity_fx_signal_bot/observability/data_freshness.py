"""
Data freshness diagnostics for monitoring staleness of data artifacts.
"""

from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Tuple, List, Optional

import pandas as pd

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake


def calculate_file_age_hours(path: Path) -> Optional[float]:
    """Calculate the age of a file in hours."""
    if not path.exists():
        return None

    mtime = path.stat().st_mtime
    now = datetime.now(timezone.utc).timestamp()

    age_seconds = now - mtime
    return max(0.0, age_seconds / 3600.0)


def check_dataframe_freshness(df: pd.DataFrame, max_stale_hours: Optional[float] = None) -> Dict[str, Any]:
    """Check the freshness of a DataFrame based on its index or typical timestamp columns."""
    if df.empty:
        return {"fresh": False, "reason": "DataFrame is empty", "age_hours": None}

    latest_time = None

    # Try index first
    if isinstance(df.index, pd.DatetimeIndex):
        latest_time = df.index.max()
    elif 'timestamp' in df.columns:
        latest_time = pd.to_datetime(df['timestamp']).max()
    elif 'date' in df.columns:
        latest_time = pd.to_datetime(df['date']).max()

    if latest_time is None:
        return {"fresh": False, "reason": "Could not determine latest timestamp", "age_hours": None}

    # Ensure UTC for comparison
    if latest_time.tzinfo is None:
        latest_time = latest_time.tz_localize('UTC')

    now = datetime.now(timezone.utc)
    age_hours = max(0.0, (now - latest_time).total_seconds() / 3600.0)

    is_fresh = True
    if max_stale_hours is not None:
        is_fresh = age_hours <= max_stale_hours

    return {
        "fresh": is_fresh,
        "age_hours": age_hours,
        "latest_timestamp": latest_time.isoformat(),
        "reason": "Within threshold" if is_fresh else "Exceeded threshold"
    }


def check_feature_file_freshness(path: Path, max_stale_hours: float) -> Dict[str, Any]:
    """Check freshness of a specific feature file."""
    age_hours = calculate_file_age_hours(path)

    if age_hours is None:
        return {
            "exists": False,
            "modified_time": None,
            "age_hours": None,
            "stale": True,
            "status": "missing",
            "warnings": [f"File missing: {path.name}"]
        }

    is_stale = age_hours > max_stale_hours
    status = "stale" if is_stale else "fresh"

    warnings = []
    if is_stale:
        warnings.append(f"Data is {age_hours:.1f} hours old, exceeds threshold of {max_stale_hours}h")

    return {
        "exists": True,
        "modified_time": datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
        "age_hours": age_hours,
        "stale": is_stale,
        "status": status,
        "warnings": warnings
    }


def build_data_freshness_report(
    data_lake: DataLake,
    symbols: Optional[List[SymbolSpec]] = None,
    timeframe: str = "1d",
    max_stale_hours: float = 48.0
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a comprehensive report on data freshness across all key pipelines."""

    if symbols is None:
        from config.symbols import ALL_SYMBOLS
        symbols = [s for s in ALL_SYMBOLS if s.enabled]

    rows = []

    artifact_types = [
        ("processed_ohlcv", data_lake.paths.LAKE_PROCESSED_OHLCV_DIR),
        ("technical_features", data_lake.paths.LAKE_FEATURES_TECHNICAL_DIR),
        ("strategy_pool", data_lake.paths.LAKE_DIR / "strategy_candidates" / "pool"),
    ]

    for spec in symbols:
        safe_symbol = DataLake.safe_symbol_name(spec.symbol)

        for artifact_name, base_dir in artifact_types:
            path = base_dir / timeframe / f"{safe_symbol}.parquet"
            check_result = check_feature_file_freshness(path, max_stale_hours)

            rows.append({
                "symbol": spec.symbol,
                "timeframe": timeframe,
                "artifact_type": artifact_name,
                "path": str(path),
                "exists": check_result["exists"],
                "modified_time": check_result["modified_time"],
                "age_hours": check_result["age_hours"],
                "stale": check_result["stale"],
                "status": check_result["status"],
                "warnings": check_result["warnings"]
            })

    df = pd.DataFrame(rows)

    if df.empty:
        summary = {
            "total_artifacts_checked": 0,
            "missing_count": 0,
            "stale_count": 0,
            "fresh_count": 0,
            "avg_age_hours": 0.0,
            "status": "unknown"
        }
        return df, summary

    missing_count = int(sum(~df["exists"]))
    stale_count = int(sum(df["stale"] & df["exists"]))
    fresh_count = int(sum(~df["stale"] & df["exists"]))
    avg_age = float(df["age_hours"].mean()) if not df["age_hours"].isna().all() else 0.0

    overall_status = "healthy"
    if missing_count > 0 or stale_count > 0:
        overall_status = "degraded"

    summary = {
        "total_artifacts_checked": len(df),
        "missing_count": missing_count,
        "stale_count": stale_count,
        "fresh_count": fresh_count,
        "avg_age_hours": avg_age,
        "threshold_hours": max_stale_hours,
        "status": overall_status
    }

    return df, summary
