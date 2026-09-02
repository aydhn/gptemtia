from dataclasses import dataclass
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
