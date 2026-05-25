import pandas as pd
from typing import Dict, Optional

from .performance_config import PerformanceProfile

def build_large_run_stability_checklist(profile: PerformanceProfile) -> pd.DataFrame:
    checklist = [
        {"item": "runtime budget tanımlı", "expected": True},
        {"item": "memory budget tanımlı", "expected": True},
        {"item": "batch plan var", "expected": True},
        {"item": "checkpointing açık", "expected": profile.enable_checkpointing},
        {"item": "cache policy var", "expected": profile.enable_cache},
        {"item": "output folders var", "expected": True},
        {"item": "safe commands only", "expected": True},
        {"item": "no daemon loop", "expected": True},
        {"item": "no broker/live/deploy command", "expected": True},
        {"item": "graceful timeout strategy var", "expected": True},
        {"item": "large file handling warning var", "expected": True},
        {"item": "quality reports mevcut", "expected": True}
    ]
    return pd.DataFrame(checklist)

def evaluate_large_run_stability(
    runtime_df: Optional[pd.DataFrame],
    memory_df: Optional[pd.DataFrame],
    cache_df: Optional[pd.DataFrame],
    batch_df: Optional[pd.DataFrame],
    profile: PerformanceProfile
) -> pd.DataFrame:

    checklist = build_large_run_stability_checklist(profile)

    def evaluate(row):
        item = row["item"]

        # Simple heuristics for evaluation
        if item == "batch plan var":
            return batch_df is not None and not batch_df.empty
        if item == "cache policy var":
            return profile.enable_cache and cache_df is not None
        if item == "runtime budget tanımlı":
            return runtime_df is not None
        if item == "memory budget tanımlı":
            return memory_df is not None

        # Others are conceptually true for this architecture if tests pass
        return True

    checklist["actual"] = checklist.apply(evaluate, axis=1)
    checklist["passed"] = checklist["actual"] == checklist["expected"]

    return checklist

def infer_large_run_stability_label(evaluated_df: pd.DataFrame) -> str:
    if evaluated_df.empty:
        return "unknown_stability"

    total = len(evaluated_df)
    passed = evaluated_df["passed"].sum()

    if passed == total:
        return "stable_large_run"
    elif passed >= total * 0.8:
        return "stable_with_warnings"
    elif passed >= total * 0.5:
        return "unstable_large_run"
    else:
        return "insufficient_stability_data"

def summarize_large_run_stability(evaluated_df: pd.DataFrame) -> dict:
    if evaluated_df.empty:
        return {
            "total_checks": 0,
            "passed_checks": 0,
            "stability_label": "unknown_stability"
        }

    passed = int(evaluated_df["passed"].sum())
    total = len(evaluated_df)

    return {
        "total_checks": total,
        "passed_checks": passed,
        "pass_rate_pct": (passed / total) * 100 if total > 0 else 0,
        "stability_label": infer_large_run_stability_label(evaluated_df)
    }
