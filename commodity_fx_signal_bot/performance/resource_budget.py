import pandas as pd
from typing import List, Tuple, Dict, Optional

from .performance_config import PerformanceProfile
from .performance_models import ResourceBudget, build_resource_budget_id

_MODULE_NAMES = [
    "research_reports",
    "portfolio_research",
    "portfolio_regime",
    "synthetic_indices",
    "factor_research",
    "meta_research",
    "experiments",
    "governance",
    "research_planning",
    "knowledge_base",
    "command_center",
    "quality_gates",
    "performance"
]

def build_default_resource_budgets(profile: PerformanceProfile) -> List[ResourceBudget]:
    budgets = []
    for mod in _MODULE_NAMES:
        budget = ResourceBudget(
            budget_id=build_resource_budget_id(mod, profile.name),
            module_name=mod,
            max_runtime_seconds=profile.max_runtime_seconds_per_script,
            max_memory_mb=profile.max_memory_mb_per_script,
            max_batch_symbols=profile.max_batch_symbols,
            max_parallel_workers=profile.max_parallel_workers,
            cache_enabled=profile.enable_cache,
            checkpointing_enabled=profile.enable_checkpointing,
            warnings=[]
        )
        budgets.append(budget)
    return budgets

def resource_budgets_to_dataframe(budgets: List[ResourceBudget]) -> pd.DataFrame:
    import dataclasses
    return pd.DataFrame([dataclasses.asdict(b) for b in budgets])

def check_runtime_against_budget(runtime_df: pd.DataFrame, budgets_df: pd.DataFrame) -> pd.DataFrame:
    if runtime_df.empty or budgets_df.empty:
        return pd.DataFrame()

    merged = pd.merge(runtime_df, budgets_df, on="module_name", how="left")

    def check_limit(row):
        if pd.isna(row["duration_seconds"]) or pd.isna(row["max_runtime_seconds"]):
            return "unknown"
        if row["duration_seconds"] > row["max_runtime_seconds"]:
            return "over_budget"
        if row["duration_seconds"] > row["max_runtime_seconds"] * 0.8:
            return "near_budget_limit"
        return "within_budget"

    merged["runtime_budget_status"] = merged.apply(check_limit, axis=1)

    # Return violations
    return merged[merged["runtime_budget_status"] == "over_budget"]

def check_memory_against_budget(memory_df: pd.DataFrame, budgets_df: pd.DataFrame) -> pd.DataFrame:
    if memory_df.empty or budgets_df.empty:
        return pd.DataFrame()

    merged = pd.merge(memory_df, budgets_df, on="module_name", how="left")

    # Budget status is already in memory_df ideally, but we can verify against specific module budget
    def check_limit(row):
        if pd.isna(row["peak_memory_mb"]) or pd.isna(row["max_memory_mb"]):
            return "unknown"
        if row["peak_memory_mb"] > row["max_memory_mb"]:
            return "over_budget"
        if row["peak_memory_mb"] > row["max_memory_mb"] * 0.8:
            return "near_budget_limit"
        return "within_budget"

    merged["memory_budget_status"] = merged.apply(check_limit, axis=1)

    # Return violations
    return merged[merged["memory_budget_status"] == "over_budget"]

def build_resource_budget_violation_report(
    runtime_df: Optional[pd.DataFrame],
    memory_df: Optional[pd.DataFrame],
    budgets_df: pd.DataFrame
) -> Tuple[pd.DataFrame, Dict]:

    violations = []

    if runtime_df is not None and not runtime_df.empty:
        r_violations = check_runtime_against_budget(runtime_df, budgets_df)
        if not r_violations.empty:
            for _, row in r_violations.iterrows():
                violations.append({
                    "module_name": row["module_name"],
                    "violation_type": "runtime",
                    "value": row["duration_seconds"],
                    "limit": row["max_runtime_seconds"]
                })

    if memory_df is not None and not memory_df.empty:
        m_violations = check_memory_against_budget(memory_df, budgets_df)
        if not m_violations.empty:
            for _, row in m_violations.iterrows():
                violations.append({
                    "module_name": row["module_name"],
                    "violation_type": "memory",
                    "value": row["peak_memory_mb"],
                    "limit": row["max_memory_mb"]
                })

    v_df = pd.DataFrame(violations)

    summary = {
        "total_violations": len(v_df),
        "runtime_violations": len(v_df[v_df["violation_type"] == "runtime"]) if not v_df.empty else 0,
        "memory_violations": len(v_df[v_df["violation_type"] == "memory"]) if not v_df.empty else 0
    }

    return v_df, summary

def summarize_resource_budgets(budgets_df: pd.DataFrame) -> dict:
    if budgets_df.empty:
        return {"total_budgets": 0, "avg_runtime_limit": 0, "avg_memory_limit": 0}

    return {
        "total_budgets": len(budgets_df),
        "avg_runtime_limit": budgets_df["max_runtime_seconds"].mean() if "max_runtime_seconds" in budgets_df.columns else 0,
        "avg_memory_limit": budgets_df["max_memory_mb"].mean() if "max_memory_mb" in budgets_df.columns else 0
    }
