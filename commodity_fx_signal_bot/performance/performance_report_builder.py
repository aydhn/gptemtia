import pandas as pd
from typing import Optional

def build_performance_disclaimer() -> str:
    return (
        "**ÖNEMLİ UYARI:**\n\n"
        "Bu çıktı offline performance profiling/resource budgeting raporudur. "
        "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, "
        "production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"
    )

def build_performance_profile_markdown_report(
    summary: dict,
    runtime_df: Optional[pd.DataFrame] = None,
    memory_df: Optional[pd.DataFrame] = None
) -> str:
    md = "# Performance Profile Report\n\n"
    md += build_performance_disclaimer()

    md += "## 1. Summary\n"
    for k, v in summary.items():
        md += f"- **{k}**: {v}\n"
    md += "\n"

    if runtime_df is not None and not runtime_df.empty:
        md += "## 2. Runtime Profiles\n"
        md += runtime_df.to_markdown(index=False)
        md += "\n\n"

    if memory_df is not None and not memory_df.empty:
        md += "## 3. Memory Profiles\n"
        md += memory_df.to_markdown(index=False)
        md += "\n\n"

    return md

def build_resource_budget_markdown_report(
    summary: dict,
    budget_df: pd.DataFrame,
    violation_df: Optional[pd.DataFrame] = None
) -> str:
    md = "# Resource Budget Report\n\n"
    md += build_performance_disclaimer()

    md += "## 1. Budget Summary\n"
    for k, v in summary.items():
        md += f"- **{k}**: {v}\n"
    md += "\n"

    if not budget_df.empty:
        md += "## 2. Defined Budgets\n"
        md += budget_df.to_markdown(index=False)
        md += "\n\n"

    if violation_df is not None and not violation_df.empty:
        md += "## 3. Budget Violations (Offline Warnings)\n"
        md += violation_df.to_markdown(index=False)
        md += "\n\n"
    else:
        md += "## 3. Budget Violations\n"
        md += "No violations detected.\n\n"

    return md

def build_cache_strategy_markdown_report(
    summary: dict,
    cache_df: Optional[pd.DataFrame] = None,
    policy_df: Optional[pd.DataFrame] = None
) -> str:
    md = "# Cache Strategy Report\n\n"
    md += build_performance_disclaimer()

    md += "## 1. Cache Summary\n"
    for k, v in summary.items():
        md += f"- **{k}**: {v}\n"
    md += "\n"

    if policy_df is not None and not policy_df.empty:
        md += "## 2. Cache Policies\n"
        md += policy_df.to_markdown(index=False)
        md += "\n\n"

    if cache_df is not None and not cache_df.empty:
        md += "## 3. Tracked Caches\n"
        md += cache_df.to_markdown(index=False)
        md += "\n\n"

    return md

def build_large_run_stability_markdown_report(
    summary: dict,
    stability_df: Optional[pd.DataFrame] = None
) -> str:
    md = "# Large-Run Stability Report\n\n"
    md += build_performance_disclaimer()

    md += "## 1. Stability Summary\n"
    for k, v in summary.items():
        md += f"- **{k}**: {v}\n"
    md += "\n"

    if stability_df is not None and not stability_df.empty:
        md += "## 2. Stability Checklist\n"
        md += stability_df.to_markdown(index=False)
        md += "\n\n"

    return md

def build_runtime_optimization_markdown_report(
    summary: dict,
    recommendation_df: Optional[pd.DataFrame] = None
) -> str:
    md = "# Runtime Optimization Report\n\n"
    md += build_performance_disclaimer()

    md += "## 1. Optimization Summary\n"
    for k, v in summary.items():
        md += f"- **{k}**: {v}\n"
    md += "\n"

    if recommendation_df is not None and not recommendation_df.empty:
        md += "## 2. Safe Optimization Recommendations\n"
        md += recommendation_df.to_markdown(index=False)
        md += "\n\n"

    return md
