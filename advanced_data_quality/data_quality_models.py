from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any


def build_data_quality_profile_id(profile_name: str) -> str:
    clean = profile_name.strip().lower().replace(" ", "_").replace("-", "_")
    return f"dqp_{clean}"


def build_data_quality_domain_id(domain_label: str) -> str:
    clean = domain_label.strip().lower().replace(" ", "_").replace("-", "_")
    return f"dqd_{clean}"


def build_quality_rule_id(rule_name: str, rule_domain: str) -> str:
    clean_name = rule_name.strip().lower().replace(" ", "_").replace("-", "_")
    clean_domain = rule_domain.strip().lower().replace(" ", "_").replace("-", "_")
    return f"rule_{clean_domain}_{clean_name}"


def build_quality_finding_id(rule_id: str, dataset_type: str, field_name: str = "") -> str:
    clean_rule = rule_id.strip().lower().replace(" ", "_").replace("-", "_")
    clean_ds = dataset_type.strip().lower().replace(" ", "_").replace("-", "_")
    clean_fld = field_name.strip().lower().replace(" ", "_").replace("-", "_") if field_name else "all"
    return f"find_{clean_rule}_{clean_ds}_{clean_fld}"


def build_manual_review_id(finding_id: str) -> str:
    clean = finding_id.strip().lower().replace(" ", "_").replace("-", "_")
    return f"rev_{clean}"


def build_provider_quality_score_id(provider_name: str, dataset_type: str) -> str:
    clean_p = provider_name.strip().lower().replace(" ", "_").replace("-", "_")
    clean_d = dataset_type.strip().lower().replace(" ", "_").replace("-", "_")
    return f"pqs_{clean_p}_{clean_d}"


def build_dataset_quality_score_id(dataset_name: str, provider_name: str) -> str:
    clean_ds = dataset_name.strip().lower().replace(" ", "_").replace("-", "_")
    clean_p = provider_name.strip().lower().replace(" ", "_").replace("-", "_")
    return f"dqs_{clean_ds}_{clean_p}"


@dataclass
class DataQualityProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int = 112
    target_final_phase: int = 160
    next_phase: int = 113
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    dry_run: bool = True
    status_label: str = "quality_pass"
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DataQualityDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class QualityRule:
    rule_id: str
    rule_name: str
    rule_domain: str
    dataset_types: List[str]
    severity_label: str
    description: str
    check_function_ref: str
    future_phase_owner: str = "Phase 113"
    manual_review_required: bool = False
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class QualityFinding:
    finding_id: str
    rule_id: str
    finding_type: str
    dataset_type: str
    provider_name: str
    field_name: str = ""
    severity_label: str = "quality_medium"
    status_label: str = "quality_manual_review_required"
    message: str = ""
    recommendation: str = ""
    future_phase_owner: str = "Phase 113"
    manual_review_required: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ManualReviewItem:
    review_id: str
    finding_id: str
    dataset_type: str
    provider_name: str
    priority: str = "quality_medium"
    review_reason: str = ""
    suggested_action: str = ""
    destructive_action_allowed: bool = False
    status_label: str = "quality_manual_review_required"

    def to_dict(self) -> Dict[str, Any]:
        res = asdict(self)
        res["destructive_action_allowed"] = False
        return res


@dataclass
class ProviderQualityScore:
    score_id: str
    provider_name: str
    dataset_type: str
    score: float = 1.0
    status_label: str = "quality_pass"
    critical_findings: int = 0
    high_findings: int = 0
    medium_findings: int = 0
    low_findings: int = 0
    manual_review_required: bool = False
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DatasetQualityScore:
    score_id: str
    dataset_name: str
    dataset_type: str
    provider_name: str
    score: float = 1.0
    status_label: str = "quality_pass"
    row_count: int = 0
    checked_rules: int = 0
    failed_rules: int = 0
    manual_review_required: bool = False
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
