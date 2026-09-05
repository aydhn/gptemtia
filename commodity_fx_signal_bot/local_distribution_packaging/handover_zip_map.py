import pandas as pd
from pathlib import Path
from .packaging_config import LocalDistributionPackagingProfile

def build_handover_zip_map_sections(profile: LocalDistributionPackagingProfile) -> list[dict]:
    return [
        {"title": "ZIP-map amaci", "content": "ZIP-map for handover."},
        {"title": "Bu ZIP-map ne degildir?", "content": "Gercek ZIP degildir."},
        {"title": "Gercek ZIP uretilmedigi beyani", "content": "No zipfile, shutil.make_archive, etc."},
        {"title": "Folder-to-file mapping", "content": "Mapping items."},
        {"title": "Handover route", "content": "Route to operator."},
        {"title": "Recipient checklist", "content": "Checklist for recipient."},
        {"title": "Compression non-goals", "content": "No compression."},
        {"title": "Safety boundary", "content": "Safety boundary."},
        {"title": "Manual review statement", "content": "Review needed."}
    ]

def build_terminal_handover_zip_map(project_root: Path, profile: LocalDistributionPackagingProfile) -> tuple[str, dict]:
    sections = build_handover_zip_map_sections(profile)
    text = "\n\n".join([f"## {s['title']}\n{s['content']}" for s in sections])
    text = f"# Terminal Handover ZIP-Map\n\n{text}"
    return text, summarize_handover_zip_map(text)

def build_zip_map_manifest(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"zip_file": "dummy.zip", "status": "rehearsal"}])
    return df, summarize_zip_map_manifest(df)

def summarize_handover_zip_map(text: str) -> dict:
    return {"status": "generated", "length": len(text)}

def summarize_zip_map_manifest(df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(df)}
