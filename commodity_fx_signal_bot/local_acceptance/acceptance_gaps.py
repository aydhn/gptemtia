import pandas as pd
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def detect_missing_acceptance_evidence(evidence_df: pd.DataFrame, criteria_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(columns=["gap_id", "type", "description"])

def detect_missing_acceptance_traces(trace_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(columns=["gap_id", "type", "description"])

def detect_missing_acceptance_checklist_items(checklist_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(columns=["gap_id", "type", "description"])

def build_acceptance_gap_register(
    checklist_df: pd.DataFrame,
    evidence_df: pd.DataFrame,
    trace_df: pd.DataFrame,
    criteria_df: pd.DataFrame,
    profile: LocalAcceptanceProfile,
) -> tuple[pd.DataFrame, dict]:
    g1 = detect_missing_acceptance_evidence(evidence_df, criteria_df)
    g2 = detect_missing_acceptance_traces(trace_df)
    g3 = detect_missing_acceptance_checklist_items(checklist_df)
    df = pd.concat([g1, g2, g3], ignore_index=True) if not (g1.empty and g2.empty and g3.empty) else pd.DataFrame(columns=["gap_id", "type", "description"])
    return df, summarize_acceptance_gaps(df)

def summarize_acceptance_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total_gaps": len(gap_df)}
