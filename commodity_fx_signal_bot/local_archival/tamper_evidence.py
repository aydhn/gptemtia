"""
Tamper Evidence.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def build_tamper_evidence_checks(hash_df: pd.DataFrame, hoh_df: pd.DataFrame, profile: LocalArchivalProfile) -> pd.DataFrame:
    checks = [
        {"check_type": "hash_presence", "status": "passed" if hash_df is not None and not hash_df.empty else "failed"},
        {"check_type": "hoh_presence", "status": "passed" if hoh_df is not None and not hoh_df.empty else "failed"},
        {"check_type": "legal_proof", "status": "skipped", "note": "Not a forensic proof."}
    ]
    return pd.DataFrame(checks)

def build_tamper_evidence_dry_run_report(hash_df: pd.DataFrame, hoh_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = build_tamper_evidence_checks(hash_df, hoh_df, profile)
    return df, summarize_tamper_evidence_dry_run(df)

def summarize_tamper_evidence_dry_run(tamper_df: pd.DataFrame) -> dict:
    return {"total_checks": len(tamper_df) if tamper_df is not None else 0}
