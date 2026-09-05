from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any


@dataclass
class FeatureEngineProfileItem:
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
class FeatureEngineDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str]
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureInputContract:
    contract_id: str
    dataset_type: str
    required_fields: List[str]
    optional_fields: List[str]
    timestamp_field: str
    symbol_field: str
    provider_field: str
    quality_dependency: str
    normalization_dependency: str
    lineage_dependency: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureSchema:
    schema_id: str
    feature_name: str
    feature_type: str
    dataset_type: str
    output_field: str
    value_type: str
    lookback_window: Optional[int]
    required_input_fields: List[str]
    non_signal: bool
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FactorSchema:
    factor_id: str
    factor_name: str
    factor_type: str
    description: str
    required_features: List[str]
    output_field: str
    non_signal: bool
    future_phase_owner: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class IndicatorCatalogItem:
    indicator_id: str
    indicator_name: str
    indicator_family: str
    feature_type: str
    dataset_types: List[str]
    required_fields: List[str]
    default_windows: List[int]
    formula_note: str
    non_signal_usage_note: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureComputationResult:
    result_id: str
    feature_name: str
    dataset_type: str
    provider_name: str
    output_field: str
    row_count: int
    non_signal: bool
    warnings: List[str] = field(default_factory=list)
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureValidationFinding:
    finding_id: str
    feature_name: str
    dataset_type: str
    severity_label: str
    status_label: str
    message: str
    recommendation: str
    manual_review_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def build_feature_engine_profile_id(profile_name: str) -> str:
    return f"fep_{profile_name.strip().lower()}"


def build_feature_engine_domain_id(domain_label: str) -> str:
    clean = domain_label.replace("feature_engine_", "").replace("_domain", "").strip().lower()
    return f"fed_{clean}"


def build_feature_input_contract_id(dataset_type: str) -> str:
    clean = dataset_type.replace("dataset_", "").strip().lower()
    return f"fic_{clean}"


def build_feature_schema_id(feature_name: str, dataset_type: str) -> str:
    clean_ds = dataset_type.replace("dataset_", "").strip().lower()
    return f"fs_{clean_ds}_{feature_name.strip().lower()}"


def build_factor_schema_id(factor_name: str) -> str:
    return f"fact_{factor_name.strip().lower()}"


def build_indicator_catalog_id(indicator_name: str, indicator_family: str) -> str:
    clean_fam = indicator_family.strip().lower().replace(" ", "_")
    clean_ind = indicator_name.strip().lower().replace(" ", "_")
    return f"ind_{clean_fam}_{clean_ind}"


def build_feature_computation_result_id(feature_name: str, provider_name: str) -> str:
    clean_feat = feature_name.strip().lower().replace(" ", "_")
    clean_prov = provider_name.strip().lower().replace(" ", "_")
    return f"fcr_{clean_feat}_{clean_prov}"


def build_feature_validation_finding_id(feature_name: str, dataset_type: str) -> str:
    clean_feat = feature_name.strip().lower().replace(" ", "_")
    clean_ds = dataset_type.replace("dataset_", "").strip().lower()
    return f"fvf_{clean_ds}_{clean_feat}"
