from local_review_governance.review_config import LocalReviewGovernanceProfile

def build_review_governance_escalation_sections(profile: LocalReviewGovernanceProfile) -> list[dict]:
    return [
        {"title": "Escalation Policy", "content": "Manual offline escalation rehearsal."},
        {"title": "Not Real Escalation", "content": "Not an official incident tracker."}
    ]

def build_review_governance_escalation_rehearsal(profile: LocalReviewGovernanceProfile) -> tuple[str, dict]:
    sections = build_review_governance_escalation_sections(profile)
    lines = ["# Escalation Rehearsal\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    return text, summarize_review_governance_escalation(text)

def summarize_review_governance_escalation(text: str) -> dict:
    return {"length": len(text)}
