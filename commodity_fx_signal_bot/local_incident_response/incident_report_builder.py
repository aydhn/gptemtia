import pandas as pd
from typing import Optional, Dict

def build_incident_disclaimer() -> str:
    return "\n\nUyarı: Bu rapor offline/local incident-response rehearsal ve resilience supervision çıktısıdır; gerçek incident response, forensic analiz, production rollback, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n"

def build_incident_domain_registry_markdown_report(summary: Dict, domain_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Incident Domain Registry\n{summary}\n" + build_incident_disclaimer()

def build_incident_rehearsal_packet_markdown_report(summary: Dict, packet_text: Optional[str] = None) -> str:
    return f"# Incident Rehearsal Packet\n{summary}\n" + build_incident_disclaimer()

def build_safety_event_register_markdown_report(summary: Dict, event_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Safety Event Register\n{summary}\n" + build_incident_disclaimer()

def build_rollback_decision_playbook_markdown_report(summary: Dict, playbook_text: Optional[str] = None) -> str:
    return f"# Rollback Decision Playbook\n{summary}\n" + build_incident_disclaimer()

def build_post_incident_review_template_markdown_report(summary: Dict, template_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Post-Incident Review Templates\n{summary}\n" + build_incident_disclaimer()

def build_incident_quality_markdown_report(summary: Dict, quality: Optional[Dict] = None) -> str:
    return f"# Incident Quality\n{summary}\n" + build_incident_disclaimer()

def build_incident_status_markdown_report(summary: Dict, status_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Incident Status\n{summary}\n" + build_incident_disclaimer()
