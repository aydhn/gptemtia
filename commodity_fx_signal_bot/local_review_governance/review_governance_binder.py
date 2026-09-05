from pathlib import Path
from local_review_governance.review_config import LocalReviewGovernanceProfile

def build_review_governance_binder_sections(project_root: Path, profile: LocalReviewGovernanceProfile) -> list[dict]:
    return [
        {"title": "Review governance amaci", "content": "Offline rehearsal only."},
        {"title": "Bu binder ne degildir?", "content": "Legal/compliance/production policy degildir."},
        {"title": "Human-review cockpit recap", "content": "Available."},
        {"title": "Manual approval ledger recap", "content": "Available."},
        {"title": "Expert review workbook recap", "content": "Available."},
        {"title": "Reviewer console recap", "content": "Available."},
        {"title": "Criteria/evidence recap", "content": "Available."},
        {"title": "Issue/unresolved recap", "content": "Available."},
        {"title": "Escalation rehearsal recap", "content": "Available."},
        {"title": "Non-goals recap", "content": "Available."},
        {"title": "No-go/safe-go recap", "content": "Available."},
        {"title": "Exceptions/gaps/risks recap", "content": "Available."},
        {"title": "Final boundary statement", "content": "No real deploy, live trading, investment advice."}
    ]

def build_terminal_review_governance_binder(project_root: Path, profile: LocalReviewGovernanceProfile) -> tuple[str, dict]:
    sections = build_review_governance_binder_sections(project_root, profile)
    lines = ["# Terminal Review Governance Binder\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    return text, summarize_review_governance_binder(text)

def summarize_review_governance_binder(text: str) -> dict:
    return {"length": len(text)}
