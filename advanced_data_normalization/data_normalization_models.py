from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any


def build_data_normalization_profile_id(profile_name: str) -> str:
    clean = profile_name.strip().lower().replace(" ", "_").replace("-", "_")
    return f"dnp_{clean}"


def build_data_normalization_domain_id(domain_label: str) -> str:
    clean = domain_label.strip().lower().replace(" ", "_").replace("-", "_")
    return f"dnd_{clean}"


def build_normalization_rule_id(rule_name: str, rule_domain: str) -> str:
    clean_name = rule_name.strip().lower().replace(" ", "_").replace("-", "_")
    clean_domain = rule_domain.strip().lower().replace(" ", "_").replace("-", "_")
    return f"norm_rule_{clean_domain}_{clean_name}"


def build_canonical_schema_id(dataset_type: str, schema_version: str) -> str:
    clean_type = dataset_type.strip().lower().replace(" ", "_").replace("-", "_")
    clean_ver = schema_version.strip().lower().replace(" ", "_").replace(".", "_")
    return f"schema_{clean_type}_{clean_ver}"


def build_canonical_field_id(dataset_type: str, field_name: str) -> str:
    clean_type = dataset_type.strip().lower().replace(" ", "_").replace("-", "_")
    clean_fld = field_name.strip().lower().replace(" ", "_").replace("-", "_")
    return f"cfld_{clean_type}_{clean_fld}"


def build_normalization_finding_id(rule_id: str, dataset_type: str, source_field: str) -> str:
    clean_rule = rule_id.strip().lower().replace(" ", "_").replace("-", "_")
    clean_type = dataset_type.strip().lower().replace(" ", "_").replace("-", "_")
    clean_fld = source_field.strip().lower().replace(" ", "_").replace("-", "_") if source_field else "all"
    return f"nfind_{clean_rule}_{clean_type}_{clean_fld}"


def build_normalization_decision_id(finding_id: str) -> str:
    clean_find = finding_id.strip().lower().replace(" ", "_").replace("-", "_")
    return f"ndec_{clean_find}"


def build_normalized_view_manifest_id(dataset_name: str, provider_name: str) -> str:
    clean_ds = dataset_name.strip().lower().replace(" ", "_").replace("-", "_")
    clean_p = provider_name.strip().lower().replace(" ", "_").replace("-", "_")
    return f"nvm_{clean_ds}_{clean_p}"


def build_normalization_score_id(dataset_name: str, provider_name: str) -> str:
    clean_ds = dataset_name.strip().lower().replace(" ", "_").replace("-", "_")
    clean_p = provider_name.strip().lower().replace(" ", "_").replace("-", "_")
    return f"nscore_{clean_ds}_{clean_p}"


@dataclass
class DataNormalizationProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int = 113
    target_final_phase: int = 160
    next_phase: int = 114
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    dry_run: bool = True
    non_destructive: bool = True
    status_label: str = "normalization_applied"
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DataNormalizationDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class NormalizationRule:
    rule_id: str
    rule_name: str
    rule_domain: str
    dataset_types: List[str]
    action_label: str
    description: str
    source_field: str
    target_field: str
    non_destructive: bool = True
    future_phase_owner: str = "Phase 114"
    manual_review_required: bool = False
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CanonicalSchema:
    schema_id: str
    dataset_type: str
    schema_name: str
    schema_version: str
    canonical_fields: List[str]
    primary_key_fields: List[str]
    timestamp_field: str
    provider_field: str
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CanonicalField:
    field_id: str
    dataset_type: str
    canonical_field_name: str
    field_type: str
    required: bool
    nullable: bool
    unit_policy: str
    normalization_note: str
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class NormalizationFinding:
    finding_id: str
    rule_id: str
    dataset_type: str
    source_field: str
    original_value_repr: str
    normalized_value_repr: str
    status_label: str = "normalization_manual_review_required"
    severity_label: str = "normalization_medium"
    message: str = ""
    manual_review_required: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class NormalizationDecision:
    decision_id: str
    finding_id: str
    rule_id: str
    decision_type: str
    decision_note: str
    source_preserved: bool = True
    destructive_action_allowed: bool = False
    lineage_required: bool = True
    future_phase_owner: str = "Phase 114"

    def to_dict(self) -> Dict[str, Any]:
        res = asdict(self)
        res["source_preserved"] = True
        res["destructive_action_allowed"] = False
        return res


@dataclass
class NormalizedViewManifest:
    manifest_id: str
    dataset_name: str
    dataset_type: str
    provider_name: str
    original_ref: str
    normalized_ref: str
    schema_version: str
    row_count: int
    normalized_field_count: int
    source_preserved: bool = True
    destructive_action_allowed: bool = False
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        res = asdict(self)
        res["source_preserved"] = True
        res["destructive_action_allowed"] = False
        return res


@dataclass
class NormalizationScore:
    score_id: str
    dataset_name: str
    dataset_type: str
    provider_name: str
    score: float
    status_label: str
    applied_rules: int
    manual_review_count: int
    blocked_count: int
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
