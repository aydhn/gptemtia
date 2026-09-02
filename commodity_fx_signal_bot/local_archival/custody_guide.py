"""
Custody Guide.
"""
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile

def build_custody_guide_sections(profile: LocalArchivalProfile) -> list[dict]:
    return [
        {"title": "Overview", "content": "This is a dry-run guide for long-term custody rehearsal."},
        {"title": "Disclaimer", "content": "Not a legal advice or official custody chain."},
        {"title": "Storage", "content": "All artifacts are stored locally in data/lake."}
    ]

def build_long_term_custody_rehearsal_guide(profile: LocalArchivalProfile) -> tuple[str, dict]:
    sections = build_custody_guide_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_custody_guide(text)

def save_long_term_custody_rehearsal_guide(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    return output_path

def summarize_custody_guide(text: str) -> dict:
    return {"guide_length": len(text) if text else 0}
