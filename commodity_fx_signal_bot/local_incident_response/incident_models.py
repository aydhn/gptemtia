from dataclasses import dataclass
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
