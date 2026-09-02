from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class SimplificationDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_reports: list[str]
    warnings: list[str]

@dataclass
class ComplexityItem:
    item_id: str
    item_name: str
    item_path: Optional[str]
    source_layer: str
    metric_name: str
    metric_value: Union[float, int, str, None]
    complexity_level: str
    warnings: list[str]

@dataclass
class SimplificationCandidate:
    candidate_id: str
    candidate_label: str
    candidate_name: str
    source_layer: str
    rationale: str
    expected_benefit: str
    manual_review_required: bool
    safety_boundaries: list[str]
    warnings: list[str]

@dataclass
class SlimmingPlanItem:
    plan_item_id: str
    title: str
    category: str
    priority_hint: str
    action_type: str
    dry_run_only: bool
    prerequisites: list[str]
    warnings: list[str]

@dataclass
class SimplificationFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_simplification_domain_id(domain_label: str) -> str:
    return f"domain_{domain_label}"

def build_complexity_item_id(item_name: str, metric_name: str) -> str:
    return f"comp_{item_name}_{metric_name}".replace(" ", "_")

def build_simplification_candidate_id(candidate_label: str, candidate_name: str) -> str:
    return f"cand_{candidate_label}_{candidate_name}".replace(" ", "_")

def build_slimming_plan_item_id(title: str, category: str) -> str:
    return f"plan_{category}_{title}".replace(" ", "_")

def build_simplification_finding_id(title: str) -> str:
    return f"finding_{title}".replace(" ", "_")

def simplification_domain_to_dict(item: SimplificationDomain) -> dict:
    return {
        "domain_id": item.domain_id, "domain_label": item.domain_label,
        "domain_name": item.domain_name, "description": item.description,
        "required_reports": ",".join(item.required_reports), "warnings": ",".join(item.warnings)
    }

def complexity_item_to_dict(item: ComplexityItem) -> dict:
    return {
        "item_id": item.item_id, "item_name": item.item_name, "item_path": item.item_path,
        "source_layer": item.source_layer, "metric_name": item.metric_name,
        "metric_value": item.metric_value, "complexity_level": item.complexity_level,
        "warnings": ",".join(item.warnings)
    }

def simplification_candidate_to_dict(item: SimplificationCandidate) -> dict:
    return {
        "candidate_id": item.candidate_id, "candidate_label": item.candidate_label,
        "candidate_name": item.candidate_name, "source_layer": item.source_layer,
        "rationale": item.rationale, "expected_benefit": item.expected_benefit,
        "manual_review_required": item.manual_review_required,
        "safety_boundaries": ",".join(item.safety_boundaries), "warnings": ",".join(item.warnings)
    }

def slimming_plan_item_to_dict(item: SlimmingPlanItem) -> dict:
    return {
        "plan_item_id": item.plan_item_id, "title": item.title, "category": item.category,
        "priority_hint": item.priority_hint, "action_type": item.action_type,
        "dry_run_only": item.dry_run_only, "prerequisites": ",".join(item.prerequisites),
        "warnings": ",".join(item.warnings)
    }

def simplification_finding_to_dict(item: SimplificationFinding) -> dict:
    return {
        "finding_id": item.finding_id, "risk_label": item.risk_label, "title": item.title,
        "description": item.description, "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required, "warnings": ",".join(item.warnings)
    }
