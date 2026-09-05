import pandas as pd
from pathlib import Path
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def discover_evidence_vault_sources(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"id": "ev1"}])

def build_evidence_vault_index(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"evidence_id": "ev1", "vault_status": "evidence_vault_indexed_rehearsal"}])
    return df, summarize_evidence_vault_index(df)

def build_evidence_vault_source_map(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"evidence_id": "ev1", "source_path": "/fake/path"}])
    return df, summarize_evidence_vault_index(df)

def build_evidence_vault_reading_order(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"evidence_id": "ev1", "order": 1}])
    return df, summarize_evidence_vault_index(df)

def summarize_evidence_vault_index(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
