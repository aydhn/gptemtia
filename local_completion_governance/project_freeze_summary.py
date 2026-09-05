from pathlib import Path
import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile

def build_terminal_project_freeze_summary(project_root: Path, profile: LocalCompletionGovernanceProfile) -> tuple[str, dict]:
    sections = build_project_freeze_summary_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_project_freeze_summary(text)

def build_project_freeze_summary_sections(profile: LocalCompletionGovernanceProfile) -> list[dict]:
    return [
        {"title": "Project freeze amacı", "content": "Offline/local project freeze summary."},
        {"title": "Bu freeze ne değildir?", "content": "Bu rapor offline/local closure synthesis ve completion governance rehearsal çıktısıdır; gerçek certification, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."},
        {"title": "Freeze snapshot overview", "content": "Overview."},
        {"title": "Freeze scope overview", "content": "Overview."},
        {"title": "Non-goals overview", "content": "Overview."},
        {"title": "Manual review ledger overview", "content": "Overview."},
        {"title": "Frozen-by-documentation statement", "content": "Documentation only."},
        {"title": "Not official freeze statement", "content": "Not official."},
        {"title": "Final boundary statement", "content": "Final boundary."}
    ]

def build_project_freeze_summary_index(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"index": "1", "item": "Freeze Summary"}])
    return df, summarize_project_freeze_summary_index(df)

def summarize_project_freeze_summary(text: str) -> dict:
    return {"length": len(text)}

def summarize_project_freeze_summary_index(df: pd.DataFrame) -> dict:
    return {"count": len(df)}\n