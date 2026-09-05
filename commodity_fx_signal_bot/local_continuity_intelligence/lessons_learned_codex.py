from pathlib import Path
def build_lessons_learned_codex(project_root: Path, profile) -> tuple[str, dict]:
    sections = build_lessons_learned_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_lessons_learned_codex(text)
def build_lessons_learned_sections(profile) -> list[dict]:
    return [
        {"title": "Bu codex ne anlatır?", "content": "Lessons learned."},
        {"title": "Bu codex ne değildir?", "content": "Official lessons report değildir. Legal/compliance evidence değildir. Yatırım tavsiyesi yoktur."},
        {"title": "Architecture lessons", "content": "Arch lessons."},
        {"title": "DataLake/reporting lessons", "content": "DL lessons."},
        {"title": "Quality/testing lessons", "content": "Quality lessons."},
        {"title": "Safety/governance lessons", "content": "Safety lessons."},
        {"title": "Redteam/incident/release/longterm/completion/preservation lessons", "content": "Misc lessons."},
        {"title": "Operator handoff lessons", "content": "Handoff lessons."},
        {"title": "Future maintenance lessons", "content": "Maint lessons."},
        {"title": "Anti-misuse lessons", "content": "Anti-misuse lessons."},
        {"title": "Final boundary statement", "content": "Boundary."}
    ]
def summarize_lessons_learned_codex(text: str) -> dict:
    return {"length": len(text)}