from dataclasses import dataclass
from typing import Dict, List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalGovernanceControlProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_governance_decision: bool = False
    allow_real_committee_approval: bool = False
    allow_legal_signoff: bool = False
    allow_compliance_signoff: bool = False
    allow_production_approval_claim: bool = False
    allow_live_trading_approval_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_dashboard_creation: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
    allow_telemetry: bool = False
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
    scan_usability_outputs: bool = True
    scan_performance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_ledger_rows: int = 10000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES: Dict[str, LocalGovernanceControlProfile] = {
    "balanced_local_governance_control": LocalGovernanceControlProfile(
        name="balanced_local_governance_control",
        description="Genel amaçlı local/offline governance control room, executive oversight ve operator supervision rehearsal profili.",
        notes="Genel amaçlı local/offline governance control room, executive oversight ve operator supervision rehearsal profili."
    ),
    "executive_oversight_focus": LocalGovernanceControlProfile(
        name="executive_oversight_focus",
        description="Executive oversight packet, report reading order ve KPI rehearsal odaklı profil.",
        scan_docs=True,
        scan_reports=True,
        scan_generated_docs=True,
        scan_usability_outputs=True,
        scan_performance_outputs=True,
        max_ledger_rows=5000,
        notes="Executive oversight packet, report reading order ve KPI rehearsal odaklı profil."
    ),
    "risk_committee_focus": LocalGovernanceControlProfile(
        name="risk_committee_focus",
        description="Risk committee rehearsal, manual approval ledger, escalation matrix ve decision rehearsal odaklı profil.",
        scan_reports=True,
        scan_data_lake=True,
        scan_generated_docs=True,
        scan_safety_outputs=True,
        max_ledger_rows=5000,
        notes="Risk committee rehearsal, manual approval ledger, escalation matrix ve decision rehearsal odaklı profil."
    ),
    "strict_governance_safety": LocalGovernanceControlProfile(
        name="strict_governance_safety",
        description="Gerçek onay, compliance sign-off, production approval, live/broker/advice overclaim denetimini sıkılaştıran profil.",
        max_items=300000,
        max_ledger_rows=3000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Gerçek onay, compliance sign-off, production approval, live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_governance_control_profile(name: str) -> LocalGovernanceControlProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return _PROFILES[name]

def list_local_governance_control_profiles(enabled_only: bool = True) -> list[LocalGovernanceControlProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_governance_control_profiles() -> None:
    for name, p in _PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} must have a language")
        if p.max_items <= 0 or p.max_ledger_rows <= 0:
            raise ConfigError(f"Profile {name} max_items and max_ledger_rows must be positive")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {name} min_readiness_score and min_quality_score must be between 0 and 1")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name} dry_run_default must be True")
        
        forbidden_flags = [
            p.allow_real_governance_decision,
            p.allow_real_committee_approval,
            p.allow_legal_signoff,
            p.allow_compliance_signoff,
            p.allow_production_approval_claim,
            p.allow_live_trading_approval_claim,
            p.allow_broker_readiness_claim,
            p.allow_investment_advice,
            p.allow_model_deployment_claim,
            p.allow_dashboard_creation,
            p.allow_gui_creation,
            p.allow_tui_creation,
            p.allow_telemetry,
            p.allow_cloud_upload,
            p.allow_package_publish,
            p.allow_external_service,
            p.allow_external_llm,
            p.allow_file_modification,
            p.allow_file_deletion,
            p.allow_file_move,
            p.allow_overwrite
        ]
        if any(forbidden_flags):
            raise ConfigError(f"Profile {name} must have all real execution/claim flags set to False")

def get_default_local_governance_control_profile() -> LocalGovernanceControlProfile:
    return _PROFILES["balanced_local_governance_control"]
