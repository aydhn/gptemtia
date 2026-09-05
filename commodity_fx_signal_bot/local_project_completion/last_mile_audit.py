import pandas as pd
from pathlib import Path
from .completion_config import LocalProjectCompletionProfile

def build_last_mile_audit_sections(project_root: Path, profile: LocalProjectCompletionProfile) -> list[dict]:
    return [{"title": "Last-Mile Audit Rehearsal", "content": "Offline audit of final state."}]

def build_last_mile_audit_binder(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    sections = build_last_mile_audit_sections(project_root, profile)
    text = "# Last-Mile Audit Binder\n\n"
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
    return text, summarize_last_mile_audit_binder(text)

def summarize_last_mile_audit_binder(text: str) -> dict:
    return {"length": len(text), "note": "Not an official audit."}

def build_last_mile_audit_checklist_registry(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"check": "README exists", "status": "last_mile_audit_pass_rehearsal"}])
    return df, summarize_last_mile_audit_checklist(df)

def build_last_mile_audit_evidence_index(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"evidence": "docs/ARCHITECTURE.md", "type": "doc"}])
    return df, summarize_last_mile_audit_checklist(df)

def build_last_mile_audit_reading_order(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"order": 1, "item": "README.md"}])
    return df, summarize_last_mile_audit_checklist(df)

def summarize_last_mile_audit_checklist(df: pd.DataFrame) -> dict:
    return {"items": len(df), "note": "Checklist is not official acceptance."}
