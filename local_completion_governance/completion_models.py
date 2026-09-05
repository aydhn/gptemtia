from dataclasses import dataclass, asdict

@dataclass
class CompletionDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class ClosureSynthesisItem:
    closure_id: str
    recap_area: str
    recap_title: str
    source_ref: str
    status_label: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class CertificationRehearsalItem:
    certification_id: str
    criteria_area: str
    criteria_title: str
    rehearsal_status: str
    boundary_note: str
    evidence_refs: list[str]
    warnings: list[str]

@dataclass
class ProjectFreezeItem:
    freeze_id: str
    freeze_area: str
    freeze_title: str
    snapshot_ref: str
    freeze_status: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class AcceptanceEvidenceItem:
    evidence_id: str
    evidence_area: str
    evidence_title: str
    source_ref: str
    output_ref: str
    acceptance_status: str
    warnings: list[str]

@dataclass
class CompletionFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_completion_domain_id(domain_label: str) -> str:
    return f"dom_{hash(domain_label) % 1000000}"

def build_closure_synthesis_item_id(recap_area: str, recap_title: str) -> str:
    return f"clo_{hash(recap_area + recap_title) % 1000000}"

def build_certification_rehearsal_item_id(criteria_area: str, criteria_title: str) -> str:
    return f"cert_{hash(criteria_area + criteria_title) % 1000000}"

def build_project_freeze_item_id(freeze_area: str, freeze_title: str) -> str:
    return f"frz_{hash(freeze_area + freeze_title) % 1000000}"

def build_acceptance_evidence_item_id(evidence_area: str, evidence_title: str) -> str:
    return f"acc_{hash(evidence_area + evidence_title) % 1000000}"

def build_completion_finding_id(title: str) -> str:
    return f"fnd_{hash(title) % 1000000}"

def completion_domain_to_dict(item: CompletionDomain) -> dict:
    return asdict(item)

def closure_synthesis_item_to_dict(item: ClosureSynthesisItem) -> dict:
    return asdict(item)

def certification_rehearsal_item_to_dict(item: CertificationRehearsalItem) -> dict:
    return asdict(item)

def project_freeze_item_to_dict(item: ProjectFreezeItem) -> dict:
    return asdict(item)

def acceptance_evidence_item_to_dict(item: AcceptanceEvidenceItem) -> dict:
    return asdict(item)

def completion_finding_to_dict(item: CompletionFinding) -> dict:
    return asdict(item)
