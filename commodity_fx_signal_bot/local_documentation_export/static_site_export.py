"""Static site export."""
import pandas as pd
from pathlib import Path
from .export_config import LocalDocumentationExportProfile

def build_final_local_static_site_export_rehearsal(project_root: Path, profile: LocalDocumentationExportProfile) -> tuple[str, dict]:
    sections = build_static_site_export_sections(project_root, profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_static_site_export_rehearsal(text)

def build_static_site_export_sections(project_root: Path, profile: LocalDocumentationExportProfile) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Local static site rehearsal."},
        {"title": "Bu static site export ne değildir?", "content": "Gerçek deploy değildir, web server başlatmaz."},
        {"title": "Offline HTML pack overview", "content": "Offline pack overview."},
        {"title": "Navigation tree recap", "content": "Navigation tree recap."},
        {"title": "Source map recap", "content": "Source map recap."},
        {"title": "Link map recap", "content": "Link map recap."},
        {"title": "Printable binder recap", "content": "Printable binder recap."},
        {"title": "PDF-ready docs recap", "content": "PDF-ready docs recap."},
        {"title": "Presentation-freeze recap", "content": "Presentation-freeze recap."},
        {"title": "No-go/safe-go recap", "content": "No-go/safe-go recap."},
        {"title": "Final boundary statement", "content": "Final boundary statement."}
    ]

def build_static_site_export_manifest(project_root: Path, profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"manifest_item": "test"}])
    return df, summarize_static_site_export_manifest(df)

def summarize_static_site_export_rehearsal(text: str) -> dict:
    return {"length": len(text)}

def summarize_static_site_export_manifest(df: pd.DataFrame) -> dict:
    return {"item_count": len(df)}
