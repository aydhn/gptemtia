"""PDF ready docs."""
import pandas as pd
from pathlib import Path
from .export_config import LocalDocumentationExportProfile

def build_pdf_ready_documentation_packet(project_root: Path, profile: LocalDocumentationExportProfile) -> tuple[str, dict]:
    sections = build_pdf_ready_documentation_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_pdf_ready_documentation_packet(text)

def build_pdf_ready_documentation_sections(profile: LocalDocumentationExportProfile) -> list[dict]:
    return [
        {"title": "PDF-Ready Docs", "content": "This is a PDF ready, non-PDF document."}
    ]

def build_pdf_ready_markdown_packet(profile: LocalDocumentationExportProfile) -> tuple[str, dict]:
    text = "# PDF-ready Markdown\nNo real PDF binary generated."
    return text, summarize_pdf_ready_documentation_packet(text)

def build_pdf_ready_html_packet(profile: LocalDocumentationExportProfile) -> tuple[str, dict]:
    html = "<html><body><h1>PDF-ready HTML</h1><p>No real PDF binary generated.</p></body></html>"
    return html, summarize_pdf_ready_documentation_packet(html)

def summarize_pdf_ready_documentation_packet(text: str) -> dict:
    return {"length": len(text)}
