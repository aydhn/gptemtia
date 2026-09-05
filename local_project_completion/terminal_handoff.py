from .completion_config import LocalProjectCompletionProfile

def build_terminal_handoff_sections(profile: LocalProjectCompletionProfile) -> list[dict]:
    return [
        {"title": "Kim okumalı?", "content": "Maintainers and Operators."},
        {"title": "İlk okunacak dosyalar", "content": "README.md, docs/ARCHITECTURE.md"},
        {"title": "No-go/safe-go sınırları", "content": "Do not use for live trading."},
        {"title": "Final boundary statement", "content": "Terminal handoff is a documentation layer, not a deployment package."}
    ]

def build_terminal_handoff_pack(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    sections = build_terminal_handoff_sections(profile)
    text = "# Terminal Handoff Pack\n\n"
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
    return text, summarize_terminal_handoff_pack(text)

def summarize_terminal_handoff_pack(text: str) -> dict:
    return {"length": len(text), "note": "Handoff pack is not official acceptance."}
