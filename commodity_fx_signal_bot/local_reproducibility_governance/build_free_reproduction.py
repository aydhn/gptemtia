"""Build-free reproduction layer."""
import pandas as pd
from pathlib import Path
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def build_build_free_reproduction_manifest(project_root: Path, profile: LocalReproducibilityGovernanceProfile) -> tuple[str, dict]:
    sections = build_build_free_reproduction_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    summary = summarize_build_free_reproduction_manifest(text)
    return text, summary

def build_build_free_reproduction_sections(profile: LocalReproducibilityGovernanceProfile) -> list[dict]:
    return [
        {"title": "Build-free reproduction amacı", "content": "Build-free"},
        {"title": "Bu layer ne değildir?", "content": "Gercek build degildir, install yoktur."},
        {"title": "Build yapılmadan okunabilir çıktılar", "content": "Report-only reading."},
        {"title": "Script/report/DataLake ilişkisi", "content": "Map"},
        {"title": "Generated docs ilişkisi", "content": "Map"},
        {"title": "Packaging/docs/export ilişkisi", "content": "Map"},
        {"title": "Manual review required", "content": "Review"},
        {"title": "Final boundary statement", "content": "Artifact uretmez."}
    ]

def summarize_build_free_reproduction_manifest(text: str) -> dict:
    return {"length": len(text), "note": "Build-free reproduction gercek build degildir."}
