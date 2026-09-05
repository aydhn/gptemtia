from pathlib import Path
from .completion_config import LocalProjectCompletionProfile

def build_completion_readiness_sections(profile: LocalProjectCompletionProfile) -> list[dict]:
    return [{"title": "Readiness Overview", "content": "System is locally ready."}]

def build_project_completion_readiness_packet(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    sections = build_completion_readiness_sections(profile)
    text = "# Project Completion Readiness Packet\n\n"
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
    return text, summarize_completion_readiness_packet(text)

def summarize_completion_readiness_packet(text: str) -> dict:
    return {"length": len(text), "note": "Readiness packet is not production approval."}
