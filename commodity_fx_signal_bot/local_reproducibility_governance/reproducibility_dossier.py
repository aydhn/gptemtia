"""Reproducibility dossier."""
import pandas as pd
from pathlib import Path
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def build_final_local_reproducibility_dossier(project_root: Path, profile: LocalReproducibilityGovernanceProfile) -> tuple[str, dict]:
    sections = build_reproducibility_dossier_sections(project_root, profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    summary = summarize_reproducibility_dossier(text)
    return text, summary

def build_reproducibility_dossier_sections(project_root: Path, profile: LocalReproducibilityGovernanceProfile) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Offline/local reproducibility dossier."},
        {"title": "Bu dossier ne değildir?", "content": "Gercek build, CI/CD, Docker image, attestation degildir."},
        {"title": "Build-free reproduction overview", "content": "Build-free reproduction saglanmaktadir."},
        {"title": "Environment replay overview", "content": "Environment replay saglanmaktadir."},
        {"title": "Deterministic runbook overview", "content": "Deterministic runbook saglanmaktadir."},
        {"title": "Evidence/integrity recap", "content": "Evidence/integrity checkleri saglanmaktadir."},
        {"title": "Drift/variance recap", "content": "Drift/variance checkleri saglanmaktadir."},
        {"title": "Manual review recap", "content": "Manual review saglanmaktadir."},
        {"title": "Governance recap", "content": "Governance saglanmaktadir."},
        {"title": "No-go/safe-go recap", "content": "No-go/safe-go saglanmaktadir."},
        {"title": "Final boundary statement", "content": "Bu dossier offline okuma icindir, kurulum icermez."}
    ]

def build_reproducibility_dossier_index(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"index": "1", "name": "dossier"}])
    return df, summarize_reproducibility_dossier_index(df)

def summarize_reproducibility_dossier(text: str) -> dict:
    return {"length": len(text), "note": "Reproducibility dossier official attestation degildir."}

def summarize_reproducibility_dossier_index(df: pd.DataFrame) -> dict:
    return {"items": len(df)}
