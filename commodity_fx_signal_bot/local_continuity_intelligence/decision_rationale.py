import pandas as pd
from pathlib import Path
from .continuity_models import DecisionRationaleItem

def build_decision_rationale_capsule(project_root: Path, profile) -> tuple[str, dict]:
    sections = build_decision_rationale_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_decision_rationale_capsule(text)

def build_decision_rationale_sections(profile) -> list[dict]:
    return [
        {"title": "Decision rationale", "content": "Official ADR değildir. Legal/compliance/broker/deploy/advice karar kaydı yoktur."}
    ]

def build_decision_rationale_registry(profile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([i.__dict__ for i in build_default_decision_rationales(profile)])
    return df, summarize_decision_rationale_registry(df)

def build_default_decision_rationales(profile) -> list[DecisionRationaleItem]:
    return [DecisionRationaleItem("d1", "a1", "t1", "s1", [], "note", ["Manual review boundary"])]

def summarize_decision_rationale_capsule(text: str) -> dict:
    return {"length": len(text)}

def summarize_decision_rationale_registry(df: pd.DataFrame) -> dict:
    return {"total": len(df)}