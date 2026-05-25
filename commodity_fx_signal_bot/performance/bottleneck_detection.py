import pandas as pd
from typing import Tuple, Dict, Optional

from .performance_config import PerformanceProfile

def detect_runtime_bottlenecks(runtime_df: pd.DataFrame, profile: PerformanceProfile) -> pd.DataFrame:
    if runtime_df.empty:
        return pd.DataFrame()

    bottlenecks = []

    for _, row in runtime_df.iterrows():
        duration = row.get("duration_seconds")
        if pd.isna(duration):
            continue

        if duration > profile.max_runtime_seconds_per_script * 0.9:
            bottlenecks.append({
                "module_name": row.get("module_name", "unknown"),
                "bottleneck_type": "runtime_bottleneck",
                "severity": "high",
                "details": f"Runtime {duration:.2f}s is very close to or over limit {profile.max_runtime_seconds_per_script}s"
            })
        elif duration > profile.max_runtime_seconds_per_script * 0.5:
            bottlenecks.append({
                "module_name": row.get("module_name", "unknown"),
                "bottleneck_type": "runtime_bottleneck",
                "severity": "medium",
                "details": f"Runtime {duration:.2f}s is > 50% of limit {profile.max_runtime_seconds_per_script}s"
            })

    return pd.DataFrame(bottlenecks)

def detect_memory_bottlenecks(memory_df: pd.DataFrame, profile: PerformanceProfile) -> pd.DataFrame:
    if memory_df.empty:
        return pd.DataFrame()

    bottlenecks = []

    for _, row in memory_df.iterrows():
        peak = row.get("peak_memory_mb")
        if pd.isna(peak):
            continue

        if peak > profile.max_memory_mb_per_script * 0.9:
            bottlenecks.append({
                "module_name": row.get("module_name", "unknown"),
                "bottleneck_type": "memory_bottleneck",
                "severity": "high",
                "details": f"Peak memory {peak:.2f}MB is very close to or over limit {profile.max_memory_mb_per_script}MB"
            })
        elif peak > profile.max_memory_mb_per_script * 0.5:
            bottlenecks.append({
                "module_name": row.get("module_name", "unknown"),
                "bottleneck_type": "memory_bottleneck",
                "severity": "medium",
                "details": f"Peak memory {peak:.2f}MB is > 50% of limit {profile.max_memory_mb_per_script}MB"
            })

    return pd.DataFrame(bottlenecks)

def detect_cache_bottlenecks(cache_df: Optional[pd.DataFrame]) -> pd.DataFrame:
    if cache_df is None or cache_df.empty:
        return pd.DataFrame()

    bottlenecks = []

    # Example heuristic: Too many cache invalidations
    if "status" in cache_df.columns:
        invalid_count = len(cache_df[cache_df["status"] == "invalid"])
        if invalid_count > len(cache_df) * 0.5 and len(cache_df) > 5:
            bottlenecks.append({
                "module_name": "cache_system",
                "bottleneck_type": "cache_bottleneck",
                "severity": "medium",
                "details": "High cache invalidation rate (>50%), reducing cache effectiveness"
            })

    return pd.DataFrame(bottlenecks)

def detect_io_bottlenecks(inventory_df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
    if inventory_df is None or inventory_df.empty:
        return pd.DataFrame()

    bottlenecks = []

    if "size_bytes" in inventory_df.columns:
        total_size = inventory_df["size_bytes"].sum() / (1024 * 1024)
        if total_size > 5000: # 5GB
            bottlenecks.append({
                "module_name": "data_lake",
                "bottleneck_type": "io_bottleneck",
                "severity": "medium",
                "details": f"Total cache/inventory size is large ({total_size:.2f}MB), potential IO slowdowns"
            })

    return pd.DataFrame(bottlenecks)

def build_bottleneck_report(
    runtime_df: Optional[pd.DataFrame],
    memory_df: Optional[pd.DataFrame],
    cache_df: Optional[pd.DataFrame],
    profile: PerformanceProfile
) -> Tuple[pd.DataFrame, Dict]:

    dfs = []

    if runtime_df is not None and not runtime_df.empty:
        dfs.append(detect_runtime_bottlenecks(runtime_df, profile))

    if memory_df is not None and not memory_df.empty:
        dfs.append(detect_memory_bottlenecks(memory_df, profile))

    if cache_df is not None and not cache_df.empty:
        dfs.append(detect_cache_bottlenecks(cache_df))

    valid_dfs = [df for df in dfs if not df.empty]

    if not valid_dfs:
        df = pd.DataFrame(columns=["module_name", "bottleneck_type", "severity", "details"])
    else:
        df = pd.concat(valid_dfs, ignore_index=True)

    summary = {
        "total_bottlenecks": len(df),
        "high_severity": len(df[df["severity"] == "high"]) if not df.empty else 0,
        "medium_severity": len(df[df["severity"] == "medium"]) if not df.empty else 0
    }

    return df, summary
