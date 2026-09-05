import pandas as pd
from pathlib import Path
from .packaging_config import LocalDistributionPackagingProfile

def map_packaging_governance_evidence_sources(project_root: Path, profile: LocalDistributionPackagingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"evidence": "manifest exists", "source": "bundle_manifest"}
    ])

def build_packaging_governance_evidence_index(project_root: Path, profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = map_packaging_governance_evidence_sources(project_root, profile)
    return df, summarize_packaging_governance_evidence(df)

def summarize_packaging_governance_evidence(df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(df)}
