"""Reproducibility evidence."""
import pandas as pd
from pathlib import Path
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def map_reproducibility_evidence_sources(project_root: Path, profile: LocalReproducibilityGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"evidence": "source1", "status": "mapped"}])

def build_reproducibility_evidence_index(project_root: Path, profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = map_reproducibility_evidence_sources(project_root, profile)
    return df, summarize_reproducibility_evidence(df)

def summarize_reproducibility_evidence(df: pd.DataFrame) -> dict:
    return {"items": len(df), "note": "Evidence index legal/compliance proof degildir."}
