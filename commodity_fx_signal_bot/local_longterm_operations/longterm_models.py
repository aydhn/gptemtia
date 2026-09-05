"""Long-term models."""
from dataclasses import dataclass
import hashlib

@dataclass
class LongTermDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class ReviewCalendarItem:
    calendar_id: str
    calendar_name: str
    cadence: str
    review_area: str
    calendar_status: str
    expected_manual_action: str
    warnings: list[str]

@dataclass
class LifecycleWorkbookItem:
    workbook_id: str
    workbook_area: str
    lifecycle_status: str
    review_question: str
    evidence_refs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class DeprecationCandidate:
    candidate_id: str
    candidate_name: str
    candidate_area: str
    deprecation_status: str
    impact_note: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class RoadmapCandidate:
    roadmap_id: str
    roadmap_name: str
    roadmap_area: str
    priority_hint: str
    expected_benefit: str
    risk_note: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class LifecycleFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_longterm_domain_id(domain_label: str) -> str:
    return hashlib.sha256(domain_label.encode()).hexdigest()[:12]

def build_review_calendar_item_id(calendar_name: str, review_area: str) -> str:
    return hashlib.sha256(f"{calendar_name}_{review_area}".encode()).hexdigest()[:12]

def build_lifecycle_workbook_item_id(workbook_area: str, review_question: str) -> str:
    return hashlib.sha256(f"{workbook_area}_{review_question}".encode()).hexdigest()[:12]

def build_deprecation_candidate_id(candidate_name: str, candidate_area: str) -> str:
    return hashlib.sha256(f"{candidate_name}_{candidate_area}".encode()).hexdigest()[:12]

def build_roadmap_candidate_id(roadmap_name: str, roadmap_area: str) -> str:
    return hashlib.sha256(f"{roadmap_name}_{roadmap_area}".encode()).hexdigest()[:12]

def build_lifecycle_finding_id(title: str) -> str:
    return hashlib.sha256(title.encode()).hexdigest()[:12]

def longterm_domain_to_dict(item: LongTermDomain) -> dict:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "domain_name": item.domain_name,
        "description": item.description,
        "required_outputs": "|".join(item.required_outputs),
        "warnings": "|".join(item.warnings)
    }

def review_calendar_item_to_dict(item: ReviewCalendarItem) -> dict:
    return {
        "calendar_id": item.calendar_id,
        "calendar_name": item.calendar_name,
        "cadence": item.cadence,
        "review_area": item.review_area,
        "calendar_status": item.calendar_status,
        "expected_manual_action": item.expected_manual_action,
        "warnings": "|".join(item.warnings)
    }

def lifecycle_workbook_item_to_dict(item: LifecycleWorkbookItem) -> dict:
    return {
        "workbook_id": item.workbook_id,
        "workbook_area": item.workbook_area,
        "lifecycle_status": item.lifecycle_status,
        "review_question": item.review_question,
        "evidence_refs": "|".join(item.evidence_refs),
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }

def deprecation_candidate_to_dict(item: DeprecationCandidate) -> dict:
    return {
        "candidate_id": item.candidate_id,
        "candidate_name": item.candidate_name,
        "candidate_area": item.candidate_area,
        "deprecation_status": item.deprecation_status,
        "impact_note": item.impact_note,
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }

def roadmap_candidate_to_dict(item: RoadmapCandidate) -> dict:
    return {
        "roadmap_id": item.roadmap_id,
        "roadmap_name": item.roadmap_name,
        "roadmap_area": item.roadmap_area,
        "priority_hint": item.priority_hint,
        "expected_benefit": item.expected_benefit,
        "risk_note": item.risk_note,
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }

def lifecycle_finding_to_dict(item: LifecycleFinding) -> dict:
    return {
        "finding_id": item.finding_id,
        "risk_label": item.risk_label,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }
