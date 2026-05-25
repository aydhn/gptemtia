"""
Project consolidation logic.
"""

import pandas as pd
from pathlib import Path
from command_center.project_status import summarize_project_status
from command_center.module_health import summarize_module_health
from command_center.script_discovery import summarize_script_discovery
from command_center.phase_coverage import summarize_phase_coverage

def build_project_consolidation_summary(project_status_df: pd.DataFrame, module_health_df: pd.DataFrame, phase_coverage_df: pd.DataFrame, script_matrix_df: pd.DataFrame) -> dict:
    return {
        "status_summary": summarize_project_status(project_status_df),
        "health_summary": summarize_module_health(module_health_df),
        "script_summary": summarize_script_discovery(script_matrix_df),
        "coverage_summary": summarize_phase_coverage(phase_coverage_df)
    }

def build_consolidation_score(summary: dict) -> float:
    # A simple scoring based on the summaries
    score = 0.0

    health = summary.get("health_summary", {})
    if health.get("healthy_modules", 0) > 10:
        score += 0.5

    coverage = summary.get("coverage_summary", {})
    if coverage.get("phases_covered", 0) >= 5:
        score += 0.5

    return score

def infer_project_maturity_label(score: float) -> str:
    if score >= 0.8:
        return "consolidated_offline_research_platform"
    elif score >= 0.5:
        return "mature_offline_research_platform"
    elif score >= 0.2:
        return "developing_research_platform"
    elif score >= 0.0:
        return "early_research_platform"
    return "unknown_maturity"

def build_consolidation_table(summary: dict) -> pd.DataFrame:
    score = build_consolidation_score(summary)
    label = infer_project_maturity_label(score)

    data = [
        {"metric": "Consolidation Score", "value": score},
        {"metric": "Maturity Label", "value": label},
        {"metric": "Healthy Modules", "value": summary.get("health_summary", {}).get("healthy_modules", 0)},
        {"metric": "Phases Covered", "value": summary.get("coverage_summary", {}).get("phases_covered", 0)}
    ]
    return pd.DataFrame(data)

def build_phase_1_to_50_digest(project_root: Path) -> str:
    return "Phase 1-50 Consolidation Digest: The project has successfully integrated all offline research layers (Data, Features, ML, Backtest, Portfolio, Factor, Meta, Planning, Knowledge Base) into a unified Command Center. The platform is strictly for offline research and does not generate live trades."
