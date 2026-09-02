
from dataclasses import dataclass
from typing import Any
import hashlib

@dataclass
class ClosureDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class ClosureItem:
    item_id: str
    item_label: str
    item_name: str
    source_layer: str
    status: str
    evidence_refs: list[str]
    warnings: list[str]

@dataclass
class LessonLearnedItem:
    lesson_id: str
    lesson_title: str
    category: str
    observation: str
    implication: str
    recommendation: str
    warnings: list[str]

@dataclass
class RoadmapItem:
    roadmap_id: str
    title: str
    category: str
    status: str
    rationale: str
    prerequisites: list[str]
    safety_boundaries: list[str]
    warnings: list[str]

@dataclass
class ClosureFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_closure_domain_id(domain_label: str) -> str:
    return hashlib.sha256(domain_label.encode()).hexdigest()[:12]

def build_closure_item_id(item_name: str, item_label: str) -> str:
    return hashlib.sha256(f"{item_name}_{item_label}".encode()).hexdigest()[:12]

def build_lesson_learned_id(lesson_title: str) -> str:
    return hashlib.sha256(lesson_title.encode()).hexdigest()[:12]

def build_roadmap_item_id(title: str) -> str:
    return hashlib.sha256(title.encode()).hexdigest()[:12]

def build_closure_finding_id(title: str) -> str:
    return hashlib.sha256(title.encode()).hexdigest()[:12]

def closure_domain_to_dict(item: ClosureDomain) -> dict[str, Any]:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "domain_name": item.domain_name,
        "description": item.description,
        "required_outputs": ",".join(item.required_outputs),
        "warnings": ",".join(item.warnings)
    }

def closure_item_to_dict(item: ClosureItem) -> dict[str, Any]:
    return {
        "item_id": item.item_id,
        "item_label": item.item_label,
        "item_name": item.item_name,
        "source_layer": item.source_layer,
        "status": item.status,
        "evidence_refs": ",".join(item.evidence_refs),
        "warnings": ",".join(item.warnings)
    }

def lesson_learned_item_to_dict(item: LessonLearnedItem) -> dict[str, Any]:
    return {
        "lesson_id": item.lesson_id,
        "lesson_title": item.lesson_title,
        "category": item.category,
        "observation": item.observation,
        "implication": item.implication,
        "recommendation": item.recommendation,
        "warnings": ",".join(item.warnings)
    }

def roadmap_item_to_dict(item: RoadmapItem) -> dict[str, Any]:
    return {
        "roadmap_id": item.roadmap_id,
        "title": item.title,
        "category": item.category,
        "status": item.status,
        "rationale": item.rationale,
        "prerequisites": ",".join(item.prerequisites),
        "safety_boundaries": ",".join(item.safety_boundaries),
        "warnings": ",".join(item.warnings)
    }

def closure_finding_to_dict(item: ClosureFinding) -> dict[str, Any]:
    return {
        "finding_id": item.finding_id,
        "risk_label": item.risk_label,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required,
        "warnings": ",".join(item.warnings)
    }
