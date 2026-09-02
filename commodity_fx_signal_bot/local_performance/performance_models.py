import hashlib
from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class PerformanceDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_reports: list[str]
    warnings: list[str]

@dataclass
class ResourceEstimateItem:
    estimate_id: str
    estimate_label: str
    item_name: str
    source_layer: str
    estimate_metric: str
    estimate_value: float | int | str | None
    estimate_basis: str
    warnings: list[str]

@dataclass
class RuntimeEstimateItem:
    runtime_id: str
    target_name: str
    target_type: str
    runtime_estimate_label: str
    estimated_minutes: float | None
    estimate_basis: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class EfficiencyCandidate:
    candidate_id: str
    candidate_label: str
    candidate_name: str
    source_layer: str
    rationale: str
    expected_local_benefit: str
    dry_run_only: bool
    manual_review_required: bool
    warnings: list[str]

@dataclass
class PerformanceFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_performance_domain_id(domain_label: str) -> str:
    return hashlib.md5(f"domain_{domain_label}".encode()).hexdigest()[:12]

def build_resource_estimate_id(item_name: str, estimate_metric: str) -> str:
    return hashlib.md5(f"resource_{item_name}_{estimate_metric}".encode()).hexdigest()[:12]

def build_runtime_estimate_id(target_name: str, target_type: str) -> str:
    return hashlib.md5(f"runtime_{target_type}_{target_name}".encode()).hexdigest()[:12]

def build_efficiency_candidate_id(candidate_label: str, candidate_name: str) -> str:
    return hashlib.md5(f"cand_{candidate_label}_{candidate_name}".encode()).hexdigest()[:12]

def build_performance_finding_id(title: str) -> str:
    return hashlib.md5(f"finding_{title}".encode()).hexdigest()[:12]

def performance_domain_to_dict(item: PerformanceDomain) -> dict: return asdict(item)
def resource_estimate_item_to_dict(item: ResourceEstimateItem) -> dict: return asdict(item)
def runtime_estimate_item_to_dict(item: RuntimeEstimateItem) -> dict: return asdict(item)
def efficiency_candidate_to_dict(item: EfficiencyCandidate) -> dict: return asdict(item)
def performance_finding_to_dict(item: PerformanceFinding) -> dict: return asdict(item)
