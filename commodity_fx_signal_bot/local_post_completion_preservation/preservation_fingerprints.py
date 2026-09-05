import pandas as pd
from pathlib import Path
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def compute_preservation_fingerprint(path: Path, project_root: Path, profile: LocalPostCompletionPreservationProfile) -> dict:
    return {"hash": "fake_hash"}

def build_preservation_hash_fingerprint_rehearsal(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"file": "fake", "hash": "fake_hash"}])
    return df, summarize_preservation_fingerprints(df)

def summarize_preservation_fingerprints(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
