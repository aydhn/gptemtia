from typing import Tuple, Dict, List
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_degraded_mode_sections(profile: LocalIncidentResponseProfile) -> List[Dict]:
    return [
        {"title": "Degraded Mode Guide", "content": "Offline degraded mode template."}
    ]

def build_degraded_mode_rehearsal_guide(profile: LocalIncidentResponseProfile) -> Tuple[str, Dict]:
    sections = build_degraded_mode_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    text += "\n\nUyarı: Bu rapor offline/local incident-response rehearsal ve resilience supervision çıktısıdır; gerçek incident response, forensic analiz, production rollback, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
    summary = summarize_degraded_mode_guide(text)
    return text, summary

def summarize_degraded_mode_guide(text: str) -> Dict:
    return {
        "length": len(text),
        "note": "Guide generated."
    }
