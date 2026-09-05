"""Deterministic runbook."""
import pandas as pd
from pathlib import Path
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def build_deterministic_runbook(project_root: Path, profile: LocalReproducibilityGovernanceProfile) -> tuple[str, dict]:
    sections = build_deterministic_runbook_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    summary = summarize_deterministic_runbook(text)
    return text, summary

def build_deterministic_runbook_sections(profile: LocalReproducibilityGovernanceProfile) -> list[dict]:
    return [
        {"title": "Deterministic runbook amacı", "content": "Deterministic runbook"},
        {"title": "Bu runbook ne değildir?", "content": "Determinism guarantee degildir."},
        {"title": "Local-only rerun logic", "content": "Rerun logic"},
        {"title": "Safe report-only command families", "content": "Safe commands"},
        {"title": "Expected output families", "content": "Expected output kesin performans iddiası olmamalı."},
        {"title": "Non-determinism sources", "content": "Sources"},
        {"title": "Drift/variance notes", "content": "Randomness/clock/filesystem/order gibi drift kaynaklari not edilmeli."},
        {"title": "Manual review points", "content": "Review"},
        {"title": "No-go/safe-go recap", "content": "Recap"}
    ]

def summarize_deterministic_runbook(text: str) -> dict:
    return {"length": len(text), "note": "Deterministic runbook komut calistirmaz, build yapmaz."}
