import tracemalloc
import time
import pandas as pd
from typing import Callable, Tuple, Dict, Any, Optional

try:
    import psutil
    import os
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

from .performance_models import MemoryProfileRecord, build_runtime_profile_id

def get_current_process_memory_mb() -> Optional[float]:
    if PSUTIL_AVAILABLE:
        process = psutil.Process(os.getpid())
        mem_info = process.memory_info()
        return mem_info.rss / (1024 * 1024)
    return None

def profile_function_memory(func: Callable, command_name: str, module_name: str, max_memory_mb: int, *args, **kwargs) -> Tuple[Any, MemoryProfileRecord]:
    start_memory = get_current_process_memory_mb()

    tracemalloc.start()

    start_time = datetime.now(timezone.utc).isoformat() if 'datetime' in globals() else "2023-01-01" # Mock if not imported

    result = func(*args, **kwargs)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    peak_mb = peak / (1024 * 1024)
    end_memory = get_current_process_memory_mb()

    memory_delta_mb = None
    if start_memory is not None and end_memory is not None:
        memory_delta_mb = end_memory - start_memory

    budget_status = classify_memory_budget_status(peak_mb, max_memory_mb)

    warnings = []
    if not PSUTIL_AVAILABLE:
        warnings.append("psutil not available, using tracemalloc only.")
    if budget_status == "over_budget":
        warnings.append(f"Memory over budget: Peak {peak_mb:.2f}MB > {max_memory_mb}MB limit")

    record = MemoryProfileRecord(
        profile_id=build_runtime_profile_id(command_name, "now"),
        command_name=command_name,
        module_name=module_name,
        peak_memory_mb=peak_mb,
        start_memory_mb=start_memory,
        end_memory_mb=end_memory,
        memory_delta_mb=memory_delta_mb,
        budget_status=budget_status,
        warnings=warnings
    )

    return result, record

def estimate_dataframe_memory_mb(df: pd.DataFrame) -> float:
    return df.memory_usage(deep=True).sum() / (1024 * 1024)

def build_memory_profile_table(dataframes: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    records = []
    for name, df in dataframes.items():
        records.append({
            "dataframe_name": name,
            "estimated_memory_mb": estimate_dataframe_memory_mb(df),
            "rows": len(df),
            "columns": len(df.columns)
        })
    return pd.DataFrame(records)

def classify_memory_budget_status(peak_memory_mb: Optional[float], max_memory_mb: int) -> str:
    if peak_memory_mb is None:
        return "budget_unknown"

    if peak_memory_mb > max_memory_mb:
        return "over_budget"
    elif peak_memory_mb > max_memory_mb * 0.8:
        return "near_budget_limit"
    else:
        return "within_budget"

def summarize_memory_profiles(memory_df: pd.DataFrame) -> dict:
    if memory_df.empty:
        return {"total_profiles": 0, "avg_peak_memory_mb": 0.0, "over_budget_count": 0}

    return {
        "total_profiles": len(memory_df),
        "avg_peak_memory_mb": memory_df["peak_memory_mb"].mean() if "peak_memory_mb" in memory_df.columns else 0.0,
        "over_budget_count": len(memory_df[memory_df["budget_status"] == "over_budget"]) if "budget_status" in memory_df.columns else 0
    }
