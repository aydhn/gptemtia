import math
import pandas as pd
from typing import List, Tuple, Dict, Optional

from .performance_config import PerformanceProfile
from .performance_models import BatchPlan, build_batch_plan_id

def calculate_safe_batch_size(
    total_items: int,
    profile: PerformanceProfile,
    item_cost_estimate_mb: Optional[float] = None
) -> int:
    # Use max_batch_symbols from profile as base
    safe_size = profile.max_batch_symbols

    # If we have memory estimates, we could lower the batch size
    if item_cost_estimate_mb and item_cost_estimate_mb > 0:
        max_items_by_mem = int(profile.max_memory_mb_per_script / item_cost_estimate_mb)
        if max_items_by_mem > 0:
            safe_size = min(safe_size, max_items_by_mem)

    # Always ensure at least 1, but no more than total_items
    safe_size = max(1, min(safe_size, total_items))
    return safe_size

def build_symbol_batch_plan(
    symbols: List[str],
    module_name: str,
    profile: PerformanceProfile
) -> BatchPlan:

    total = len(symbols)
    if total == 0:
        return BatchPlan(
            plan_id=build_batch_plan_id(f"{module_name}_empty", module_name),
            plan_name=f"{module_name}_batch_plan",
            module_name=module_name,
            total_items=0,
            batch_size=profile.max_batch_symbols,
            batch_count=0,
            max_parallel_workers=profile.max_parallel_workers,
            checkpoint_every_items=profile.checkpoint_every_items,
            estimated_runtime_seconds=0.0,
            warnings=["Empty symbol list"]
        )

    safe_size = calculate_safe_batch_size(total, profile)
    batch_count = math.ceil(total / safe_size)

    return BatchPlan(
        plan_id=build_batch_plan_id(f"{module_name}_plan", module_name),
        plan_name=f"{module_name}_batch_plan",
        module_name=module_name,
        total_items=total,
        batch_size=safe_size,
        batch_count=batch_count,
        max_parallel_workers=profile.max_parallel_workers,
        checkpoint_every_items=profile.checkpoint_every_items,
        estimated_runtime_seconds=None, # Needs historical data to estimate
        warnings=[]
    )

def build_module_batch_plans(
    module_items: Dict[str, List[str]],
    profile: PerformanceProfile
) -> Tuple[pd.DataFrame, Dict]:

    plans = []
    for mod, items in module_items.items():
        plan = build_symbol_batch_plan(items, mod, profile)
        plans.append(plan)

    import dataclasses
    df = pd.DataFrame([dataclasses.asdict(p) for p in plans])
    summary = summarize_batch_plans(df)

    return df, summary

def estimate_batch_runtime_seconds(batch_count: int, avg_runtime_per_batch: Optional[float] = None) -> Optional[float]:
    if avg_runtime_per_batch is None:
        return None
    return batch_count * avg_runtime_per_batch

def summarize_batch_plans(batch_df: pd.DataFrame) -> dict:
    if batch_df.empty:
        return {"total_plans": 0, "total_batches": 0}

    return {
        "total_plans": len(batch_df),
        "total_batches": batch_df["batch_count"].sum() if "batch_count" in batch_df.columns else 0
    }
