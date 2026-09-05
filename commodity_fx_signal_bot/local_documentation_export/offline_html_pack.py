"""Offline HTML pack."""
import pandas as pd
from pathlib import Path
from .export_config import LocalDocumentationExportProfile

def build_offline_html_documentation_pack(project_root: Path, profile: LocalDocumentationExportProfile) -> tuple[str, dict]:
    sections = build_offline_html_pack_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_offline_html_pack(text)

def build_offline_html_pack_sections(profile: LocalDocumentationExportProfile) -> list[dict]:
    return [
        {"title": "Offline HTML Pack", "content": "This is the offline html pack."}
    ]

def build_offline_html_page_registry(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"page_name": "index"}])
    return df, summarize_offline_html_page_registry(df)

def summarize_offline_html_pack(text: str) -> dict:
    return {"length": len(text)}

def summarize_offline_html_page_registry(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
