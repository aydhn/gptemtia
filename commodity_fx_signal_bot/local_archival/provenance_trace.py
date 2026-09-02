"""
Provenance Trace.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile

def link_provenance_to_delivery_outputs(hash_df: pd.DataFrame, project_root: Path) -> pd.DataFrame:
    df = hash_df.copy()
    if not df.empty:
        df["delivery_link"] = df["relative_path"].apply(lambda x: "linked" if "delivery" in str(x) else "unlinked")
    return df

def link_provenance_to_acceptance_outputs(hash_df: pd.DataFrame, project_root: Path) -> pd.DataFrame:
    df = hash_df.copy()
    if not df.empty:
        df["acceptance_link"] = df["relative_path"].apply(lambda x: "linked" if "acceptance" in str(x) else "unlinked")
    return df

def build_provenance_trace_matrix(inventory_df: pd.DataFrame, hash_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = hash_df.copy()
    if not df.empty:
        df["trace_status"] = "traced"
    return df, summarize_provenance_trace(df)

def build_provenance_delivery_trace_matrix(hash_df: pd.DataFrame, project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = link_provenance_to_delivery_outputs(hash_df, project_root)
    return df, summarize_provenance_trace(df)

def build_provenance_acceptance_trace_matrix(hash_df: pd.DataFrame, project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = link_provenance_to_acceptance_outputs(hash_df, project_root)
    return df, summarize_provenance_trace(df)

def summarize_provenance_trace(trace_df: pd.DataFrame) -> dict:
    return {"total_traces": len(trace_df) if trace_df is not None else 0}
