"""Offline HTML pages."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile

def sanitize_offline_html_text(text: str) -> str:
    return text.replace("<script", "&lt;script")

def render_offline_html_page(title: str, body_markdown: str, profile: LocalDocumentationExportProfile) -> str:
    return f"<html><head><title>{title}</title></head><body><h1>{title}</h1><p>{sanitize_offline_html_text(body_markdown)}</p></body></html>"

def build_offline_html_index_page(profile: LocalDocumentationExportProfile) -> tuple[str, dict]:
    html = render_offline_html_page("Index", "Local documentation export rehearsal index.", profile)
    return html, {"length": len(html)}

def build_offline_html_section_registry(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"section": "main"}])
    return df, summarize_offline_html_sections(df)

def build_offline_html_print_stylesheet(profile: LocalDocumentationExportProfile) -> tuple[str, dict]:
    css = "body { font-family: sans-serif; }"
    return css, {"length": len(css)}

def summarize_offline_html_sections(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
