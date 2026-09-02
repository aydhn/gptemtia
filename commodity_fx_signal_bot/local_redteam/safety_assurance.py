from pathlib import Path
import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_safety_assurance_sections(project_root: Path, profile: LocalRedTeamProfile) -> list[dict]:
    return [
        {"title": "Overview", "content": "This is an offline safety assurance rehearsal."},
        {"title": "Disclaimer", "content": "Not a production safety approval, real attack, or investment advice."}
    ]

def build_safety_assurance_summary(project_root: Path, profile: LocalRedTeamProfile) -> tuple[str, dict]:
    sections = build_safety_assurance_sections(project_root, profile)
    text = "SAFETY ASSURANCE SUMMARY\n========================\n\n"
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
    return text, summarize_safety_assurance_summary(text)

def build_safety_assurance_evidence_index(project_root: Path, profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"evidence_id": "ev_1", "description": "Offline rehearsal evidence", "warnings": "Not a real audit proof."}])
    return df, summarize_safety_assurance_evidence_index(df)

def summarize_safety_assurance_summary(text: str) -> dict:
    return {"length": len(text), "note": "Not a real certification."}

def summarize_safety_assurance_evidence_index(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Not an audit proof."}
