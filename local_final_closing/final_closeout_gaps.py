import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def detect_missing_final_closing_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame() if domain_df is not None and not domain_df.empty else pd.DataFrame([{"gap": "missing_domains"}])

def detect_missing_terminal_lock_items(lock_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame() if lock_df is not None and not lock_df.empty else pd.DataFrame([{"gap": "missing_lock_items"}])

def detect_missing_constitution_items(constitution_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame() if constitution_df is not None and not constitution_df.empty else pd.DataFrame([{"gap": "missing_constitution_items"}])

def detect_missing_archive_index_items(archive_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame() if archive_df is not None and not archive_df.empty else pd.DataFrame([{"gap": "missing_archive_items"}])

def build_final_closeout_gap_register(domain_df: pd.DataFrame, lock_df: pd.DataFrame, constitution_df: pd.DataFrame, archive_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    gaps = pd.concat([
        detect_missing_final_closing_domains(domain_df),
        detect_missing_terminal_lock_items(lock_df),
        detect_missing_constitution_items(constitution_df),
        detect_missing_archive_index_items(archive_df)
    ], ignore_index=True)
    return gaps, summarize_final_closeout_gaps(gaps)

def summarize_final_closeout_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total_gaps": len(gap_df) if gap_df is not None else 0}
