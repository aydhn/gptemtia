"""Phase 122 Factor Metadata Models and Entities.

Defines schemas and dataclasses for factor profiles, families, contracts,
input feature sets, dependencies, manifests, and manual reviews.
Strictly non-signal and research-only.
"""

from dataclasses import asdict, dataclass, field
import hashlib
import re
from typing import Any, Dict, List

FORBIDDEN_FACTOR_TOKENS: List[str] = [
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


def _slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_]+", "_", text.strip().lower())
    return cleaned.strip("_")


def build_factor_metadata_profile_id(profile_name: str) -> str:
    digest = hashlib.sha256(profile_name.encode("utf-8")).hexdigest()[:8]
    return f"prof_{_slugify(profile_name)}_{digest}"


def build_factor_family_id(family_label: str) -> str:
    digest = hashlib.sha256(family_label.encode("utf-8")).hexdigest()[:8]
    return f"fam_{_slugify(family_label)}_{digest}"


def build_factor_contract_id(factor_name: str, factor_family: str) -> str:
    raw = f"{factor_name}:{factor_family}"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:8]
    return f"cntr_{_slugify(factor_name)}_{digest}"


def build_factor_input_feature_set_id(factor_name: str) -> str:
    digest = hashlib.sha256(factor_name.encode("utf-8")).hexdigest()[:8]
    return f"fset_{_slugify(factor_name)}_{digest}"


def build_factor_dependency_id(factor_name: str, dependency_ref: str) -> str:
    raw = f"{factor_name}:{dependency_ref}"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:8]
    return f"dep_{_slugify(factor_name)}_{digest}"


def build_factor_metadata_manifest_id(factor_name: str) -> str:
    digest = hashlib.sha256(factor_name.encode("utf-8")).hexdigest()[:8]
    return f"manf_{_slugify(factor_name)}_{digest}"


def build_factor_manual_review_id(factor_name: str, review_reason: str) -> str:
    raw = f"{factor_name}:{review_reason}"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:8]
    return f"rev_{_slugify(factor_name)}_{digest}"


@dataclass
class FactorMetadataProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int = 122
    target_final_phase: int = 160
    next_phase: int = 123
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    dry_run: bool = True
    non_signal: bool = True
    status_label: str = "factor_ready"
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FactorFamily:
    family_id: str
    family_label: str
    family_name: str
    description: str
    source_feature_families: List[str] = field(default_factory=list)
    expected_inputs: List[str] = field(default_factory=list)
    non_signal_usage_note: str = "Strictly non-signal feature grouping for offline research."
    status_label: str = "factor_ready"
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FactorContract:
    contract_id: str
    factor_name: str
    factor_family: str
    required_feature_sets: List[str] = field(default_factory=list)
    optional_feature_sets: List[str] = field(default_factory=list)
    validation_dependencies: List[str] = field(default_factory=list)
    quality_dependencies: List[str] = field(default_factory=list)
    namespace: str = ""
    output_schema_ref: str = "schema_standard_factor_float64"
    non_signal: bool = True
    manual_review_required: bool = False

    def __post_init__(self):
        if not self.namespace:
            self.namespace = f"factor_{self.factor_name}"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FactorInputFeatureSet:
    feature_set_id: str
    factor_name: str
    factor_family: str
    required_features: List[str] = field(default_factory=list)
    optional_features: List[str] = field(default_factory=list)
    source_phase_refs: List[str] = field(default_factory=list)
    validation_required: bool = True
    non_signal: bool = True
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FactorDependency:
    dependency_id: str
    factor_name: str
    dependency_type: str
    dependency_ref: str
    source_phase: str
    dependency_note: str
    mandatory: bool = True
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FactorMetadataManifest:
    manifest_id: str
    factor_name: str
    factor_family: str
    input_feature_count: int = 0
    dependency_count: int = 0
    validation_dependency_count: int = 0
    quality_dependency_count: int = 0
    non_signal: bool = True
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    source_preserved: bool = True
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FactorManualReviewItem:
    review_id: str
    factor_name: str
    factor_family: str
    review_reason: str
    suggested_action: str
    destructive_action_allowed: bool = False
    status_label: str = "factor_manual_review_required"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
