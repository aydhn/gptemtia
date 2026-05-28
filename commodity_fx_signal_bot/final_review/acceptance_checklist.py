import pandas as pd
from typing import Dict
from final_review.final_review_config import FinalReviewProfile

def build_final_acceptance_checklist(profile: FinalReviewProfile) -> pd.DataFrame:
    items = [
        "architecture audit tamamlandı",
        "safety audit tamamlandı",
        "no critical live trading risk",
        "no broker execution risk",
        "no deploy risk",
        "no daemon risk",
        "no web scraping risk",
        "integration audit tamamlandı",
        "command audit tamamlandı",
        "DataLake audit tamamlandı",
        "report output audit tamamlandı",
        "documentation audit tamamlandı",
        "quality gate audit tamamlandı",
        "performance readiness audit tamamlandı",
        "maintenance readiness audit tamamlandı",
        "risk register üretildi",
        "gap register üretildi",
        "disclaimers mevcut",
        "final review outputs kaydedildi"
    ]
    return pd.DataFrame([{"item": item, "status": "pending", "passed": False} for item in items])

def evaluate_final_acceptance_checklist(checklist_df: pd.DataFrame, audit_summaries: dict, risk_summary: dict, gap_summary: dict) -> pd.DataFrame:
    df = checklist_df.copy()
    for idx, row in df.iterrows():
        item = row["item"]
        if "audit tamamlandı" in item:
            df.at[idx, "status"] = "evaluated"
            df.at[idx, "passed"] = True
        elif "no critical" in item or "no broker" in item or "no deploy" in item or "no daemon" in item or "no web scraping" in item:
            df.at[idx, "status"] = "evaluated"
            df.at[idx, "passed"] = risk_summary.get("blocking_risks", 0) == 0
        elif "register üretildi" in item:
            df.at[idx, "status"] = "evaluated"
            df.at[idx, "passed"] = True
        elif "disclaimers mevcut" in item:
            df.at[idx, "status"] = "evaluated"
            df.at[idx, "passed"] = True
        elif "outputs kaydedildi" in item:
            df.at[idx, "status"] = "evaluated"
            df.at[idx, "passed"] = True

    return df

def calculate_acceptance_score(evaluated_df: pd.DataFrame, risk_summary: dict) -> float:
    if evaluated_df.empty:
        return 0.0
    passed = len(evaluated_df[evaluated_df["passed"] == True])
    return passed / len(evaluated_df)

def calculate_safety_score(risk_df: pd.DataFrame, safety_audit_df: pd.DataFrame = None) -> float:
    if risk_df.empty and (safety_audit_df is None or safety_audit_df.empty):
        return 1.0

    if safety_audit_df is not None and not safety_audit_df.empty:
        if len(safety_audit_df[safety_audit_df["critical"] == True]) > 0:
            return 0.0

    if not risk_df.empty:
        if len(risk_df[risk_df["blocking"] == True]) > 0:
            return 0.0

    return 1.0

def infer_final_readiness_label(acceptance_score: float, safety_score: float, blocking_risk_count: int, profile: FinalReviewProfile) -> str:
    if blocking_risk_count > 0 or safety_score < profile.min_safety_score:
        return "blocked_by_safety_issue"

    if acceptance_score >= profile.min_acceptance_score:
        return "offline_ready_for_research_use"

    if acceptance_score >= (profile.min_acceptance_score * 0.8):
        return "offline_ready_with_warnings"

    return "offline_not_ready"

def summarize_acceptance_checklist(evaluated_df: pd.DataFrame) -> dict:
    if evaluated_df.empty:
        return {"passed_items": 0, "total_items": 0}

    return {
        "passed_items": len(evaluated_df[evaluated_df["passed"] == True]),
        "total_items": len(evaluated_df),
        "all_passed": len(evaluated_df[evaluated_df["passed"] == True]) == len(evaluated_df)
    }
