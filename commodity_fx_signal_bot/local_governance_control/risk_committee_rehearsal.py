from pathlib import Path
from .governance_control_config import LocalGovernanceControlProfile

def build_risk_committee_rehearsal_sections(profile: LocalGovernanceControlProfile) -> list[dict]:
    return [
        {"title": "Risk committee rehearsal purpose", "content": "Offline risk komitesi provası."},
        {"title": "What is reviewed", "content": "Sistem sağlığı ve sınırlar."},
        {"title": "What cannot be approved", "content": "Gerçek yatırım kararları ve canlı operasyon onaylanamaz."},
        {"title": "No-go review", "content": "No-go koşullarının kontrolü."},
        {"title": "Quality/risk summaries", "content": "Kalite ve risk durumları."},
        {"title": "Manual approval ledger review", "content": "Onay defterinin incelenmesi."},
        {"title": "Escalation matrix review", "content": "Manuel eskalasyon akışı."},
        {"title": "Open decision review", "content": "Açık kararların provası."},
        {"title": "Follow-up action rehearsal", "content": "Takip eylemleri."},
        {"title": "Boundary statement", "content": "Bu doküman risk komitesi kararı değildir."}
    ]

def build_risk_committee_rehearsal_pack(project_root: Path, profile: LocalGovernanceControlProfile) -> tuple[str, dict]:
    sections = build_risk_committee_rehearsal_sections(profile)
    lines = ["# Risk Committee Rehearsal Pack", ""]
    for s in sections:
        lines.append(f"## {s['title']}")
        lines.append(s["content"])
        lines.append("")
    text = "\n".join(lines)
    return text, summarize_risk_committee_rehearsal_pack(text)

def summarize_risk_committee_rehearsal_pack(text: str) -> dict:
    if not text:
        return {"length": 0, "sections": 0}
    return {"length": len(text), "sections": text.count("## ")}

def save_risk_committee_rehearsal_pack(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
