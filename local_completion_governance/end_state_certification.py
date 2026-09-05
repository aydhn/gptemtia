from pathlib import Path
import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile

def build_end_state_certification_rehearsal(project_root: Path, profile: LocalCompletionGovernanceProfile) -> tuple[str, dict]:
    sections = build_end_state_certification_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_end_state_certification_rehearsal(text)

def build_end_state_certification_sections(profile: LocalCompletionGovernanceProfile) -> list[dict]:
    return [
        {"title": "Certification rehearsal amacı", "content": "Offline/local end-state certification rehearsal."},
        {"title": "Bu certification ne değildir?", "content": "Bu rapor offline/local closure synthesis ve completion governance rehearsal çıktısıdır; gerçek certification, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."},
        {"title": "End-state criteria overview", "content": "Criteria overview."},
        {"title": "Boundary overview", "content": "Boundary overview."},
        {"title": "Evidence map overview", "content": "Evidence map overview."},
        {"title": "Limitation register overview", "content": "Limitation register overview."},
        {"title": "Non-certification statement", "content": "Not certified."},
        {"title": "Manual review required", "content": "Manual review required."},
        {"title": "Final boundary statement", "content": "Final boundary."}
    ]

def summarize_end_state_certification_rehearsal(text: str) -> dict:
    return {"length": len(text)}
