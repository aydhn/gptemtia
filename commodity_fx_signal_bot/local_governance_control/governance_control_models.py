from dataclasses import dataclass
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
