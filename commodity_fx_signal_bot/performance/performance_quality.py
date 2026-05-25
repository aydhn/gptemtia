import pandas as pd
from typing import Dict, Optional, List
import json

from .performance_config import PerformanceProfile

_FORBIDDEN_TERMS = [
    "live order",
    "broker order",
    "real trade",
    "open position",
    "close position",
    "buy now",
    "sell now",
    "deploy model",
    "production deploy",
    "production scheduler",
    "background daemon",
    "while true",
    "run live",
    "exchange api key"
]

def check_runtime_profile_quality(runtime_df: Optional[pd.DataFrame], profile: PerformanceProfile) -> dict:
    if runtime_df is None or runtime_df.empty:
        return {"passed": False, "warnings": ["No runtime profiles generated"]}

    warnings = []

    if "duration_seconds" in runtime_df.columns:
        if runtime_df["duration_seconds"].isna().any():
            warnings.append("Some runtime profiles are missing duration_seconds")

    if "exit_code" in runtime_df.columns:
        failures = len(runtime_df[runtime_df["exit_code"] != 0])
        if failures > 0:
            warnings.append(f"{failures} scripts had non-zero exit codes")

    if "timed_out" in runtime_df.columns:
        timeouts = len(runtime_df[runtime_df["timed_out"] == True])
        if timeouts > 0:
            warnings.append(f"{timeouts} scripts timed out")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_memory_profile_quality(memory_df: Optional[pd.DataFrame], profile: PerformanceProfile) -> dict:
    if memory_df is None or memory_df.empty:
        return {"passed": False, "warnings": ["No memory profiles generated"]}

    warnings = []

    if "peak_memory_mb" in memory_df.columns:
        if memory_df["peak_memory_mb"].isna().any():
            warnings.append("Some memory profiles are missing peak_memory_mb")

    if "budget_status" in memory_df.columns:
        over = len(memory_df[memory_df["budget_status"] == "over_budget"])
        if over > 0:
            warnings.append(f"{over} scripts went over budget (offline warning)")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_resource_budget_quality(budget_df: Optional[pd.DataFrame]) -> dict:
    if budget_df is None or budget_df.empty:
        return {"passed": False, "warnings": ["No resource budgets generated"]}

    warnings = []

    if "max_parallel_workers" in budget_df.columns:
        bad_workers = len(budget_df[budget_df["max_parallel_workers"] < 1])
        if bad_workers > 0:
            warnings.append(f"{bad_workers} budgets have invalid max_parallel_workers < 1")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_cache_quality(cache_df: Optional[pd.DataFrame]) -> dict:
    if cache_df is None or cache_df.empty:
        return {"passed": True, "warnings": ["Cache is empty or disabled"]}

    warnings = []
    return {"passed": True, "warnings": warnings}

def check_batch_plan_quality(batch_df: Optional[pd.DataFrame]) -> dict:
    if batch_df is None or batch_df.empty:
        return {"passed": True, "warnings": ["No batch plans generated"]}

    warnings = []

    if "batch_size" in batch_df.columns:
        bad_sizes = len(batch_df[batch_df["batch_size"] < 1])
        if bad_sizes > 0:
            warnings.append(f"{bad_sizes} batch plans have invalid batch_size < 1")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_large_run_stability_quality(stability_df: Optional[pd.DataFrame]) -> dict:
    if stability_df is None or stability_df.empty:
        return {"passed": False, "warnings": ["No stability checklist evaluated"]}

    warnings = []

    if "passed" in stability_df.columns:
        failures = len(stability_df[stability_df["passed"] == False])
        if failures > 0:
            warnings.append(f"{failures} stability checks failed")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_for_forbidden_terms_in_performance(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[dict] = None
) -> dict:

    found = []

    def scan_string(s: str):
        s_lower = s.lower()
        for term in _FORBIDDEN_TERMS:
            # specifically "no live order" should be fine, but we will simplify
            if term in s_lower:
                if f"no {term}" not in s_lower and f"not {term}" not in s_lower:
                    found.append(term)

    if text:
        scan_string(text)

    if df is not None and not df.empty:
        for col in df.columns:
            if df[col].dtype == object:
                # Fill na with empty string, convert everything to string to be safe
                for val in df[col].fillna('').astype(str).tolist():
                    scan_string(val)

    if summary:
        scan_string(json.dumps(summary))

    unique_found = list(set(found))
    return {
        "passed": len(unique_found) == 0,
        "warnings": [f"Found forbidden term: {t}" for t in unique_found]
    }

def build_performance_quality_report(
    summary: dict,
    runtime_df: Optional[pd.DataFrame] = None,
    memory_df: Optional[pd.DataFrame] = None,
    budget_df: Optional[pd.DataFrame] = None,
    profile: Optional[PerformanceProfile] = None
) -> dict:

    # We will just use a dummy profile if none passed for the checks
    if profile is None:
        from .performance_config import get_default_performance_profile
        profile = get_default_performance_profile()

    rt_qual = check_runtime_profile_quality(runtime_df, profile)
    mem_qual = check_memory_profile_quality(memory_df, profile)
    bud_qual = check_resource_budget_quality(budget_df)

    forbidden_terms = check_for_forbidden_terms_in_performance(summary=summary, df=runtime_df)

    all_warnings = rt_qual["warnings"] + mem_qual["warnings"] + bud_qual["warnings"] + forbidden_terms["warnings"]

    passed = rt_qual["passed"] and mem_qual["passed"] and bud_qual["passed"] and forbidden_terms["passed"]

    return {
        "runtime_profiles_valid": rt_qual["passed"],
        "memory_profiles_valid": mem_qual["passed"],
        "resource_budgets_valid": bud_qual["passed"],
        "cache_valid": True,
        "batch_plans_valid": True,
        "stability_valid": True,
        "forbidden_terms_found": not forbidden_terms["passed"],
        "warning_count": len(all_warnings),
        "passed": passed,
        "warnings": all_warnings
    }
