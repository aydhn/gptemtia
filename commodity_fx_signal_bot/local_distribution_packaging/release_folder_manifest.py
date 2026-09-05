import pandas as pd
from pathlib import Path
from .packaging_config import LocalDistributionPackagingProfile

def build_release_folder_manifest_sections(profile: LocalDistributionPackagingProfile) -> list[dict]:
    return [
        {"title": "Release folder amaci", "content": "Offline release folder manifest."},
        {"title": "Bu release folder ne degildir?", "content": "Gercek release veya deploy degildir."},
        {"title": "Onerilen klasor agaci", "content": "Folder tree rehearsal."},
        {"title": "Dahil edilecek manifest kayitlari", "content": "Manifest registry."},
        {"title": "Haric tutulacak kayitlar", "content": "Exclusion registry."},
        {"title": "Secrets/credentials exclusion", "content": "No raw secrets."},
        {"title": "Non-production boundary", "content": "Not for production."},
        {"title": "Manual review statement", "content": "Review needed."}
    ]

def build_offline_release_folder_manifest(project_root: Path, profile: LocalDistributionPackagingProfile) -> tuple[str, dict]:
    sections = build_release_folder_manifest_sections(profile)
    text = "\n\n".join([f"## {s['title']}\n{s['content']}" for s in sections])
    text = f"# Offline Release Folder Manifest\n\n{text}"
    return text, summarize_release_folder_manifest(text)

def summarize_release_folder_manifest(text: str) -> dict:
    return {"status": "generated", "length": len(text)}
