import pandas as pd
from datetime import datetime, timezone
from evidence_governance.evidence_config import EvidenceGovernanceProfile

def calculate_evidence_completeness_score(status_df: pd.DataFrame) -> float:
    if status_df is None or status_df.empty:
        return 0.0

    total = len(status_df)

    # weights: evidenced = 1.0, partially = 0.5, others = 0
    score = 0.0
    for _, row in status_df.iterrows():
        st = row.get("status")
        if st == "control_evidenced":
            score += 1.0
        elif st == "control_partially_evidenced":
            score += 0.5

    return score / total if total > 0 else 0.0

def calculate_evidence_freshness_score(artifact_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> float:
    if artifact_df is None or artifact_df.empty:
        return 0.0

    total = len(artifact_df)
    score = 0.0
    for _, art in artifact_df.iterrows():
        fl = art.get("freshness_label")
        if fl == "evidence_fresh":
            score += 1.0
        elif fl == "evidence_warning_stale":
            score += 0.5

    return score / total if total > 0 else 0.0

def classify_artifact_freshness(modified_at_utc: str | None, profile: EvidenceGovernanceProfile) -> str:
    if not modified_at_utc:
        return "evidence_missing_timestamp"

    try:
        dt = datetime.fromisoformat(modified_at_utc)
        days = (datetime.now(timezone.utc) - dt).days
        if days <= profile.freshness_days_warning:
            return "evidence_fresh"
        elif days <= profile.freshness_days_warning * 2:
            return "evidence_warning_stale"
        else:
            return "evidence_stale"
    except Exception:
        return "evidence_unknown_freshness"

def build_evidence_completeness_report(status_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    score = calculate_evidence_completeness_score(status_df)
    df = pd.DataFrame([{"metric": "evidence_completeness_score", "value": score}])
    return df, {"completeness_score": score}

def build_evidence_freshness_report(artifact_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_evidence_freshness_score(artifact_df, profile)

    breakdown = {}
    if artifact_df is not None and not artifact_df.empty and "freshness_label" in artifact_df.columns:
        breakdown = artifact_df["freshness_label"].value_counts().to_dict()

    df = pd.DataFrame([{"metric": "evidence_freshness_score", "value": score}])
    return df, {"freshness_score": score, "breakdown": breakdown}

def summarize_evidence_scoring(completeness: float, freshness: float) -> dict:
    return {
        "completeness_score": completeness,
        "freshness_score": freshness,
        "overall_score": (completeness + freshness) / 2.0
    }
