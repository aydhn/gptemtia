import os
import pandas as pd
from typing import Dict, Tuple, List
from pathlib import Path

# Mock imports for the generator structure
# We write the files directly

def write_incident_domain_registry():
    code = """import pandas as pd
from typing import Tuple, Dict, List
from local_incident_response.incident_config import LocalIncidentResponseProfile
from local_incident_response.incident_models import IncidentDomain, build_incident_domain_id, incident_domain_to_dict

def build_default_incident_domains(profile: LocalIncidentResponseProfile) -> List[IncidentDomain]:
    labels = [
        "incident_rehearsal_domain", "safety_event_domain", "incident_taxonomy_domain",
        "incident_triage_domain", "incident_classification_domain", "rollback_rehearsal_domain",
        "containment_rehearsal_domain", "degraded_mode_domain", "recovery_rehearsal_domain",
        "resilience_supervision_domain", "post_incident_review_domain", "corrective_action_domain",
        "escalation_domain", "quality_validation_domain"
    ]
    domains = []
    for lbl in labels:
        domains.append(IncidentDomain(
            domain_id=build_incident_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Local/offline mock domain for {lbl}",
            required_outputs=["mock_report"],
            warnings=["Offline context only."]
        ))
    return domains

def build_incident_domain_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    domains = build_default_incident_domains(profile)
    df = pd.DataFrame([incident_domain_to_dict(d) for d in domains])
    summary = summarize_incident_domains(df)
    return df, summary

def summarize_incident_domains(domain_df: pd.DataFrame) -> Dict:
    return {
        "total_domains": len(domain_df) if domain_df is not None else 0,
        "note": "This is not an official incident response scope."
    }
"""
    with open("local_incident_response/incident_domain_registry.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_rehearsal_packet():
    code = """from pathlib import Path
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
    text = "\\n\\n".join([f"# {s['title']}\\n{s['content']}" for s in sections])
    text += "\\n\\nUyarı: Bu rapor offline/local incident-response rehearsal ve resilience supervision çıktısıdır; gerçek incident response, forensic analiz, production rollback, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
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
"""
    with open("local_incident_response/incident_rehearsal_packet.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_safety_event_register():
    code = """import pandas as pd
from typing import Tuple, Dict, List
from local_incident_response.incident_config import LocalIncidentResponseProfile
from local_incident_response.incident_models import SafetyEvent, build_safety_event_id, safety_event_to_dict

def build_default_safety_events(profile: LocalIncidentResponseProfile) -> List[SafetyEvent]:
    categories = [
        "event_boundary_breach", "event_unsafe_output", "event_forbidden_capability_request",
        "event_secret_exposure", "event_file_action_request", "event_cloud_publish_request",
        "event_live_trading_broker_request", "event_investment_advice_request",
        "event_model_deployment_request", "event_external_llm_api_request"
    ]
    events = []
    for cat in categories:
        events.append(SafetyEvent(
            event_id=build_safety_event_id(cat, cat),
            event_name=cat,
            event_category=cat,
            severity_label="severity_medium",
            abstract_description="Mock safety event.",
            expected_manual_action="Review offline.",
            evidence_refs=[],
            manual_review_required=True,
            warnings=["Offline validation only."]
        ))
    return events

def build_safety_event_register(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    events = build_default_safety_events(profile)
    df = pd.DataFrame([safety_event_to_dict(e) for e in events])
    summary = summarize_safety_event_register(df)
    return df, summary

def summarize_safety_event_register(event_df: pd.DataFrame) -> Dict:
    return {
        "total_events": len(event_df) if event_df is not None else 0,
        "note": "This is a local safety register, not a real incident record."
    }
"""
    with open("local_incident_response/safety_event_register.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_safety_event_taxonomy():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile
from local_incident_response.incident_labels import list_safety_event_category_labels

def build_default_safety_event_taxonomy(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    labels = list_safety_event_category_labels()
    data = [{"category": lbl, "description": "Offline taxonomy label"} for lbl in labels]
    return pd.DataFrame(data)

def build_safety_event_taxonomy(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_safety_event_taxonomy(profile)
    summary = summarize_safety_event_taxonomy(df)
    return df, summary

def summarize_safety_event_taxonomy(df: pd.DataFrame) -> Dict:
    return {
        "total_categories": len(df) if df is not None else 0,
        "note": "Offline safety taxonomy."
    }
"""
    with open("local_incident_response/safety_event_taxonomy.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_severity():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile
from local_incident_response.incident_labels import list_severity_labels

def build_default_incident_severity_taxonomy(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    labels = list_severity_labels()
    data = [{"severity_label": lbl, "description": "Offline severity."} for lbl in labels]
    return pd.DataFrame(data)

def classify_incident_severity(event_category: str, profile: LocalIncidentResponseProfile) -> str:
    return "severity_medium"

def build_incident_severity_taxonomy(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_incident_severity_taxonomy(profile)
    summary = summarize_incident_severity_taxonomy(df)
    return df, summary

def summarize_incident_severity_taxonomy(df: pd.DataFrame) -> Dict:
    return {
        "total_severities": len(df) if df is not None else 0,
        "note": "Offline severity taxonomy, not real production severity."
    }
"""
    with open("local_incident_response/incident_severity.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_triage():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_incident_triage_items(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [
        {"triage_step": "Step 1", "description": "Offline verification."},
        {"triage_step": "Step 2", "description": "Mock triage."}
    ]
    return pd.DataFrame(data)

def build_incident_triage_checklist(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_incident_triage_items(profile)
    summary = summarize_incident_triage_checklist(df)
    return df, summary

def summarize_incident_triage_checklist(df: pd.DataFrame) -> Dict:
    return {
        "total_triage_steps": len(df) if df is not None else 0,
        "note": "Not a real incident triage."
    }
"""
    with open("local_incident_response/incident_triage.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_classification():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_incident_classification_items(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [
        {"class_name": "Class A", "criteria": "Mock criteria."},
        {"class_name": "Class B", "criteria": "Mock criteria 2."}
    ]
    return pd.DataFrame(data)

def build_incident_classification_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_incident_classification_items(profile)
    summary = summarize_incident_classification_registry(df)
    return df, summary

def summarize_incident_classification_registry(df: pd.DataFrame) -> Dict:
    return {
        "total_classes": len(df) if df is not None else 0,
        "note": "Not a compliance classification."
    }
"""
    with open("local_incident_response/incident_classification.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_specific_event_registries():
    names = [
        "boundary_breach", "unsafe_output", "forbidden_capability",
        "secret_exposure", "file_action", "cloud_publish",
        "live_trading_broker", "model_deployment", "external_llm_api"
    ]
    
    for name in names:
        code = f"""import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_{name}_event_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    data = [
        {{
            "event_name": "mock_{name}_event",
            "event_category": "event_{name}_request" if not "{name}".endswith("events") else "event_{name}",
            "severity_label": "severity_info",
            "abstract_description": "Mock offline {name} event.",
            "expected_manual_action": "No action.",
            "no_go_boundary": True,
            "evidence_refs": "none",
            "warnings": "Offline mock only."
        }}
    ]
    df = pd.DataFrame(data)
    summary = summarize_{name}_events(df)
    return df, summary

def summarize_{name}_events(df: pd.DataFrame) -> Dict:
    return {{
        "total_events": len(df) if df is not None else 0,
        "note": "Not a real event registry."
    }}
"""
        # Rename module for forbidden capability to match specification
        if name == "forbidden_capability":
            mod_name = "forbidden_capability_events.py"
        elif name == "live_trading_broker":
            mod_name = "live_trading_broker_events.py"
        elif name == "external_llm_api":
            mod_name = "external_llm_api_events.py"
        else:
            mod_name = f"{name}_events.py"

        with open(f"local_incident_response/{mod_name}", "w", encoding="utf-8") as f:
            f.write(code)

if __name__ == "__main__":
    write_incident_domain_registry()
    write_incident_rehearsal_packet()
    write_safety_event_register()
    write_safety_event_taxonomy()
    write_incident_severity()
    write_incident_triage()
    write_incident_classification()
    write_specific_event_registries()
