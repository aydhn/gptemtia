import pandas as pd
from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def link_evidence_to_outputs(evidence_df: pd.DataFrame, project_root: Path) -> pd.DataFrame:
    df = evidence_df.copy()
    if not df.empty:
        df["linked_output"] = "reports/output/dummy_output.csv"
        df["trace_label"] = "evidence_trace_available"
    return df

def build_evidence_output_trace_matrix(evidence_df: pd.DataFrame, project_root: Path, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    df = link_evidence_to_outputs(evidence_df, project_root)
    return df, summarize_evidence_output_trace(df)

def summarize_evidence_output_trace(trace_df: pd.DataFrame) -> dict:
    return {"total_output_traces": len(trace_df)}
