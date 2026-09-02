import os
from pathlib import Path

ROOT = Path("commodity_fx_signal_bot")
TARGET_DIR = ROOT / "local_governance_control"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

# __init__.py
with open(TARGET_DIR / "__init__.py", "w", encoding="utf-8") as f:
    f.write('"""Local Governance Control Module."""\n')

# governance_control_config.py
with open(TARGET_DIR / "governance_control_config.py", "w", encoding="utf-8") as f:
    f.write("""from dataclasses import dataclass
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
""")

# governance_control_labels.py
with open(TARGET_DIR / "governance_control_labels.py", "w", encoding="utf-8") as f:
    f.write("""def list_governance_domain_labels() -> list[str]:
    return [
        "governance_control_room_domain",
        "executive_oversight_domain",
        "manual_approval_domain",
        "risk_committee_rehearsal_domain",
        "operator_supervision_domain",
        "escalation_domain",
        "governance_roles_domain",
        "decision_authority_domain",
        "approval_boundary_domain",
        "oversight_evidence_domain",
        "governance_metrics_domain",
        "governance_template_domain",
        "quality_validation_domain",
        "unknown_governance_domain"
    ]

def list_approval_status_labels() -> list[str]:
    return [
        "approval_rehearsal_pending",
        "approval_rehearsal_reviewed",
        "approval_rehearsal_rejected",
        "approval_rehearsal_blocked_by_safety",
        "approval_rehearsal_not_applicable",
        "approval_rehearsal_unknown"
    ]

def list_governance_status_labels() -> list[str]:
    return [
        "governance_ready_for_rehearsal",
        "governance_ready_with_warnings",
        "governance_missing",
        "governance_blocked_by_safety",
        "governance_needs_manual_review",
        "governance_unknown"
    ]

def list_escalation_labels() -> list[str]:
    return [
        "escalation_info",
        "escalation_manual_review",
        "escalation_risk_committee_rehearsal",
        "escalation_blocked_by_no_go",
        "escalation_external_approval_not_allowed",
        "escalation_unknown"
    ]

def list_governance_risk_labels() -> list[str]:
    return [
        "governance_critical_risk",
        "governance_high_risk",
        "governance_medium_risk",
        "governance_low_risk",
        "governance_info",
        "governance_unknown_risk"
    ]

def validate_governance_domain_label(label: str) -> None:
    if label not in list_governance_domain_labels():
        raise ValueError(f"Invalid domain label: {label}")

def validate_approval_status(label: str) -> None:
    if label not in list_approval_status_labels():
        raise ValueError(f"Invalid approval status: {label}")

def validate_governance_status(label: str) -> None:
    if label not in list_governance_status_labels():
        raise ValueError(f"Invalid governance status: {label}")

def validate_escalation_label(label: str) -> None:
    if label not in list_escalation_labels():
        raise ValueError(f"Invalid escalation label: {label}")

def validate_governance_risk(label: str) -> None:
    if label not in list_governance_risk_labels():
        raise ValueError(f"Invalid risk label: {label}")
""")

# governance_control_models.py
with open(TARGET_DIR / "governance_control_models.py", "w", encoding="utf-8") as f:
    f.write("""from dataclasses import dataclass
import hashlib

@dataclass
class GovernanceDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class ManualApprovalItem:
    approval_id: str
    approval_name: str
    approval_scope: str
    approval_status: str
    evidence_refs: list[str]
    decision_note: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class OversightItem:
    oversight_id: str
    oversight_area: str
    source_layer: str
    status: str
    summary_note: str
    evidence_refs: list[str]
    warnings: list[str]

@dataclass
class EscalationItem:
    escalation_id: str
    escalation_area: str
    escalation_label: str
    trigger_condition: str
    recommended_manual_action: str
    warnings: list[str]

@dataclass
class GovernanceFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_governance_domain_id(domain_label: str) -> str:
    return "DOMAIN-" + hashlib.md5(domain_label.encode()).hexdigest()[:8].upper()

def build_manual_approval_id(approval_name: str, approval_scope: str) -> str:
    return "APP-" + hashlib.md5(f"{approval_name}-{approval_scope}".encode()).hexdigest()[:8].upper()

def build_oversight_item_id(oversight_area: str, source_layer: str) -> str:
    return "OVR-" + hashlib.md5(f"{oversight_area}-{source_layer}".encode()).hexdigest()[:8].upper()

def build_escalation_item_id(escalation_area: str) -> str:
    return "ESC-" + hashlib.md5(escalation_area.encode()).hexdigest()[:8].upper()

def build_governance_finding_id(title: str) -> str:
    return "FND-" + hashlib.md5(title.encode()).hexdigest()[:8].upper()

def governance_domain_to_dict(item: GovernanceDomain) -> dict:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "domain_name": item.domain_name,
        "description": item.description,
        "required_outputs": ",".join(item.required_outputs),
        "warnings": ",".join(item.warnings)
    }

def manual_approval_item_to_dict(item: ManualApprovalItem) -> dict:
    return {
        "approval_id": item.approval_id,
        "approval_name": item.approval_name,
        "approval_scope": item.approval_scope,
        "approval_status": item.approval_status,
        "evidence_refs": ",".join(item.evidence_refs),
        "decision_note": item.decision_note,
        "manual_review_required": item.manual_review_required,
        "warnings": ",".join(item.warnings)
    }

def oversight_item_to_dict(item: OversightItem) -> dict:
    return {
        "oversight_id": item.oversight_id,
        "oversight_area": item.oversight_area,
        "source_layer": item.source_layer,
        "status": item.status,
        "summary_note": item.summary_note,
        "evidence_refs": ",".join(item.evidence_refs),
        "warnings": ",".join(item.warnings)
    }

def escalation_item_to_dict(item: EscalationItem) -> dict:
    return {
        "escalation_id": item.escalation_id,
        "escalation_area": item.escalation_area,
        "escalation_label": item.escalation_label,
        "trigger_condition": item.trigger_condition,
        "recommended_manual_action": item.recommended_manual_action,
        "warnings": ",".join(item.warnings)
    }

def governance_finding_to_dict(item: GovernanceFinding) -> dict:
    return {
        "finding_id": item.finding_id,
        "risk_label": item.risk_label,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required,
        "warnings": ",".join(item.warnings)
    }
""")

# governance_domain_registry.py
with open(TARGET_DIR / "governance_domain_registry.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile
from .governance_control_models import GovernanceDomain, build_governance_domain_id, governance_domain_to_dict
from .governance_control_labels import list_governance_domain_labels

def build_default_governance_domains(profile: LocalGovernanceControlProfile) -> list[GovernanceDomain]:
    domains = []
    labels = list_governance_domain_labels()
    for lbl in labels:
        if lbl == "unknown_governance_domain":
            continue
        dom = GovernanceDomain(
            domain_id=build_governance_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Local/offline {lbl.replace('_', ' ')} for rehearsal.",
            required_outputs=["document"],
            warnings=["Bu domain official governance scope değildir."]
        )
        domains.append(dom)
    return domains

def build_governance_domain_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_governance_domains(profile)
    df = pd.DataFrame([governance_domain_to_dict(d) for d in domains])
    summary = summarize_governance_domains(df)
    return df, summary

def summarize_governance_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df is None or domain_df.empty:
        return {"total": 0}
    return {
        "total": len(domain_df),
        "domains": domain_df["domain_label"].tolist()
    }
""")
print("Done writing models and domains generator.")
