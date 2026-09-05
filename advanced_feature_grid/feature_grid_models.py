import re
from dataclasses import dataclass, asdict, field
from typing import List, Dict, Any, Optional


FORBIDDEN_OUTPUT_WORDS = [
    "signal", "buy", "sell", "long", "short", "position",
    "target", "label", "prediction", "recommendation"
]


def sanitize_id_part(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_]+", "_", text.strip().lower())
    return re.sub(r"_+", "_", cleaned).strip("_")


def build_feature_grid_profile_id(profile_name: str) -> str:
    return f"fg_prof_{sanitize_id_part(profile_name)}"


def build_feature_grid_domain_id(domain_label: str) -> str:
    return f"fg_dom_{sanitize_id_part(domain_label)}"


def build_window_grid_contract_id(grid_name: str, indicator_name: str) -> str:
    return f"wgc_{sanitize_id_part(grid_name)}_{sanitize_id_part(indicator_name)}"


def build_indicator_parameter_grid_id(indicator_name: str, indicator_family: str) -> str:
    return f"ipg_{sanitize_id_part(indicator_family)}_{sanitize_id_part(indicator_name)}"


def build_feature_grid_output_schema_id(grid_name: str, output_pattern: str) -> str:
    return f"fgos_{sanitize_id_part(grid_name)}_{sanitize_id_part(output_pattern)}"


def build_feature_grid_computation_result_id(grid_name: str, provider_name: str) -> str:
    return f"fgcr_{sanitize_id_part(grid_name)}_{sanitize_id_part(provider_name)}"


def build_feature_grid_validation_finding_id(grid_name: str, finding_type: str) -> str:
    return f"fgvf_{sanitize_id_part(grid_name)}_{sanitize_id_part(finding_type)}"


@dataclass
class FeatureGridProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int = 118
    target_final_phase: int = 160
    next_phase: int = 119
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    dry_run: bool = True
    non_signal: bool = True
    status_label: str = "feature_grid_ready"
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureGridDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class WindowGridContract:
    contract_id: str
    grid_name: str
    indicator_family: str
    indicator_name: str
    allowed_windows: List[int]
    default_windows: List[int]
    min_window: int = 2
    max_window: int = 1000
    warmup_policy: str = "preserve_warmup_nan"
    no_lookahead_policy: str = "strictly_backward_looking"
    non_signal_usage_note: str = "Research feature grid only. Not a trading signal or target label."
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class IndicatorParameterGrid:
    grid_id: str
    indicator_name: str
    indicator_family: str
    parameter_grid: Dict[str, Any]
    output_naming_template: str
    expected_output_count: int
    non_signal: bool = True
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureGridOutputSchema:
    schema_id: str
    grid_name: str
    output_field_pattern: str
    value_type: str = "float64"
    nullable: bool = True
    warmup_nan_expected: bool = True
    forbidden_aliases: List[str] = field(default_factory=lambda: list(FORBIDDEN_OUTPUT_WORDS))
    non_signal: bool = True
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureGridComputationResult:
    result_id: str
    grid_name: str
    indicator_family: str
    dataset_type: str
    provider_name: str
    output_fields: List[str]
    row_count: int
    output_feature_count: int
    non_signal: bool = True
    warnings: List[str] = field(default_factory=list)
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureGridValidationFinding:
    finding_id: str
    grid_name: str
    finding_type: str
    severity_label: str
    status_label: str
    message: str
    recommendation: str
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
