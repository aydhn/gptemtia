from dataclasses import dataclass, asdict
import hashlib

@dataclass
class AcceptanceDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_evidence: list[str]
    warnings: list[str]

@dataclass
class AcceptanceChecklistItem:
    item_id: str
    domain_label: str
    item_name: str
    description: str
    status: str
    evidence_refs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class ReviewerQuestion:
    question_id: str
    question: str
    domain_label: str
    expected_evidence: list[str]
    safe_answer_hint: str
    response_label: str
    warnings: list[str]

@dataclass
class EvidenceTraceItem:
    trace_id: str
    trace_type: str
    evidence_name: str
    source_path: str | None
    linked_output: str | None
    linked_test: str | None
    linked_doc: str | None
    trace_label: str
    warnings: list[str]

@dataclass
class AcceptanceFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_acceptance_domain_id(domain_label: str) -> str:
    return hashlib.md5(domain_label.encode()).hexdigest()[:8]

def build_acceptance_checklist_item_id(domain_label: str, item_name: str) -> str:
    return hashlib.md5(f"{domain_label}_{item_name}".encode()).hexdigest()[:8]

def build_reviewer_question_id(question: str) -> str:
    return hashlib.md5(question.encode()).hexdigest()[:8]

def build_evidence_trace_id(trace_type: str, evidence_name: str) -> str:
    return hashlib.md5(f"{trace_type}_{evidence_name}".encode()).hexdigest()[:8]

def build_acceptance_finding_id(title: str) -> str:
    return hashlib.md5(title.encode()).hexdigest()[:8]

def acceptance_domain_to_dict(item: AcceptanceDomain) -> dict:
    return asdict(item)

def acceptance_checklist_item_to_dict(item: AcceptanceChecklistItem) -> dict:
    return asdict(item)

def reviewer_question_to_dict(item: ReviewerQuestion) -> dict:
    return asdict(item)

def evidence_trace_item_to_dict(item: EvidenceTraceItem) -> dict:
    return asdict(item)

def acceptance_finding_to_dict(item: AcceptanceFinding) -> dict:
    return asdict(item)
