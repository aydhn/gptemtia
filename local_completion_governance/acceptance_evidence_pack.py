from pathlib import Path
import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile

def build_offline_acceptance_evidence_pack(project_root: Path, profile: LocalCompletionGovernanceProfile) -> tuple[str, dict]:
    sections = build_acceptance_evidence_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_acceptance_evidence_pack(text)

def build_acceptance_evidence_sections(profile: LocalCompletionGovernanceProfile) -> list[dict]:
    return [
        {"title": "Acceptance evidence amacı", "content": "Offline/local acceptance evidence pack."},
        {"title": "Bu evidence pack ne değildir?", "content": "Bu rapor offline/local closure synthesis ve completion governance rehearsal çıktısıdır; gerçek certification, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."},
        {"title": "Source/output/command evidence overview", "content": "Overview."},
        {"title": "Test/report/documentation evidence overview", "content": "Overview."},
        {"title": "Quality/safety evidence overview", "content": "Overview."},
        {"title": "Non-approval statement", "content": "Not approved."},
        {"title": "Limitation statement", "content": "Limitations."},
        {"title": "Manual review statement", "content": "Manual review required."}
    ]

def build_acceptance_evidence_index(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"index": "1", "item": "Acceptance Evidence"}])
    return df, summarize_acceptance_evidence_index(df)

def summarize_acceptance_evidence_pack(text: str) -> dict:
    return {"length": len(text)}

def summarize_acceptance_evidence_index(df: pd.DataFrame) -> dict:
    return {"count": len(df)}\n