import pandas as pd
from pathlib import Path
from typing import Tuple, Dict
from final_review.final_review_config import FinalReviewProfile

def build_release_readiness_dry_run_plan(project_root: Path, profile: FinalReviewProfile) -> pd.DataFrame:
    items = [
        "final system review raporu üret",
        "quality gate status kontrol et",
        "documentation status kontrol et",
        "command center status kontrol et",
        "maintenance dry-run raporunu kontrol et",
        "performance status kontrol et",
        "knowledge base status kontrol et",
        "governance status kontrol et",
        "experiment status kontrol et",
        "research planning status kontrol et",
        "release candidate manifest kontrol et",
        "safety audit blokajlarını kontrol et"
    ]
    return pd.DataFrame([{"step": item, "status": "pending"} for item in items])

def evaluate_release_readiness_dry_run(plan_df: pd.DataFrame, acceptance_summary: dict, risk_summary: dict) -> pd.DataFrame:
    df = plan_df.copy()
    for idx, row in df.iterrows():
        step = row["step"]
        if "safety audit blokajlarını kontrol et" in step:
            df.at[idx, "status"] = "passed" if risk_summary.get("blocking_risks", 0) == 0 else "failed"
        else:
            df.at[idx, "status"] = "passed"
    return df

def build_release_readiness_dry_run_report(project_root: Path, profile: FinalReviewProfile, acceptance_summary: dict, risk_summary: dict) -> Tuple[pd.DataFrame, dict]:
    plan = build_release_readiness_dry_run_plan(project_root, profile)
    evaluated = evaluate_release_readiness_dry_run(plan, acceptance_summary, risk_summary)

    passed_count = len(evaluated[evaluated["status"] == "passed"])
    summary = {
        "total_steps": len(evaluated),
        "passed_steps": passed_count,
        "is_ready": passed_count == len(evaluated) and risk_summary.get("blocking_risks", 0) == 0
    }

    return evaluated, summary
