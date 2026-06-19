from dataclasses import dataclass

@dataclass
class ReadinessGate:
    gate_id: str
    gate_name: str
    domain: str
    description: str
    required_artifacts: list[str]
    status: str
    no_go_if_failed: bool
    warnings: list[str]

@dataclass
class AcceptanceCriterion:
    criterion_id: str
    criterion_name: str
    domain: str
    description: str
    evidence_path: str | None
    status: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class OperatorChecklistItem:
    item_id: str
    checklist_name: str
    domain: str
    instruction: str
    expected_output: str
    status: str
    safe_command: str | None
    warnings: list[str]

@dataclass
class ReadinessFinding:
    finding_id: str
    domain: str
    risk_level: str
    title: str
    description: str
    recommendation: str
    no_go: bool
    warnings: list[str]

@dataclass
class HandoffManifest:
    manifest_id: str
    profile_name: str
    created_at_utc: str
    local_only: bool
    readiness_score: float
    gate_summary: dict
    included_sections: list[str]
    warnings: list[str]

def build_readiness_gate_id(gate_name: str, domain: str) -> str:
    return f"{domain}_{gate_name.replace(' ', '_').lower()}_gate"

def build_acceptance_criterion_id(criterion_name: str, domain: str) -> str:
    return f"{domain}_{criterion_name.replace(' ', '_').lower()}_crit"

def build_operator_checklist_item_id(checklist_name: str, instruction: str) -> str:
    # A simplified hash or clean string
    return f"{checklist_name.replace(' ', '_').lower()}_{hash(instruction) % 10000}"

def build_readiness_finding_id(domain: str, title: str) -> str:
    return f"{domain}_{title.replace(' ', '_').lower()}_finding"

def build_handoff_manifest_id(profile_name: str, created_at_utc: str) -> str:
    return f"manifest_{profile_name}_{created_at_utc.replace(':', '').replace('-', '')}"

def readiness_gate_to_dict(item: ReadinessGate) -> dict:
    return {
        "gate_id": item.gate_id,
        "gate_name": item.gate_name,
        "domain": item.domain,
        "description": item.description,
        "required_artifacts": item.required_artifacts,
        "status": item.status,
        "no_go_if_failed": item.no_go_if_failed,
        "warnings": item.warnings
    }

def acceptance_criterion_to_dict(item: AcceptanceCriterion) -> dict:
    return {
        "criterion_id": item.criterion_id,
        "criterion_name": item.criterion_name,
        "domain": item.domain,
        "description": item.description,
        "evidence_path": item.evidence_path,
        "status": item.status,
        "manual_review_required": item.manual_review_required,
        "warnings": item.warnings
    }

def operator_checklist_item_to_dict(item: OperatorChecklistItem) -> dict:
    return {
        "item_id": item.item_id,
        "checklist_name": item.checklist_name,
        "domain": item.domain,
        "instruction": item.instruction,
        "expected_output": item.expected_output,
        "status": item.status,
        "safe_command": item.safe_command,
        "warnings": item.warnings
    }

def readiness_finding_to_dict(item: ReadinessFinding) -> dict:
    return {
        "finding_id": item.finding_id,
        "domain": item.domain,
        "risk_level": item.risk_level,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "no_go": item.no_go,
        "warnings": item.warnings
    }

def handoff_manifest_to_dict(item: HandoffManifest) -> dict:
    return {
        "manifest_id": item.manifest_id,
        "profile_name": item.profile_name,
        "created_at_utc": item.created_at_utc,
        "local_only": item.local_only,
        "readiness_score": item.readiness_score,
        "gate_summary": item.gate_summary,
        "included_sections": item.included_sections,
        "warnings": item.warnings
    }
