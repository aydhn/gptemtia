import pandas as pd
from pathlib import Path
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def build_project_constitution_sections(profile: LocalFinalClosingProfile) -> list[dict]:
    return [
        {"title": "Constitution amacı", "content": "Ultimate offline project constitution amacı."},
        {"title": "Bu constitution ne değildir?", "content": "Bu constitution official constitution değildir. Legal authority, compliance approval, production approval, broker readiness, live trading approval, investment advice, release approval, project lock, archive generation değildir."},
        {"title": "Local/offline principle", "content": "Only local and offline operations are permitted."},
        {"title": "Research-only principle", "content": "System is limited to research purposes."},
        {"title": "Non-production principle", "content": "Not for production use."},
        {"title": "No-advice principle", "content": "No investment advice."},
        {"title": "No-broker/live-trading principle", "content": "No broker or live trading allowed."},
        {"title": "No-deployment/build/release principle", "content": "No deployment, real builds, or releases."},
        {"title": "Evidence/readability principle", "content": "Output is meant for readability and evidence gathering."},
        {"title": "Manual review principle", "content": "Manual review required."},
        {"title": "Preservation statement", "content": "Preservation statement info."},
        {"title": "Final boundary statement", "content": "Bu rapor offline/local final closing governance ve non-production seal rehearsal çıktısıdır; gerçek project lock, official constitution, official seal, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."}
    ]

def build_project_constitution_preservation_statement(profile: LocalFinalClosingProfile) -> tuple[str, dict]:
    text = "Preservation statement. Not an official retention policy."
    return text, {"length": len(text)}

def build_ultimate_offline_project_constitution(project_root: Path, profile: LocalFinalClosingProfile) -> tuple[str, dict]:
    sections = build_project_constitution_sections(profile)
    lines = ["# Ultimate Offline Project Constitution\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    return text, summarize_project_constitution(text)

def summarize_project_constitution(text: str) -> dict:
    return {"length": len(text)}
