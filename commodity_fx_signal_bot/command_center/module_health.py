"""
Module health calculations.
"""

import pandas as pd

def calculate_module_health_score(row: pd.Series) -> float:
    score = 0.0
    if row.get("data_lake_available", False):
        score += 0.25
    if row.get("reports_available", False):
        score += 0.25
    if row.get("script_count", 0) > 0:
        score += 0.25
    if row.get("test_count", 0) > 0:
        score += 0.25
    return score

def infer_module_health_label(score: float, warnings: list[str] | None = None) -> str:
    if warnings and len(warnings) > 0:
        if score >= 0.75:
            return "usable_with_warnings"
        else:
            return "incomplete_module"

    if score >= 0.75:
        return "healthy_offline_module"
    elif score >= 0.5:
        return "incomplete_module"
    elif score > 0:
        return "missing_outputs"
    return "unknown_health"

def build_module_health_table(status_df: pd.DataFrame) -> pd.DataFrame:
    health_data = []
    for _, row in status_df.iterrows():
        score = calculate_module_health_score(row)
        label = infer_module_health_label(score, row.get("warnings", []))
        health_data.append({
            "module_name": row["module_name"],
            "health_score": score,
            "health_label": label
        })
    return pd.DataFrame(health_data)

def summarize_module_health(health_df: pd.DataFrame) -> dict:
    if health_df.empty:
        return {}

    return {
        "average_score": health_df["health_score"].mean(),
        "healthy_modules": len(health_df[health_df["health_label"] == "healthy_offline_module"]),
        "incomplete_modules": len(health_df[health_df["health_label"] == "incomplete_module"])
    }
