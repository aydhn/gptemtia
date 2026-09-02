from typing import Tuple, Dict, List
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_rollback_decision_sections(profile: LocalIncidentResponseProfile) -> List[Dict]:
    return [
        {"title": "Rollback Decision Playbook", "content": "Offline rollback decision template."},
        {"title": "Rules", "content": "No real rollback allowed."}
    ]

def build_rollback_decision_playbook(profile: LocalIncidentResponseProfile) -> Tuple[str, Dict]:
    sections = build_rollback_decision_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    text += "\n\nUyarı: Bu rapor offline/local incident-response rehearsal ve resilience supervision çıktısıdır; gerçek incident response, forensic analiz, production rollback, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
    summary = summarize_rollback_decision_playbook(text)
    return text, summary

def summarize_rollback_decision_playbook(text: str) -> Dict:
    return {
        "length": len(text),
        "note": "Playbook generated."
    }
