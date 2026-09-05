from pathlib import Path
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile

def build_final_completion_governance_binder(project_root: Path, profile: LocalCompletionGovernanceProfile) -> tuple[str, dict]:
    sections = build_completion_governance_binder_sections(project_root, profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_completion_governance_binder(text)

def build_completion_governance_binder_sections(project_root: Path, profile: LocalCompletionGovernanceProfile) -> list[dict]:
    return [
        {"title": "Completion governance amacı", "content": "Offline/local completion governance."},
        {"title": "Bu binder ne değildir?", "content": "Bu rapor offline/local closure synthesis ve completion governance rehearsal çıktısıdır; gerçek certification, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."},
        {"title": "Closure synthesis recap", "content": "Recap."},
        {"title": "End-state certification rehearsal recap", "content": "Recap."},
        {"title": "Project freeze summary recap", "content": "Recap."},
        {"title": "Acceptance evidence pack recap", "content": "Recap."},
        {"title": "Criteria/evidence recap", "content": "Recap."},
        {"title": "Issue/unresolved recap", "content": "Recap."},
        {"title": "Handoff/closure checklist recap", "content": "Recap."},
        {"title": "Final readiness recap", "content": "Recap."},
        {"title": "No-go/safe-go recap", "content": "Recap."},
        {"title": "Exceptions/gaps/risks recap", "content": "Recap."},
        {"title": "Final boundary statement", "content": "Final boundary."}
    ]

def summarize_completion_governance_binder(text: str) -> dict:
    return {"length": len(text)}\n