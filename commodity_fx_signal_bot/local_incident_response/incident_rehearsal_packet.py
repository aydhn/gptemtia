from pathlib import Path
from typing import Tuple, Dict, List
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_incident_rehearsal_sections(project_root: Path, profile: LocalIncidentResponseProfile) -> List[Dict]:
    return [
        {"title": "Amaç ve Kapsam", "content": "Offline rehearsal for local incidents."},
        {"title": "Bu paket ne değildir?", "content": "Gerçek incident report değildir."},
        {"title": "Incident rehearsal overview", "content": "Overview text."},
        {"title": "Safety event register recap", "content": "Recap of events."},
        {"title": "Severity/triage recap", "content": "Recap of severity."},
        {"title": "Rollback decision boundary recap", "content": "Rollback boundary."},
        {"title": "Containment/degraded-mode/recovery rehearsal recap", "content": "Containment text."},
        {"title": "Post-incident review templates", "content": "Templates text."},
        {"title": "Evidence snapshot and reading order", "content": "Evidence text."},
        {"title": "Corrective-action rehearsal", "content": "Corrective action text."},
        {"title": "Escalation decision registry", "content": "Escalation text."},
        {"title": "No-go/safe-go recap", "content": "No-go safe-go boundaries."},
        {"title": "Open gaps and risks", "content": "Gaps and risks text."},
        {"title": "Final boundary statement", "content": "Gerçek operasyon yoktur."}
    ]

def build_final_local_incident_response_rehearsal_packet(project_root: Path, profile: LocalIncidentResponseProfile) -> Tuple[str, Dict]:
    sections = build_incident_rehearsal_sections(project_root, profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    text += "\n\nUyarı: Bu rapor offline/local incident-response rehearsal ve resilience supervision çıktısıdır; gerçek incident response, forensic analiz, production rollback, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
    summary = summarize_incident_rehearsal_packet(text)
    return text, summary

def summarize_incident_rehearsal_packet(text: str) -> Dict:
    return {
        "length": len(text),
        "note": "Rehearsal packet generated successfully."
    }

def save_incident_rehearsal_packet(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
