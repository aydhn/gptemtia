"""Reproducibility governance binder."""
import pandas as pd
from pathlib import Path
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def build_terminal_reproducibility_governance_binder(project_root: Path, profile: LocalReproducibilityGovernanceProfile) -> tuple[str, dict]:
    sections = build_reproducibility_governance_binder_sections(project_root, profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    summary = summarize_reproducibility_governance_binder(text)
    return text, summary

def build_reproducibility_governance_binder_sections(project_root: Path, profile: LocalReproducibilityGovernanceProfile) -> list[dict]:
    return [
        {"title": "Reproducibility governance amacı", "content": "Governance"},
        {"title": "Bu binder ne değildir?", "content": "Official reproducibility policy degildir. Certification yoktur."},
        {"title": "Dossier recap", "content": "Dossier"},
        {"title": "Environment replay recap", "content": "Replay"},
        {"title": "Deterministic runbook recap", "content": "Runbook"},
        {"title": "Build-free reproduction recap", "content": "Build-free"},
        {"title": "Evidence/integrity recap", "content": "Evidence"},
        {"title": "Drift/variance recap", "content": "Drift"},
        {"title": "Manual review recap", "content": "Review"},
        {"title": "Criteria/issues/handoff recap", "content": "Criteria"},
        {"title": "No-go/safe-go recap", "content": "No-go"},
        {"title": "Exceptions/gaps/risks recap", "content": "Exceptions"},
        {"title": "Final boundary statement", "content": "Yatirim tavsiyesi yoktur."}
    ]

def summarize_reproducibility_governance_binder(text: str) -> dict:
    return {"length": len(text), "note": "Binder official reproducibility policy degildir."}
