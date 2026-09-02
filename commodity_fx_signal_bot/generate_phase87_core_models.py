import os
from pathlib import Path

def patch_settings():
    settings_file = "config/settings.py"
    with open(settings_file, "r", encoding="utf-8") as f:
        content = f.read()

    new_settings = """
    local_incident_response_enabled: bool = True
    default_local_incident_response_profile: str = "balanced_local_incident_response"
    local_incident_response_default_language: str = "tr"
    local_incident_response_dry_run_default: bool = True
    local_incident_response_allow_real_incident_response: bool = False
    local_incident_response_allow_real_rollback: bool = False
    local_incident_response_allow_forensic_analysis: bool = False
    local_incident_response_allow_production_recovery: bool = False
    local_incident_response_allow_live_system_halt: bool = False
    local_incident_response_allow_broker_halt_instruction: bool = False
    local_incident_response_allow_compliance_signoff: bool = False
    local_incident_response_allow_legal_signoff: bool = False
    local_incident_response_allow_production_recovery_claim: bool = False
    local_incident_response_allow_live_trading_claim: bool = False
    local_incident_response_allow_broker_readiness_claim: bool = False
    local_incident_response_allow_investment_advice: bool = False
    local_incident_response_allow_model_deployment_claim: bool = False
    local_incident_response_allow_telemetry: bool = False
    local_incident_response_allow_dashboard_creation: bool = False
    local_incident_response_allow_gui_creation: bool = False
    local_incident_response_allow_tui_creation: bool = False
    local_incident_response_allow_cloud_upload: bool = False
    local_incident_response_allow_package_publish: bool = False
    local_incident_response_allow_external_service: bool = False
    local_incident_response_allow_external_llm: bool = False
    local_incident_response_allow_file_modification: bool = False
    local_incident_response_allow_file_deletion: bool = False
    local_incident_response_allow_file_move: bool = False
    local_incident_response_allow_overwrite: bool = False
    local_incident_response_scan_docs: bool = True
    local_incident_response_scan_reports: bool = True
    local_incident_response_scan_data_lake: bool = True
    local_incident_response_scan_scripts: bool = True
    local_incident_response_scan_tests: bool = True
    local_incident_response_scan_generated_docs: bool = True
    local_incident_response_scan_redteam_outputs: bool = True
    local_incident_response_scan_governance_outputs: bool = True
    local_incident_response_scan_safety_outputs: bool = True
    local_incident_response_max_items: int = 500000
    local_incident_response_max_events: int = 10000
    local_incident_response_min_readiness_score: float = 0.40
    local_incident_response_min_quality_score: float = 0.40
    local_incident_response_save_reports: bool = True
"""
    if "local_incident_response_enabled" not in content:
        content = content.replace("class Settings(BaseSettings):", f"class Settings(BaseSettings):\n{new_settings}")
        with open(settings_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated settings.py")

def patch_env():
    env_file = ".env.example"
    with open(env_file, "r", encoding="utf-8") as f:
        content = f.read()

    new_env = """
LOCAL_INCIDENT_RESPONSE_ENABLED=true
DEFAULT_LOCAL_INCIDENT_RESPONSE_PROFILE=balanced_local_incident_response
LOCAL_INCIDENT_RESPONSE_DEFAULT_LANGUAGE=tr
LOCAL_INCIDENT_RESPONSE_DRY_RUN_DEFAULT=true
LOCAL_INCIDENT_RESPONSE_ALLOW_REAL_INCIDENT_RESPONSE=false
LOCAL_INCIDENT_RESPONSE_ALLOW_REAL_ROLLBACK=false
LOCAL_INCIDENT_RESPONSE_ALLOW_FORENSIC_ANALYSIS=false
LOCAL_INCIDENT_RESPONSE_ALLOW_PRODUCTION_RECOVERY=false
LOCAL_INCIDENT_RESPONSE_ALLOW_LIVE_SYSTEM_HALT=false
LOCAL_INCIDENT_RESPONSE_ALLOW_BROKER_HALT_INSTRUCTION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_COMPLIANCE_SIGNOFF=false
LOCAL_INCIDENT_RESPONSE_ALLOW_LEGAL_SIGNOFF=false
LOCAL_INCIDENT_RESPONSE_ALLOW_PRODUCTION_RECOVERY_CLAIM=false
LOCAL_INCIDENT_RESPONSE_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_INCIDENT_RESPONSE_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_INCIDENT_RESPONSE_ALLOW_INVESTMENT_ADVICE=false
LOCAL_INCIDENT_RESPONSE_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_INCIDENT_RESPONSE_ALLOW_TELEMETRY=false
LOCAL_INCIDENT_RESPONSE_ALLOW_DASHBOARD_CREATION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_GUI_CREATION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_TUI_CREATION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_CLOUD_UPLOAD=false
LOCAL_INCIDENT_RESPONSE_ALLOW_PACKAGE_PUBLISH=false
LOCAL_INCIDENT_RESPONSE_ALLOW_EXTERNAL_SERVICE=false
LOCAL_INCIDENT_RESPONSE_ALLOW_EXTERNAL_LLM=false
LOCAL_INCIDENT_RESPONSE_ALLOW_FILE_MODIFICATION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_FILE_DELETION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_FILE_MOVE=false
LOCAL_INCIDENT_RESPONSE_ALLOW_OVERWRITE=false
LOCAL_INCIDENT_RESPONSE_SCAN_DOCS=true
LOCAL_INCIDENT_RESPONSE_SCAN_REPORTS=true
LOCAL_INCIDENT_RESPONSE_SCAN_DATA_LAKE=true
LOCAL_INCIDENT_RESPONSE_SCAN_SCRIPTS=true
LOCAL_INCIDENT_RESPONSE_SCAN_TESTS=true
LOCAL_INCIDENT_RESPONSE_SCAN_GENERATED_DOCS=true
LOCAL_INCIDENT_RESPONSE_SCAN_REDTEAM_OUTPUTS=true
LOCAL_INCIDENT_RESPONSE_SCAN_GOVERNANCE_OUTPUTS=true
LOCAL_INCIDENT_RESPONSE_SCAN_SAFETY_OUTPUTS=true
LOCAL_INCIDENT_RESPONSE_MAX_ITEMS=500000
LOCAL_INCIDENT_RESPONSE_MAX_EVENTS=10000
LOCAL_INCIDENT_RESPONSE_MIN_READINESS_SCORE=0.40
LOCAL_INCIDENT_RESPONSE_MIN_QUALITY_SCORE=0.40
LOCAL_INCIDENT_RESPONSE_SAVE_REPORTS=true
"""
    if "LOCAL_INCIDENT_RESPONSE_ENABLED" not in content:
        with open(env_file, "a", encoding="utf-8") as f:
            f.write(new_env)
        print("Updated .env.example")

def patch_paths():
    paths_file = "config/paths.py"
    with open(paths_file, "r", encoding="utf-8") as f:
        content = f.read()

    new_paths = """
    # Local Incident Response
    LOCAL_INCIDENT_RESPONSE_DIR = LAKE_DIR / "local_incident_response"
    LOCAL_INCIDENT_RESPONSE_PROFILES_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "profiles"
    LOCAL_INCIDENT_RESPONSE_DOMAINS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "domains"
    LOCAL_INCIDENT_RESPONSE_REHEARSAL_PACKET_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "rehearsal_packet"
    LOCAL_INCIDENT_RESPONSE_EVENTS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "events"
    LOCAL_INCIDENT_RESPONSE_TAXONOMY_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "taxonomy"
    LOCAL_INCIDENT_RESPONSE_SEVERITY_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "severity"
    LOCAL_INCIDENT_RESPONSE_TRIAGE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "triage"
    LOCAL_INCIDENT_RESPONSE_CLASSIFICATION_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "classification"
    LOCAL_INCIDENT_RESPONSE_BOUNDARY_BREACH_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "boundary_breach"
    LOCAL_INCIDENT_RESPONSE_UNSAFE_OUTPUTS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "unsafe_outputs"
    LOCAL_INCIDENT_RESPONSE_FORBIDDEN_CAPABILITIES_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "forbidden_capabilities"
    LOCAL_INCIDENT_RESPONSE_SECRET_EXPOSURE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "secret_exposure"
    LOCAL_INCIDENT_RESPONSE_FILE_ACTIONS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "file_actions"
    LOCAL_INCIDENT_RESPONSE_CLOUD_PUBLISH_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "cloud_publish"
    LOCAL_INCIDENT_RESPONSE_LIVE_BROKER_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "live_broker"
    LOCAL_INCIDENT_RESPONSE_MODEL_DEPLOYMENT_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "model_deployment"
    LOCAL_INCIDENT_RESPONSE_EXTERNAL_LLM_API_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "external_llm_api"
    LOCAL_INCIDENT_RESPONSE_ROLLBACK_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "rollback"
    LOCAL_INCIDENT_RESPONSE_CONTAINMENT_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "containment"
    LOCAL_INCIDENT_RESPONSE_DEGRADED_MODE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "degraded_mode"
    LOCAL_INCIDENT_RESPONSE_RECOVERY_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "recovery"
    LOCAL_INCIDENT_RESPONSE_RESILIENCE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "resilience"
    LOCAL_INCIDENT_RESPONSE_EVIDENCE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "evidence"
    LOCAL_INCIDENT_RESPONSE_READING_ORDER_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "reading_order"
    LOCAL_INCIDENT_RESPONSE_TIMELINE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "timeline"
    LOCAL_INCIDENT_RESPONSE_POST_INCIDENT_REVIEW_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "post_incident_review"
    LOCAL_INCIDENT_RESPONSE_ROOT_CAUSE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "root_cause"
    LOCAL_INCIDENT_RESPONSE_CORRECTIVE_ACTIONS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "corrective_actions"
    LOCAL_INCIDENT_RESPONSE_COMMUNICATION_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "communication"
    LOCAL_INCIDENT_RESPONSE_ESCALATION_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "escalation"
    LOCAL_INCIDENT_RESPONSE_NO_GO_SAFE_GO_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "no_go_safe_go"
    LOCAL_INCIDENT_RESPONSE_EXCEPTIONS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "exceptions"
    LOCAL_INCIDENT_RESPONSE_GAPS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "gaps"
    LOCAL_INCIDENT_RESPONSE_RISKS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "risks"
    LOCAL_INCIDENT_RESPONSE_SCORING_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "scoring"
    LOCAL_INCIDENT_RESPONSE_VALIDATION_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "validation"
    LOCAL_INCIDENT_RESPONSE_QUALITY_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "quality"
    
    OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR = OUTPUT_DIR / "local_incident_response"
    OUTPUT_LOCAL_INCIDENT_RESPONSE_CSV_DIR = OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR / "csv"
    OUTPUT_LOCAL_INCIDENT_RESPONSE_MARKDOWN_DIR = OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR / "markdown"
    OUTPUT_LOCAL_INCIDENT_RESPONSE_TXT_DIR = OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR / "txt"
    OUTPUT_LOCAL_INCIDENT_RESPONSE_JSON_DIR = OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR / "json"

    DOCS_GENERATED_LOCAL_INCIDENT_RESPONSE_DIR = DOCS_GENERATED_DIR / "local_incident_response"
"""
    if "LOCAL_INCIDENT_RESPONSE_DIR" not in content:
        content = content.replace('    # Docs Generated', new_paths + '\n    # Docs Generated')
        
        dirs_to_add = """        LOCAL_INCIDENT_RESPONSE_DIR,
        LOCAL_INCIDENT_RESPONSE_PROFILES_DIR,
        LOCAL_INCIDENT_RESPONSE_DOMAINS_DIR,
        LOCAL_INCIDENT_RESPONSE_REHEARSAL_PACKET_DIR,
        LOCAL_INCIDENT_RESPONSE_EVENTS_DIR,
        LOCAL_INCIDENT_RESPONSE_TAXONOMY_DIR,
        LOCAL_INCIDENT_RESPONSE_SEVERITY_DIR,
        LOCAL_INCIDENT_RESPONSE_TRIAGE_DIR,
        LOCAL_INCIDENT_RESPONSE_CLASSIFICATION_DIR,
        LOCAL_INCIDENT_RESPONSE_BOUNDARY_BREACH_DIR,
        LOCAL_INCIDENT_RESPONSE_UNSAFE_OUTPUTS_DIR,
        LOCAL_INCIDENT_RESPONSE_FORBIDDEN_CAPABILITIES_DIR,
        LOCAL_INCIDENT_RESPONSE_SECRET_EXPOSURE_DIR,
        LOCAL_INCIDENT_RESPONSE_FILE_ACTIONS_DIR,
        LOCAL_INCIDENT_RESPONSE_CLOUD_PUBLISH_DIR,
        LOCAL_INCIDENT_RESPONSE_LIVE_BROKER_DIR,
        LOCAL_INCIDENT_RESPONSE_MODEL_DEPLOYMENT_DIR,
        LOCAL_INCIDENT_RESPONSE_EXTERNAL_LLM_API_DIR,
        LOCAL_INCIDENT_RESPONSE_ROLLBACK_DIR,
        LOCAL_INCIDENT_RESPONSE_CONTAINMENT_DIR,
        LOCAL_INCIDENT_RESPONSE_DEGRADED_MODE_DIR,
        LOCAL_INCIDENT_RESPONSE_RECOVERY_DIR,
        LOCAL_INCIDENT_RESPONSE_RESILIENCE_DIR,
        LOCAL_INCIDENT_RESPONSE_EVIDENCE_DIR,
        LOCAL_INCIDENT_RESPONSE_READING_ORDER_DIR,
        LOCAL_INCIDENT_RESPONSE_TIMELINE_DIR,
        LOCAL_INCIDENT_RESPONSE_POST_INCIDENT_REVIEW_DIR,
        LOCAL_INCIDENT_RESPONSE_ROOT_CAUSE_DIR,
        LOCAL_INCIDENT_RESPONSE_CORRECTIVE_ACTIONS_DIR,
        LOCAL_INCIDENT_RESPONSE_COMMUNICATION_DIR,
        LOCAL_INCIDENT_RESPONSE_ESCALATION_DIR,
        LOCAL_INCIDENT_RESPONSE_NO_GO_SAFE_GO_DIR,
        LOCAL_INCIDENT_RESPONSE_EXCEPTIONS_DIR,
        LOCAL_INCIDENT_RESPONSE_GAPS_DIR,
        LOCAL_INCIDENT_RESPONSE_RISKS_DIR,
        LOCAL_INCIDENT_RESPONSE_SCORING_DIR,
        LOCAL_INCIDENT_RESPONSE_VALIDATION_DIR,
        LOCAL_INCIDENT_RESPONSE_QUALITY_DIR,
        OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR,
        OUTPUT_LOCAL_INCIDENT_RESPONSE_CSV_DIR,
        OUTPUT_LOCAL_INCIDENT_RESPONSE_MARKDOWN_DIR,
        OUTPUT_LOCAL_INCIDENT_RESPONSE_TXT_DIR,
        OUTPUT_LOCAL_INCIDENT_RESPONSE_JSON_DIR,
        DOCS_GENERATED_LOCAL_INCIDENT_RESPONSE_DIR,"""
        
        content = content.replace("        OUTPUT_LOCAL_KNOWLEDGE_GRAPH_JSON_DIR,", f"        OUTPUT_LOCAL_KNOWLEDGE_GRAPH_JSON_DIR,\n{dirs_to_add}")
        with open(paths_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated paths.py")

def write_module_init():
    os.makedirs("local_incident_response", exist_ok=True)
    with open("local_incident_response/__init__.py", "w", encoding="utf-8") as f:
        f.write('"""Local Incident-Response Module."""\n')

def write_incident_config():
    code = """from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalIncidentResponseProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_incident_response: bool = False
    allow_real_rollback: bool = False
    allow_forensic_analysis: bool = False
    allow_production_recovery: bool = False
    allow_live_system_halt: bool = False
    allow_broker_halt_instruction: bool = False
    allow_compliance_signoff: bool = False
    allow_legal_signoff: bool = False
    allow_production_recovery_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_telemetry: bool = False
    allow_dashboard_creation: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
    allow_cloud_upload: bool = False
    allow_package_publish: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_redteam_outputs: bool = True
    scan_governance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_events: int = 10000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = [
    LocalIncidentResponseProfile(
        name="balanced_local_incident_response",
        description="Balanced profile for incident response.",
        notes="Genel amaçlı local/offline incident-response rehearsal, safety event register ve resilience supervision profili."
    ),
    LocalIncidentResponseProfile(
        name="safety_event_focus",
        description="Focus on safety events.",
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        scan_governance_outputs=False,
        max_events=8000,
        notes="Safety event register, event taxonomy, severity taxonomy ve triage checklist odaklı profil."
    ),
    LocalIncidentResponseProfile(
        name="rollback_rehearsal_focus",
        description="Focus on rollback rehearsal.",
        scan_docs=False,
        scan_scripts=False,
        scan_tests=False,
        scan_redteam_outputs=False,
        scan_safety_outputs=False,
        max_events=8000,
        notes="Rollback decision playbook, containment, degraded mode ve recovery rehearsal odaklı profil."
    ),
    LocalIncidentResponseProfile(
        name="strict_incident_safety",
        description="Strict safety enforcement for incident responses.",
        max_items=300000,
        max_events=5000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Gerçek incident/rollback/forensic/recovery/live/broker/advice/deploy overclaim denetimini sıkılaştıran profil."
    )
]

def get_local_incident_response_profile(name: str) -> LocalIncidentResponseProfile:
    for p in PROFILES:
        if p.name == name:
            return p
    raise ConfigError(f"Profile not found: {name}")

def list_local_incident_response_profiles(enabled_only: bool = True) -> List[LocalIncidentResponseProfile]:
    if enabled_only:
        return [p for p in PROFILES if p.enabled]
    return PROFILES

def validate_local_incident_response_profiles() -> None:
    for p in PROFILES:
        if not p.language:
            raise ConfigError("language boş olmamalı.")
        if p.max_items <= 0 or p.max_events <= 0:
            raise ConfigError("max_items ve max_events pozitif olmalı.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError("min_readiness_score ve min_quality_score 0-1 aralığında olmalı.")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default True olmalı.")
        if p.allow_real_incident_response or p.allow_real_rollback or p.allow_forensic_analysis or p.allow_production_recovery or p.allow_live_system_halt or p.allow_broker_halt_instruction or p.allow_investment_advice or p.allow_model_deployment_claim or p.allow_telemetry or p.allow_dashboard_creation or p.allow_cloud_upload or p.allow_package_publish or p.allow_external_service or p.allow_file_modification or p.allow_file_deletion or p.allow_file_move or p.allow_overwrite:
            raise ConfigError("incident/rollback/forensic/recovery/live/broker/advice/deploy/telemetry/dashboard/cloud/package/external/file action flagleri False olmalı.")

def get_default_local_incident_response_profile() -> LocalIncidentResponseProfile:
    return get_local_incident_response_profile("balanced_local_incident_response")
"""
    with open("local_incident_response/incident_config.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_labels():
    code = """from typing import List

INCIDENT_DOMAIN_LABELS = [
    "incident_rehearsal_domain", "safety_event_domain", "incident_taxonomy_domain",
    "incident_triage_domain", "incident_classification_domain", "rollback_rehearsal_domain",
    "containment_rehearsal_domain", "degraded_mode_domain", "recovery_rehearsal_domain",
    "resilience_supervision_domain", "post_incident_review_domain", "corrective_action_domain",
    "escalation_domain", "quality_validation_domain", "unknown_incident_domain"
]

SAFETY_EVENT_CATEGORY_LABELS = [
    "event_boundary_breach", "event_unsafe_output", "event_forbidden_capability_request",
    "event_secret_exposure", "event_file_action_request", "event_cloud_publish_request",
    "event_live_trading_broker_request", "event_investment_advice_request",
    "event_model_deployment_request", "event_external_llm_api_request",
    "event_quality_warning", "event_unknown"
]

SEVERITY_LABELS = [
    "severity_info", "severity_low", "severity_medium", "severity_high", "severity_critical", "severity_unknown"
]

INCIDENT_STATUS_LABELS = [
    "incident_ready_for_rehearsal", "incident_ready_with_warnings", "incident_missing",
    "incident_blocked_by_safety", "incident_needs_manual_review", "incident_unknown"
]

INCIDENT_RISK_LABELS = [
    "incident_critical_risk", "incident_high_risk", "incident_medium_risk",
    "incident_low_risk", "incident_info", "incident_unknown_risk"
]

def list_incident_domain_labels() -> List[str]:
    return INCIDENT_DOMAIN_LABELS

def list_safety_event_category_labels() -> List[str]:
    return SAFETY_EVENT_CATEGORY_LABELS

def list_severity_labels() -> List[str]:
    return SEVERITY_LABELS

def list_incident_status_labels() -> List[str]:
    return INCIDENT_STATUS_LABELS

def list_incident_risk_labels() -> List[str]:
    return INCIDENT_RISK_LABELS

def validate_incident_domain_label(label: str) -> None:
    if label not in INCIDENT_DOMAIN_LABELS:
        raise ValueError(f"Invalid domain label: {label}")

def validate_safety_event_category(label: str) -> None:
    if label not in SAFETY_EVENT_CATEGORY_LABELS:
        raise ValueError(f"Invalid safety event category label: {label}")

def validate_severity_label(label: str) -> None:
    if label not in SEVERITY_LABELS:
        raise ValueError(f"Invalid severity label: {label}")

def validate_incident_status(label: str) -> None:
    if label not in INCIDENT_STATUS_LABELS:
        raise ValueError(f"Invalid incident status label: {label}")

def validate_incident_risk(label: str) -> None:
    if label not in INCIDENT_RISK_LABELS:
        raise ValueError(f"Invalid incident risk label: {label}")
"""
    with open("local_incident_response/incident_labels.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_models():
    code = """from dataclasses import dataclass
from typing import List, Dict
import hashlib

@dataclass
class IncidentDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str]
    warnings: List[str]

@dataclass
class SafetyEvent:
    event_id: str
    event_name: str
    event_category: str
    severity_label: str
    abstract_description: str
    expected_manual_action: str
    evidence_refs: List[str]
    manual_review_required: bool
    warnings: List[str]

@dataclass
class RollbackDecisionItem:
    rollback_id: str
    rollback_area: str
    rollback_status: str
    decision_context: str
    rollback_allowed: bool
    expected_manual_action: str
    warnings: List[str]

@dataclass
class PostIncidentTemplate:
    template_id: str
    template_name: str
    template_area: str
    sections: List[str]
    disclaimer: str
    warnings: List[str]

@dataclass
class IncidentFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: List[str]

def build_incident_domain_id(domain_label: str) -> str:
    return hashlib.md5(f"domain_{domain_label}".encode()).hexdigest()[:12]

def build_safety_event_id(event_name: str, event_category: str) -> str:
    return hashlib.md5(f"event_{event_name}_{event_category}".encode()).hexdigest()[:12]

def build_rollback_decision_id(rollback_area: str) -> str:
    return hashlib.md5(f"rollback_{rollback_area}".encode()).hexdigest()[:12]

def build_post_incident_template_id(template_name: str) -> str:
    return hashlib.md5(f"template_{template_name}".encode()).hexdigest()[:12]

def build_incident_finding_id(title: str) -> str:
    return hashlib.md5(f"finding_{title}".encode()).hexdigest()[:12]

def incident_domain_to_dict(item: IncidentDomain) -> Dict:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "domain_name": item.domain_name,
        "description": item.description,
        "required_outputs": ";".join(item.required_outputs),
        "warnings": ";".join(item.warnings)
    }

def safety_event_to_dict(item: SafetyEvent) -> Dict:
    return {
        "event_id": item.event_id,
        "event_name": item.event_name,
        "event_category": item.event_category,
        "severity_label": item.severity_label,
        "abstract_description": item.abstract_description,
        "expected_manual_action": item.expected_manual_action,
        "evidence_refs": ";".join(item.evidence_refs),
        "manual_review_required": item.manual_review_required,
        "warnings": ";".join(item.warnings)
    }

def rollback_decision_item_to_dict(item: RollbackDecisionItem) -> Dict:
    return {
        "rollback_id": item.rollback_id,
        "rollback_area": item.rollback_area,
        "rollback_status": item.rollback_status,
        "decision_context": item.decision_context,
        "rollback_allowed": item.rollback_allowed,
        "expected_manual_action": item.expected_manual_action,
        "warnings": ";".join(item.warnings)
    }

def post_incident_template_to_dict(item: PostIncidentTemplate) -> Dict:
    return {
        "template_id": item.template_id,
        "template_name": item.template_name,
        "template_area": item.template_area,
        "sections": ";".join(item.sections),
        "disclaimer": item.disclaimer,
        "warnings": ";".join(item.warnings)
    }

def incident_finding_to_dict(item: IncidentFinding) -> Dict:
    return {
        "finding_id": item.finding_id,
        "risk_label": item.risk_label,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required,
        "warnings": ";".join(item.warnings)
    }
"""
    with open("local_incident_response/incident_models.py", "w", encoding="utf-8") as f:
        f.write(code)

if __name__ == "__main__":
    patch_settings()
    patch_env()
    patch_paths()
    write_module_init()
    write_incident_config()
    write_incident_labels()
    write_incident_models()
