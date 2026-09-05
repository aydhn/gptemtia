"""Presentation freeze."""
import pandas as pd
from pathlib import Path
from .export_config import LocalDocumentationExportProfile

def build_archival_presentation_freeze_packet(project_root: Path, profile: LocalDocumentationExportProfile) -> tuple[str, dict]:
    sections = build_presentation_freeze_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_presentation_freeze_packet(text)

def build_presentation_freeze_sections(profile: LocalDocumentationExportProfile) -> list[dict]:
    return [
        {"title": "Presentation-freeze amacı", "content": "Archival documentation preparation."},
        {"title": "Bu paket ne değildir?", "content": "Gerçek sunum, Slide deck, PowerPoint değildir."},
        {"title": "Slide deck değildir", "content": "No slides."},
        {"title": "PowerPoint değildir", "content": "No pptx."},
        {"title": "Archival narrative overview", "content": "Narrative."},
        {"title": "Final system story", "content": "System story."},
        {"title": "Review governance recap", "content": "Review recap."},
        {"title": "Atlas/continuity/preservation/completion recap", "content": "Recap."},
        {"title": "Safety boundary recap", "content": "Safety recap."},
        {"title": "No-go/safe-go recap", "content": "No-go recap."},
        {"title": "Manual review statement", "content": "Manual review required."}
    ]

def summarize_presentation_freeze_packet(text: str) -> dict:
    return {"length": len(text)}
