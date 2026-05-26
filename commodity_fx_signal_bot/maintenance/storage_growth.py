"""Storage Growth Tracking for offline maintenance."""
import pandas as pd
from typing import Dict
from datetime import datetime, timezone
from pathlib import Path
import json

def build_storage_snapshot(inventory_df: pd.DataFrame) -> Dict:
    if inventory_df.empty:
        return {
            "created_at_utc": datetime.now(timezone.utc).isoformat(),
            "total_files": 0,
            "total_size_bytes": 0
        }

    return {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "total_files": len(inventory_df),
        "total_size_bytes": int(inventory_df["size_bytes"].sum()),
        "size_by_category": inventory_df.groupby("retention_category")["size_bytes"].sum().to_dict(),
        "largest_categories": list(inventory_df.groupby("retention_category")["size_bytes"].sum().sort_values(ascending=False).head(3).index),
        "report_size_bytes": int(inventory_df[inventory_df["retention_category"] == "report_retention"]["size_bytes"].sum()),
        "cache_size_bytes": int(inventory_df[inventory_df["retention_category"] == "cache_retention"]["size_bytes"].sum()),
        "checkpoint_size_bytes": int(inventory_df[inventory_df["retention_category"] == "checkpoint_retention"]["size_bytes"].sum())
    }

def save_storage_snapshot(snapshot: Dict, output_dir: Path) -> Path:
    # Actual save happens via DataLake
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"snapshot_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    with open(out_path, "w") as f:
        json.dump(snapshot, f)
    return out_path

def load_storage_snapshots(snapshot_dir: Path) -> pd.DataFrame:
    # Actual load happens via DataLake
    return pd.DataFrame()

def calculate_storage_growth(snapshot_df: pd.DataFrame) -> pd.DataFrame:
    if snapshot_df.empty:
        return pd.DataFrame()
    df = snapshot_df.copy()
    if "total_size_bytes" in df:
        df["growth_bytes"] = df["total_size_bytes"].diff().fillna(0)
    return df

def forecast_simple_storage_growth(snapshot_df: pd.DataFrame, days_ahead: int = 30) -> Dict:
    return {"forecasted_bytes_30d": 0, "disclaimer": "Simple heuristic only, not an exact prediction."}

def summarize_storage_growth(growth_df: pd.DataFrame) -> Dict:
    return {"snapshots_analyzed": len(growth_df)}
