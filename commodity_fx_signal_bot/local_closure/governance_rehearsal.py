
from pathlib import Path
from local_closure.closure_config import LocalClosureProfile

def build_governance_rehearsal_sections(profile: LocalClosureProfile) -> list[dict]:
    return [
        {"title": "Local-only Governance Prensibi", "content": "Herhangi bir cloud veya live değişiklik yasaktır."},
        {"title": "Manual Review Ritmi", "content": "Değişiklikler manuel onaydan geçmelidir."},
        {"title": "Change Request Intake", "content": "Offline araştırma odaklı CR'lar kabul edilir."},
        {"title": "Future Phase Approval Rehearsal", "content": "Fazlar mock-approval alır."},
        {"title": "Safety Boundary Review", "content": "Kuralların ihlal edilmediği test edilir."},
        {"title": "Documentation Review", "content": "Dokümantasyon güncelliği sağlanır."},
        {"title": "Evidence Review", "content": "Kanıtların tamlığı incelenir."},
        {"title": "Roadmap Triage", "content": "Önceliklendirme yapılır."},
        {"title": "No-go Escalation", "content": "Live trade varsa reddedilir."},
        {"title": "Aftercare Communication", "content": "Bakım planı mock olarak işletilir."},
        {"title": "Neyi Yapmamalı?", "content": "Canlı ortama kod atılmamalı."}
    ]

def build_post_project_governance_rehearsal_guide(project_root: Path, profile: LocalClosureProfile) -> tuple[str, dict]:
    sections = build_governance_rehearsal_sections(profile)
    text = "# Post-Project Governance Rehearsal Guide\n\n"
    text += "> **UYARI**: Bu rapor offline/local v1.0 closure rehearsal ve final meta-review çıktısıdır; gerçek v1.0 release, production release, compliance sertifikası, resmi proje kapanışı, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    for s in sections:
        text += f"## {s['title']}\n{s['content']}\n\n"
    summary = summarize_governance_rehearsal_guide(text)
    return text, summary

def summarize_governance_rehearsal_guide(text: str) -> dict:
    return {
        "length": len(text),
        "has_warning": "UYARI" in text
    }
