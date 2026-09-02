from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def build_repo_ergonomics_sections(profile: LocalSimplificationProfile) -> list[dict]:
    return [
        {"title": "Ilk nereden baslanir?", "content": "README.md okuyarak."},
        {"title": "Klasor aileleri nasil okunur?", "content": "ARCHITECTURE.md rehberliginde."},
        {"title": "Hangi scriptler sadece rapor uretir?", "content": "run_reports.py vb."},
        {"title": "Hangi ciktilar indeks niteligindedir?", "content": "data/lake/reports/index.csv"},
        {"title": "Hangi modullerde tekrar eden pattern tasir?", "content": "builder patternler."},
        {"title": "Hangi alanlarda sadelestirme adaylari var?", "content": "Optional slimming plan."},
        {"title": "Hangi alanlara dokunulmamali?", "content": "Core modules."},
        {"title": "Manual review workflow", "content": "Manuel incele."},
        {"title": "Safe future refactor rehearsal", "content": "Sadece dry-run."},
        {"title": "Neyi yapmamali?", "content": "Otomatik refactor yapmamali."}
    ]

def build_repo_ergonomics_rehearsal_guide(project_root: Path, profile: LocalSimplificationProfile) -> tuple[str, dict]:
    sections = build_repo_ergonomics_sections(profile)
    text = "# Repo Ergonomics Rehearsal Guide\n\n"
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
    return text, summarize_repo_ergonomics_guide(text)

def summarize_repo_ergonomics_guide(text: str) -> dict:
    return {"length": len(text), "warnings": ["Guide refactor talimati degildir.", "Live/broker/deploy/advice yok."]}
