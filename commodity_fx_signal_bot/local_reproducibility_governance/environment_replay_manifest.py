"""Environment replay manifest."""
import pandas as pd
from pathlib import Path
from .reproducibility_config import LocalReproducibilityGovernanceProfile

def build_environment_replay_manifest(project_root: Path, profile: LocalReproducibilityGovernanceProfile) -> tuple[str, dict]:
    sections = build_environment_replay_manifest_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    summary = summarize_environment_replay_manifest(text)
    return text, summary

def build_environment_replay_manifest_sections(profile: LocalReproducibilityGovernanceProfile) -> list[dict]:
    return [
        {"title": "Environment replay amacı", "content": "Environment replay"},
        {"title": "Bu manifest ne değildir?", "content": "Gercek provisioning veya install degildir."},
        {"title": "Local/offline assumptions", "content": "Assumptions"},
        {"title": "Python/runtime notes", "content": "Runtime"},
        {"title": "Path conventions", "content": "Paths"},
        {"title": "Environment variables", "content": "Vars"},
        {"title": "Dependency notes", "content": "Deps"},
        {"title": "Non-install boundaries", "content": "Boundaries"},
        {"title": "Machine assumptions", "content": "Machine"},
        {"title": "Manual review required", "content": "Review required."},
        {"title": "Final boundary statement", "content": "Install yapilmaz."}
    ]

def summarize_environment_replay_manifest(text: str) -> dict:
    return {"length": len(text), "note": "Environment replay gercek provisioning degildir."}
