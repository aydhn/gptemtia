import pandas as pd
from pathlib import Path
from .packaging_config import LocalDistributionPackagingProfile

def build_portable_docs_sections(profile: LocalDistributionPackagingProfile) -> list[dict]:
    return [
        {"title": "Portable docs amaci", "content": "Offline docs bundle."},
        {"title": "Bu bundle ne degildir?", "content": "Official handover degildir."},
        {"title": "Ilk okunacak dosyalar", "content": "README vs."},
        {"title": "Role-based okuma sirasi", "content": "Operator, Analyst."},
        {"title": "Offline HTML/printable/PDF-ready iliskisi", "content": "Offline reading ready."},
        {"title": "Review/atlas/continuity/preservation/completion iliskisi", "content": "Links to other outputs."},
        {"title": "Manual review required", "content": "Review needed."},
        {"title": "Final boundary statement", "content": "Yatirim tavsiyesi degildir."}
    ]

def build_portable_docs_bundle(project_root: Path, profile: LocalDistributionPackagingProfile) -> tuple[str, dict]:
    sections = build_portable_docs_sections(profile)
    text = "\n\n".join([f"## {s['title']}\n{s['content']}" for s in sections])
    text = f"# Portable Docs Bundle\n\n{text}"
    return text, summarize_portable_docs_bundle(text)

def build_portable_docs_manifest(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"doc": "README.md", "status": "included"}])
    return df, summarize_portable_docs_manifest(df)

def build_portable_docs_quickstart_packet(profile: LocalDistributionPackagingProfile) -> tuple[str, dict]:
    text = "# Quickstart\nThis is not a real release."
    return text, summarize_portable_docs_bundle(text)

def summarize_portable_docs_bundle(text: str) -> dict:
    return {"status": "generated", "length": len(text)}

def summarize_portable_docs_manifest(df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(df)}
