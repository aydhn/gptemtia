from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any


FORBIDDEN_OUTPUT_TERMS = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
]


def validate_no_forbidden_terms_in_fields(fields: List[str]) -> None:
    for f in fields:
        low = f.lower()
        for term in FORBIDDEN_OUTPUT_TERMS:
            if term in low:
                raise ValueError(f"Alan adı '{f}' yasaklı terim '{term}' içeremez.")


@dataclass
class FusionFeatureProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int = 120
    target_final_phase: int = 160
    next_phase: int = 121
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    dry_run: bool = True
    non_signal: bool = True
    metadata_only_news: bool = True
    status_label: str = "fusion_ready"
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FusionFeatureDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FusionContract:
    contract_id: str
    contract_name: str
    fusion_family: str
    source_domains: List[str]
    required_fields: List[str]
    optional_fields: List[str]
    timestamp_field: str
    join_policy: str
    no_lookahead_policy: str = "strictly_enforced_no_future_data"
    metadata_only_required: bool = True
    non_signal: bool = True
    manual_review_required: bool = False

    def __post_init__(self):
        validate_no_forbidden_terms_in_fields(self.required_fields)
        validate_no_forbidden_terms_in_fields(self.optional_fields)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FusionPolicy:
    policy_id: str
    policy_name: str
    policy_type: str
    description: str
    future_data_allowed: bool = False
    full_text_allowed: bool = False
    destructive_action_allowed: bool = False
    non_signal: bool = True
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FusionFeatureMetadata:
    metadata_id: str = ""
    feature_name: str = ""
    fusion_family: str = ""
    feature_family: str = ""
    source_domains: List[str] = field(default_factory=list)
    timestamp_policy: str = "backward_asof"
    join_policy: str = "backward_only"
    metadata_only_news: bool = True
    no_lookahead_checked: bool = True
    non_signal: bool = True
    manual_review_required: bool = False
    feature_id: str = ""
    name: str = ""
    domain: str = ""
    description: str = ""
    input_columns: List[str] = field(default_factory=list)
    dtype: str = "float64"
    is_placeholder: bool = False
    is_signal: bool = False
    is_strictly_metadata: bool = True

    def __post_init__(self):
        if not self.feature_id and self.metadata_id:
            self.feature_id = self.metadata_id
        if not self.metadata_id and self.feature_id:
            self.metadata_id = self.feature_id
        if not self.name and self.feature_name:
            self.name = self.feature_name
        if not self.feature_name and self.name:
            self.feature_name = self.name
        if not self.feature_family and self.fusion_family:
            self.feature_family = self.fusion_family
        if not self.fusion_family and self.feature_family:
            self.fusion_family = self.feature_family
        validate_no_forbidden_terms_in_fields([self.feature_name or self.name or ""])

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FusionFeatureMatrixManifest:
    manifest_id: str = ""
    matrix_name: str = ""
    source_domains: List[str] = field(default_factory=list)
    row_count: int = 0
    feature_count: int = 0
    join_policy: str = "backward_only"
    source_preserved: bool = True
    non_signal: bool = True
    contains_target_or_prediction: bool = False
    contains_full_article_text: bool = False
    manual_review_required: bool = False
    matrix_id: str = ""
    profile_name: str = ""
    total_rows: int = 0
    total_columns: int = 0
    feature_columns: List[str] = field(default_factory=list)
    domains_included: List[str] = field(default_factory=list)
    start_timestamp: str = ""
    end_timestamp: str = ""
    is_monotonic_increasing: bool = True
    no_lookahead_guaranteed: bool = True
    is_strictly_metadata_only: bool = True
    is_non_signal_guaranteed: bool = True
    created_at: str = ""

    def __post_init__(self):
        if not self.manifest_id and self.matrix_id:
            self.manifest_id = self.matrix_id
        if not self.matrix_id and self.manifest_id:
            self.matrix_id = self.manifest_id
        if not self.row_count and self.total_rows:
            self.row_count = self.total_rows
        if not self.total_rows and self.row_count:
            self.total_rows = self.row_count
        if not self.feature_count and self.total_columns:
            self.feature_count = self.total_columns
        if not self.total_columns and self.feature_count:
            self.total_columns = self.feature_count
        if not self.source_domains and self.domains_included:
            self.source_domains = self.domains_included
        if not self.domains_included and self.source_domains:
            self.domains_included = self.source_domains

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FusionValidationFinding:
    finding_id: str = ""
    finding_type: str = "validation"
    fusion_family: str = "general"
    severity_label: str = "HIGH"
    status_label: str = "ACTIVE"
    message: str = ""
    recommendation: str = ""
    manual_review_required: bool = False
    rule_id: str = ""
    severity: str = "HIGH"
    target_field: str = ""
    is_blocking: bool = True

    def __post_init__(self):
        if not self.severity_label and self.severity:
            self.severity_label = self.severity
        if not self.severity and self.severity_label:
            self.severity = self.severity_label

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def build_fusion_feature_profile_id(profile_name: str) -> str:
    return f"ff_prof_{profile_name.lower().replace(' ', '_')}"


def build_fusion_feature_domain_id(domain_label: str) -> str:
    return f"ff_dom_{domain_label.lower().replace(' ', '_')}"


def build_fusion_contract_id(contract_name: str, fusion_family: str) -> str:
    return f"ff_cnt_{fusion_family}_{contract_name.lower().replace(' ', '_')}"


def build_fusion_policy_id(policy_name: str, policy_type: str) -> str:
    return f"ff_pol_{policy_type}_{policy_name.lower().replace(' ', '_')}"


def build_fusion_feature_metadata_id(feature_name: str, fusion_family: str) -> str:
    return f"ff_meta_{fusion_family}_{feature_name.lower().replace(' ', '_')}"


def build_fusion_feature_matrix_manifest_id(matrix_name: str) -> str:
    return f"ff_mnf_{matrix_name.lower().replace(' ', '_')}"


def build_fusion_validation_finding_id(finding_type: str, fusion_family: str) -> str:
    return f"ff_fnd_{fusion_family}_{finding_type.lower().replace(' ', '_')}"
