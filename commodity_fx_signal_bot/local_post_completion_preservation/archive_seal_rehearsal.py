import pandas as pd
from pathlib import Path
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_archive_seal_rehearsal_sections(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> list[dict]:
    return [
        {"title": "Amac ve kapsam", "content": "Archive seal rehearsal."},
        {"title": "Bu paket ne degildir?", "content": "Gercek archive seal degildir."},
        {"title": "Archive seal rehearsal overview", "content": "Overview"},
        {"title": "Evidence vault recap", "content": "Recap"},
        {"title": "Knowledge capsule recap", "content": "Recap"},
        {"title": "Preservation binder recap", "content": "Recap"},
        {"title": "Inventory/fingerprint recap", "content": "Recap"},
        {"title": "Restore notes recap", "content": "Recap"},
        {"title": "Non-goals recap", "content": "Recap"},
        {"title": "No-go/safe-go recap", "content": "Recap"},
        {"title": "Final boundary statement", "content": "Boundary"}
    ]

def build_final_local_archive_seal_rehearsal_packet(project_root: Path, profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    sections = build_archive_seal_rehearsal_sections(project_root, profile)
    text = "\n\n".join([f"## {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_archive_seal_rehearsal_packet(text)

def build_archive_seal_checklist_registry(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"item": "rehearsal_done", "status": "ok"}])
    return df, summarize_archive_seal_checklist(df)

def summarize_archive_seal_rehearsal_packet(text: str) -> dict:
    return {"length": len(text)}

def summarize_archive_seal_checklist(df: pd.DataFrame) -> dict:
    return {"items": len(df)}
