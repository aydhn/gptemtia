import pandas as pd
from pathlib import Path
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_preservation_binder_sections(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> list[dict]:
    return [
        {"title": "Preservation amaci", "content": "Amac"},
        {"title": "Bu binder ne degildir?", "content": "Official preservation policy degildir. Yatirim tavsiyesi yoktur."},
        {"title": "Archive seal rehearsal", "content": "Rehearsal"},
        {"title": "Immutable README rehearsal", "content": "Rehearsal"},
        {"title": "Evidence vault index", "content": "Index"},
        {"title": "Final knowledge capsule", "content": "Capsule"},
        {"title": "Preservation inventories", "content": "Inventories"},
        {"title": "Fingerprint rehearsal", "content": "Fingerprint"},
        {"title": "Restore notes rehearsal", "content": "Restore"},
        {"title": "Access notes", "content": "Access"},
        {"title": "Handoff checklist", "content": "Handoff"},
        {"title": "Non-goals", "content": "Non-goals"},
        {"title": "No-go/safe-go", "content": "No-go/safe-go"},
        {"title": "Exceptions/gaps/risks", "content": "Exceptions/gaps/risks"},
        {"title": "Final boundary statement", "content": "Boundary statement. Dosya kilitleme yok. Archive/publish/release/deploy yok. Yatirim tavsiyesi yok."}
    ]

def build_post_completion_preservation_binder(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    sections = build_preservation_binder_sections(project_root, profile)
    text = "\n\n".join([f"## {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_preservation_binder(text)

def summarize_preservation_binder(text: str) -> dict:
    return {"length": len(text)}
