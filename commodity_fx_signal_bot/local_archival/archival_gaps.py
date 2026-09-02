"""
Archival Gaps.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def detect_missing_hashes(hash_df: pd.DataFrame) -> pd.DataFrame:
    if hash_df.empty: return pd.DataFrame()
    return hash_df[hash_df["hash_status"] == "hash_rehearsal_missing"]

def detect_missing_provenance_entries(lock_entries_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(columns=["relative_path"])

def detect_missing_custody_steps(custody_df: pd.DataFrame) -> pd.DataFrame:
    if custody_df.empty: return pd.DataFrame()
    return custody_df[custody_df["custody_status"] == "custody_rehearsal_missing"]

def build_archival_gap_register(
    inventory_df: pd.DataFrame,
    hash_df: pd.DataFrame,
    lock_entries_df: pd.DataFrame,
    custody_df: pd.DataFrame,
    profile: LocalArchivalProfile,
) -> tuple[pd.DataFrame, dict]:
    gaps = []
    # simplified
    df = pd.DataFrame(gaps, columns=["gap_type", "description"])
    return df, summarize_archival_gaps(df)

def summarize_archival_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total_gaps": len(gap_df) if gap_df is not None else 0}
