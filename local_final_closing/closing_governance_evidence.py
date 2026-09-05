import pandas as pd
from pathlib import Path
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def map_closing_governance_evidence_sources(project_root: Path, profile: LocalFinalClosingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"source": "local_final_closing", "evidence": "Final closing structures exist", "legal_proof": False}
    ])

def build_closing_governance_final_evidence_index(project_root: Path, profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    df = map_closing_governance_evidence_sources(project_root, profile)
    return df, summarize_closing_governance_evidence(df)

def summarize_closing_governance_evidence(df: pd.DataFrame) -> dict:
    return {"total_evidence": len(df)}
