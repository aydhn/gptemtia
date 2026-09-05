from pathlib import Path
import pandas as pd

def build_final_local_operator_memory_book(project_root: Path, profile) -> tuple[str, dict]:
    sections = build_operator_memory_book_sections(project_root, profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_operator_memory_book(text)

def build_operator_memory_book_sections(project_root: Path, profile) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Local continuity memory book."},
        {"title": "Bu memory book ne değildir?", "content": "Gerçek persistent memory değildir. Yatırım tavsiyesi yoktur."},
        {"title": "Proje kimliği", "content": "Emtia-doviz offline bot."},
        {"title": "Phase 1-92 hafıza özeti", "content": "Phase 1-92 summary."},
        {"title": "Ana modül aileleri", "content": "Modules."},
        {"title": "Ana çıktı aileleri", "content": "Outputs."},
        {"title": "Kritik sınırlar", "content": "Boundaries."},
        {"title": "Operator için ilk okuma", "content": "Operator reading."},
        {"title": "Analyst için ilk okuma", "content": "Analyst reading."},
        {"title": "Maintainer için ilk okuma", "content": "Maintainer reading."},
        {"title": "Codex agent için ilk okuma", "content": "Codex reading."},
        {"title": "En çok karıştırılabilecek kavramlar", "content": "Concepts."},
        {"title": "No-go/safe-go özeti", "content": "No-go summary."},
        {"title": "Final boundary statement", "content": "Bu dokuman bir local continuity denemesidir."}
    ]

def summarize_operator_memory_book(text: str) -> dict:
    return {"length": len(text)}

def save_operator_memory_book(text: str, output_path: Path) -> Path:
    output_path.write_text(text, encoding="utf-8")
    return output_path