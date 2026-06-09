import pandas as pd
from evidence_governance.evidence_config import EvidenceGovernanceProfile
from evidence_governance.evidence_models import EvidenceGap, build_evidence_gap_id

def detect_evidence_gaps(control_status_df: pd.DataFrame, trace_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> list[EvidenceGap]:
    gaps = []

    if control_status_df is not None and not control_status_df.empty:
        for _, row in control_status_df.iterrows():
            cid = row.get("control_id")
            st = row.get("status")

            if st in ["control_missing_evidence", "control_unknown"]:
                gaps.append(EvidenceGap(
                    gap_id=build_evidence_gap_id(cid, "missing_required_evidence"),
                    control_id=cid,
                    gap_type="missing_required_evidence",
                    description=f"Control {cid} has no valid evidence mapped.",
                    severity="high",
                    recommended_safe_follow_up="Offline rapor veya artifact üretilmelidir.",
                    warnings=[]
                ))
            elif st == "control_stale_evidence":
                gaps.append(EvidenceGap(
                    gap_id=build_evidence_gap_id(cid, "stale_evidence"),
                    control_id=cid,
                    gap_type="stale_evidence",
                    description=f"Control {cid} evidence is stale.",
                    severity="medium",
                    recommended_safe_follow_up="Artifact yeniden üretilmelidir.",
                    warnings=[]
                ))
            elif st == "control_partially_evidenced":
                gaps.append(EvidenceGap(
                    gap_id=build_evidence_gap_id(cid, "weak_evidence_only"),
                    control_id=cid,
                    gap_type="weak_evidence_only",
                    description=f"Control {cid} only has supporting/weak evidence.",
                    severity="low",
                    recommended_safe_follow_up="Direct evidence sağlayacak rapor üretilmelidir.",
                    warnings=[]
                ))

    return gaps

def classify_evidence_gap(row: pd.Series) -> dict:
    gap_type = row.get("gap_type", "unknown")
    if "missing" in gap_type:
        return {"severity": "high"}
    if "stale" in gap_type:
        return {"severity": "medium"}
    return {"severity": "low"}

def evidence_gaps_to_dataframe(gaps: list[EvidenceGap]) -> pd.DataFrame:
    from evidence_governance.evidence_models import evidence_gap_to_dict
    if not gaps:
        return pd.DataFrame()
    return pd.DataFrame([evidence_gap_to_dict(g) for g in gaps])

def summarize_evidence_gaps(gap_df: pd.DataFrame) -> dict:
    if gap_df is None or gap_df.empty:
        return {"total_gaps": 0}

    return {
        "total_gaps": len(gap_df),
        "by_severity": gap_df["severity"].value_counts().to_dict() if "severity" in gap_df.columns else {},
        "by_type": gap_df["gap_type"].value_counts().to_dict() if "gap_type" in gap_df.columns else {}
    }
