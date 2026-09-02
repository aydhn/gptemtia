from pathlib import Path
from .usability_config import LocalUsabilityProfile

def build_command_discoverability_sections(project_root: Path, profile: LocalUsabilityProfile) -> list[dict]:
    return [
        {"title": "Command Discoverability Guide", "content": "Bu guide komutları çalıştırmaz."},
        {"title": "Uyarı", "content": "Gerçek kullanıcı testi, telemetry, production usability approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."}
    ]

def build_command_discoverability_guide(project_root: Path, profile: LocalUsabilityProfile) -> tuple[str, dict]:
    sections = build_command_discoverability_sections(project_root, profile)
    text = "\n\n".join(f"## {s['title']}\n{s['content']}" for s in sections)
    return text, {"sections": len(sections)}

def summarize_command_discoverability_guide(text: str) -> dict:
    return {"length": len(text)}
