"""Reproducibility governance criteria."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def build_default_reproducibility_governance_criteria(profile: LocalReproducibilityGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"criteria": "reproducibility dossier available"},
        {"criteria": "environment replay manifest available"},
        {"criteria": "deterministic runbook available"},
        {"criteria": "build-free reproduction manifest available"},
        {"criteria": "evidence/integrity rehearsal available"},
        {"criteria": "drift/variance registers available"},
        {"criteria": "no build/install/provision/deploy"},
        {"criteria": "no live/broker/advice"},
        {"criteria": "manual review required"}
    ])

def build_reproducibility_governance_criteria_matrix(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_reproducibility_governance_criteria(profile)
    return df, summarize_reproducibility_governance_criteria(df)

def summarize_reproducibility_governance_criteria(df: pd.DataFrame) -> dict:
    return {"items": len(df), "note": "Criteria official certification criteria degildir."}
