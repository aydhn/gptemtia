import pandas as pd
from pathlib import Path
from .packaging_config import LocalDistributionPackagingProfile

def build_distribution_bundle_sections(project_root: Path, profile: LocalDistributionPackagingProfile) -> list[dict]:
    return [
        {"title": "Amac ve kapsam", "content": "Distribution bundle rehearsal."},
        {"title": "Bu distribution bundle ne degildir?", "content": "Gercek archive, release veya deploy degildir."},
        {"title": "Portable docs bundle recap", "content": "Portable docs rehearsal icerir."},
        {"title": "Offline release folder manifest recap", "content": "Folder manifest recap."},
        {"title": "ZIP-map recap", "content": "ZIP-map recap."},
        {"title": "Inclusion/exclusion recap", "content": "Inclusion/exclusion recap."},
        {"title": "Safety boundary recap", "content": "Safety boundary recap."},
        {"title": "Packaging governance recap", "content": "Packaging governance recap."},
        {"title": "No-go/safe-go recap", "content": "No-go/safe-go recap."},
        {"title": "Final boundary statement", "content": "Yatirim tavsiyesi degildir, gercek trade yoktur."}
    ]

def build_final_local_distribution_bundle_rehearsal(project_root: Path, profile: LocalDistributionPackagingProfile) -> tuple[str, dict]:
    sections = build_distribution_bundle_sections(project_root, profile)
    text = "\n\n".join([f"## {s['title']}\n{s['content']}" for s in sections])
    text = f"# Final Local Distribution Bundle Rehearsal\n\n{text}"
    return text, summarize_distribution_bundle_rehearsal(text)

def build_distribution_bundle_manifest(project_root: Path, profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"bundle_file": "manifest.json", "status": "rehearsal"}])
    return df, summarize_distribution_bundle_manifest(df)

def summarize_distribution_bundle_rehearsal(text: str) -> dict:
    return {"status": "generated", "length": len(text)}

def summarize_distribution_bundle_manifest(df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(df)}
