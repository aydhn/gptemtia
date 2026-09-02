from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_report_rotation_sections(profile: LocalPerformanceProfile) -> list[dict]:
    return [{"title": "Rotation", "content": "Manuel yapiniz. Otomatik rotation uygulamaz."}]

def build_report_rotation_rehearsal_guide(project_root: Path, profile: LocalPerformanceProfile) -> tuple[str, dict]:
    sections = build_report_rotation_sections(profile)
    text = "# Report Rotation Rehearsal Guide\n"
    for s in sections:
        text += f"\n## {s['title']}\n{s['content']}\n"
    return text, summarize_report_rotation_guide(text)

def summarize_report_rotation_guide(text: str) -> dict: return {"length": len(text)}
