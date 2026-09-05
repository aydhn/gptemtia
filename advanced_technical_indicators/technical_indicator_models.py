from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any


@dataclass
class TechnicalIndicatorProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    next_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    dry_run: bool
    non_signal: bool
    status_label: str
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TechnicalIndicatorDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str]
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TechnicalIndicatorCatalogItem:
    indicator_id: str
    indicator_name: str
    indicator_family: str
    required_fields: List[str]
    optional_fields: List[str]
    output_fields: List[str]
    default_parameters: Dict[str, Any]
    formula_note: str
    warmup_policy: str
    no_lookahead_policy: str
    non_signal_usage_note: str
    status_label: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class IndicatorParameterContract:
    parameter_id: str
    indicator_name: str
    parameter_name: str
    parameter_type: str
    default_value: Any
    min_value: Optional[float]
    max_value: Optional[float]
    allowed_values: List[str]
    validation_note: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class IndicatorOutputSchema:
    schema_id: str
    indicator_name: str
    output_field: str
    value_type: str
    nullable: bool
    warmup_nan_expected: bool
    non_signal: bool
    forbidden_aliases: List[str]
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class IndicatorComputationResult:
    result_id: str
    indicator_name: str
    indicator_family: str
    dataset_type: str
    provider_name: str
    output_fields: List[str]
    row_count: int
    non_signal: bool
    warnings: List[str] = field(default_factory=list)
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class IndicatorValidationFinding:
    finding_id: str
    indicator_name: str
    finding_type: str
    severity_label: str
    status_label: str
    message: str
    recommendation: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def build_technical_indicator_profile_id(profile_name: str) -> str:
    return f"tiprof_{profile_name.lower()}"


def build_technical_indicator_domain_id(domain_label: str) -> str:
    return f"tidom_{domain_label.lower()}"


def build_technical_indicator_id(indicator_name: str, indicator_family: str) -> str:
    return f"ti_{indicator_family.lower()}_{indicator_name.lower()}"


def build_indicator_parameter_id(indicator_name: str, parameter_name: str) -> str:
    return f"tiparam_{indicator_name.lower()}_{parameter_name.lower()}"


def build_indicator_output_schema_id(indicator_name: str, output_field: str) -> str:
    return f"tischema_{indicator_name.lower()}_{output_field.lower()}"


def build_indicator_computation_result_id(indicator_name: str, provider_name: str) -> str:
    return f"ticomp_{indicator_name.lower()}_{provider_name.lower()}"


def build_indicator_validation_finding_id(indicator_name: str, finding_type: str) -> str:
    return f"tival_{indicator_name.lower()}_{finding_type.lower()}"
