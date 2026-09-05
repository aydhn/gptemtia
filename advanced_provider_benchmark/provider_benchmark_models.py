from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any


@dataclass
class ProviderBenchmarkProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    next_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    dry_run: bool
    status_label: str
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ProviderBenchmarkDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class BenchmarkMetric:
    metric_id: str
    metric_label: str
    metric_name: str
    description: str
    score_direction: str
    safe_usage_note: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class BenchmarkWeight:
    weight_id: str
    metric_label: str
    provider_domain: str
    weight: float
    rationale: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ProviderBenchmarkRecord:
    record_id: str
    provider_name: str
    provider_domain: str
    metric_label: str
    raw_score: float
    weighted_score: float
    status_label: str
    evidence_ref: str
    limitation_note: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ProviderBenchmarkFinding:
    finding_id: str
    provider_name: str
    provider_domain: str
    metric_label: str
    severity_label: str
    status_label: str
    message: str
    recommendation: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ProviderBenchmarkManualReviewItem:
    review_id: str
    finding_id: str
    provider_name: str
    provider_domain: str
    review_reason: str
    suggested_action: str
    destructive_action_allowed: bool
    status_label: str

    def __post_init__(self):
        if self.destructive_action_allowed:
            raise ValueError("destructive_action_allowed must always be False in ProviderBenchmarkManualReviewItem")

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ProviderBenchmarkScore:
    score_id: str
    provider_name: str
    provider_domain: str
    total_score: float
    coverage_score: float
    capability_score: float
    quality_score: float
    normalization_score: float
    traceability_score: float
    compliance_score: float
    manual_review_penalty: float
    status_label: str
    official_approval: bool
    production_ready: bool
    broker_ready: bool
    notes: str

    def __post_init__(self):
        if self.official_approval:
            raise ValueError("official_approval must always be False")
        if self.production_ready:
            raise ValueError("production_ready must always be False")
        if self.broker_ready:
            raise ValueError("broker_ready must always be False")
        if not (0.0 <= self.total_score <= 1.0):
            raise ValueError(f"total_score must be in range [0.0, 1.0], got {self.total_score}")

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def build_provider_benchmark_profile_id(profile_name: str) -> str:
    return f"pb_profile::{profile_name.strip().lower()}"


def build_provider_benchmark_domain_id(domain_label: str) -> str:
    return f"pb_domain::{domain_label.strip().lower()}"


def build_benchmark_metric_id(metric_label: str) -> str:
    return f"pb_metric::{metric_label.strip().lower()}"


def build_benchmark_weight_id(metric_label: str, provider_domain: str) -> str:
    return f"pb_weight::{metric_label.strip().lower()}::{provider_domain.strip().lower()}"


def build_provider_benchmark_record_id(provider_name: str, metric_label: str) -> str:
    return f"pb_rec::{provider_name.strip().lower()}::{metric_label.strip().lower()}"


def build_provider_benchmark_finding_id(provider_name: str, metric_label: str) -> str:
    return f"pb_find::{provider_name.strip().lower()}::{metric_label.strip().lower()}"


def build_provider_benchmark_review_id(finding_id: str) -> str:
    return f"pb_review::{finding_id.strip().lower()}"


def build_provider_benchmark_score_id(provider_name: str, provider_domain: str) -> str:
    return f"pb_score::{provider_name.strip().lower()}::{provider_domain.strip().lower()}"
