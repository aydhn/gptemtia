from dataclasses import dataclass, asdict
import hashlib

@dataclass
class ReviewDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class HumanReviewItem:
    review_id: str
    review_area: str
    review_title: str
    review_status: str
    reviewer_role: str
    target_ref: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class ApprovalLedgerItem:
    ledger_id: str
    approval_area: str
    approval_status: str
    boundary_note: str
    evidence_refs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class ExpertReviewItem:
    expert_review_id: str
    expert_area: str
    reviewer_role: str
    review_question: str
    evidence_refs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class ReviewerConsoleItem:
    console_id: str
    console_area: str
    console_title: str
    status_label: str
    target_ref: str
    manual_action: str
    warnings: list[str]

@dataclass
class ReviewFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def _hash(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:12]

def build_review_domain_id(domain_label: str) -> str:
    return f"dom_{_hash(domain_label)}"

def build_human_review_item_id(review_area: str, review_title: str) -> str:
    return f"hr_{_hash(review_area + review_title)}"

def build_approval_ledger_item_id(approval_area: str, approval_status: str) -> str:
    return f"al_{_hash(approval_area + approval_status)}"

def build_expert_review_item_id(expert_area: str, review_question: str) -> str:
    return f"er_{_hash(expert_area + review_question)}"

def build_reviewer_console_item_id(console_area: str, console_title: str) -> str:
    return f"rc_{_hash(console_area + console_title)}"

def build_review_finding_id(title: str) -> str:
    return f"rf_{_hash(title)}"

def review_domain_to_dict(item: ReviewDomain) -> dict:
    return asdict(item)

def human_review_item_to_dict(item: HumanReviewItem) -> dict:
    return asdict(item)

def approval_ledger_item_to_dict(item: ApprovalLedgerItem) -> dict:
    return asdict(item)

def expert_review_item_to_dict(item: ExpertReviewItem) -> dict:
    return asdict(item)

def reviewer_console_item_to_dict(item: ReviewerConsoleItem) -> dict:
    return asdict(item)

def review_finding_to_dict(item: ReviewFinding) -> dict:
    return asdict(item)
