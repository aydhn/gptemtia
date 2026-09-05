import pandas as pd
from pathlib import Path
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def build_terminal_archive_index_sections(profile: LocalFinalClosingProfile) -> list[dict]:
    return [
        {"title": "Archive index amacı", "content": "Local-only terminal archive index amacı."},
        {"title": "Bu archive index ne değildir?", "content": "Gerçek archive değildir. ZIP/TAR/RAR/7z oluşturmaz. Dosya kopyalama/taşıma/silme yok."},
        {"title": "Source map overview", "content": "Source map."},
        {"title": "Output map overview", "content": "Output map."},
        {"title": "Report map overview", "content": "Report map."},
        {"title": "Documentation map overview", "content": "Documentation map."},
        {"title": "Governance map overview", "content": "Governance map."},
        {"title": "Exclusion register overview", "content": "Excludes raw secrets and private data."},
        {"title": "No real archive statement", "content": "This does not create a real archive."},
        {"title": "Manual review statement", "content": "Manual review required."}
    ]

def build_local_only_terminal_archive_index(project_root: Path, profile: LocalFinalClosingProfile) -> tuple[str, dict]:
    sections = build_terminal_archive_index_sections(profile)
    lines = ["# Local-Only Terminal Archive Index\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    lines.append("Bu rapor offline/local final closing governance ve non-production seal rehearsal çıktısıdır; gerçek project lock, official constitution, official seal, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.")
    text = "\n".join(lines)
    return text, summarize_terminal_archive_index(text)

def summarize_terminal_archive_index(text: str) -> dict:
    return {"length": len(text)}
