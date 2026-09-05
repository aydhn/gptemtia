"""Reproducibility no-go/safe-go."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def build_reproducibility_no_go_conditions(profile: LocalReproducibilityGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "real build claim"},
        {"condition": "cloud build claim"},
        {"condition": "CI/CD claim"},
        {"condition": "Docker build/image claim"},
        {"condition": "build artifact claim"},
        {"condition": "binary artifact claim"},
        {"condition": "installer/executable claim"},
        {"condition": "environment provisioning claim"},
        {"condition": "dependency install claim"},
        {"condition": "pip/poetry/conda install claim"},
        {"condition": "package publish claim"},
        {"condition": "git tag claim"},
        {"condition": "cloud upload claim"},
        {"condition": "deployment claim"},
        {"condition": "official build attestation claim"},
        {"condition": "reproducibility certification claim"},
        {"condition": "legal/compliance approval claim"},
        {"condition": "production approval claim"},
        {"condition": "official acceptance claim"},
        {"condition": "broker readiness claim"},
        {"condition": "live trading claim"},
        {"condition": "investment advice wording"},
        {"condition": "model deployment claim"},
        {"condition": "web server/dashboard claim"},
        {"condition": "telemetry claim"},
        {"condition": "external LLM/API claim"},
        {"condition": "vector/embedding claim"},
        {"condition": "raw secret output"},
        {"condition": "file deletion/move/overwrite claim"}
    ])

def build_reproducibility_safe_go_conditions(profile: LocalReproducibilityGovernanceProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "reproducibility dossier documented"},
        {"condition": "environment replay manifest documented"},
        {"condition": "deterministic runbook documented"},
        {"condition": "build-free reproduction manifest documented"},
        {"condition": "evidence/integrity rehearsal available"},
        {"condition": "drift/variance registers available"},
        {"condition": "manual review ledger available"},
        {"condition": "no real build/install/provision/deploy/live/broker/advice"},
        {"condition": "manual review required"}
    ])

def build_reproducibility_no_go_safe_go_summary(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_reproducibility_no_go_conditions(profile)
    safe_go = build_reproducibility_safe_go_conditions(profile)
    df = pd.concat([no_go.assign(type="no-go"), safe_go.assign(type="safe-go")], ignore_index=True)
    return df, summarize_reproducibility_no_go_safe_go(df)

def summarize_reproducibility_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"items": len(summary_df), "note": "Safe-go gercek certification degildir. Manual review required."}
