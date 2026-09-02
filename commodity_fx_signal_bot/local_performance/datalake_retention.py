from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_datalake_retention_sections(profile: LocalPerformanceProfile) -> list[dict]:
    return [{"title": "Retention", "content": "Manuel yapiniz. Hukuki saklama tavsiyesi degildir."}]

def build_datalake_retention_rehearsal_guide(project_root: Path, profile: LocalPerformanceProfile) -> tuple[str, dict]:
    sections = build_datalake_retention_sections(profile)
    text = "# DataLake Retention Rehearsal Guide\n"
    for s in sections:
        text += f"\n## {s['title']}\n{s['content']}\n"
    return text, summarize_datalake_retention_guide(text)

def summarize_datalake_retention_guide(text: str) -> dict: return {"length": len(text)}
