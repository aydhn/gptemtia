"""Printable binder."""
import pandas as pd
from pathlib import Path
from .export_config import LocalDocumentationExportProfile

def build_printable_binder_packet(project_root: Path, profile: LocalDocumentationExportProfile) -> tuple[str, dict]:
    sections = build_printable_binder_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_printable_binder_packet(text)

def build_printable_binder_sections(profile: LocalDocumentationExportProfile) -> list[dict]:
    return [
        {"title": "Binder amacı", "content": "Offline okunabilir dokuman."},
        {"title": "Bu binder ne değildir?", "content": "Gerçek yazdırma veya PDF export komutu çalıştırmaz."},
        {"title": "Executive reading order", "content": "Executive order."},
        {"title": "Operator reading order", "content": "Operator order."},
        {"title": "Analyst reading order", "content": "Analyst order."},
        {"title": "Maintainer reading order", "content": "Maintainer order."},
        {"title": "Reviewer reading order", "content": "Reviewer order."},
        {"title": "Appendix overview", "content": "Appendix."},
        {"title": "Safety boundary recap", "content": "Safety."},
        {"title": "No-go/safe-go recap", "content": "No-go/safe-go."},
        {"title": "PDF-ready but not PDF statement", "content": "PDF-ready but not PDF statement."}
    ]

def build_printable_binder_index(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"item": "binder_index"}])
    return df, summarize_printable_binder_index(df)

def summarize_printable_binder_packet(text: str) -> dict:
    return {"length": len(text)}

def summarize_printable_binder_index(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
