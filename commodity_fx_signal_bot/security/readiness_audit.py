import pandas as pd
from security.security_config import SecurityProfile
from security.security_models import SecurityAuditSummary

def calculate_readiness_score(findings_df: pd.DataFrame, component_scores: dict | None = None) -> float:
    if findings_df.empty: return 1.0
    if len(findings_df[findings_df["severity"] == "critical"]) > 0 or len(findings_df[findings_df["blocking"] == True]) > 0: return 0.0
    score = 1.0 - (len(findings_df[findings_df["severity"] == "high"]) * 0.1)
    return max(0.0, score)

def infer_readiness_label(score: float, findings_df: pd.DataFrame) -> str:
    if score == 0.0: return "not_ready"
    if score < 0.8: return "readiness_warning"
    return "ready_for_local_research"

def build_readiness_checklist(findings_df: pd.DataFrame, audit_summaries: dict) -> pd.DataFrame: return pd.DataFrame()

def build_production_readiness_audit(findings_df: pd.DataFrame, audit_summaries: dict, profile: SecurityProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_readiness_score(findings_df)
    return findings_df, {
        "readiness_score": score,
        "readiness_label": infer_readiness_label(score, findings_df),
        "is_financial_production_deploy_approval": False,
        "message": "This is NOT a financial production deploy approval. It is a local research readiness score."
    }
