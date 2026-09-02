
from pathlib import Path
from local_closure.closure_config import LocalClosureProfile

def build_aftercare_sections(profile: LocalClosureProfile) -> list[dict]:
    return [
        {"title": "Handoff", "content": "All artifacts are local."},
        {"title": "Aftercare", "content": "No live support."}
    ]

def build_closure_handoff_aftercare_guide(profile: LocalClosureProfile) -> tuple[str, dict]:
    sections = build_aftercare_sections(profile)
    text = "# Handoff Aftercare Guide\n\n"
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
    summary = summarize_handoff_aftercare_guide(text)
    return text, summary

def summarize_handoff_aftercare_guide(text: str) -> dict:
    return {"len": len(text)}
