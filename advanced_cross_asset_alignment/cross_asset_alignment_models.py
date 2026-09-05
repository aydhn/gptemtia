from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any
import re


def _slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_]+", "_", text.strip())
    return cleaned.strip("_").lower()


def build_cross_asset_alignment_profile_id(profile_name: str) -> str:
    return f"caap_{_slugify(profile_name)}"


def build_cross_asset_alignment_domain_id(domain_label: str) -> str:
    return f"caad_{_slugify(domain_label)}"


def build_asset_universe_alignment_id(asset_domain: str, canonical_symbol: str) -> str:
    return f"aua_{_slugify(asset_domain)}_{_slugify(canonical_symbol)}"


def build_asset_symbol_mapping_id(*args) -> str:
    if len(args) == 4:
        s_dom, s_sym, t_dom, t_sym = args
        return f"asm_{_slugify(s_dom)}_{_slugify(s_sym)}_to_{_slugify(t_dom)}_{_slugify(t_sym)}"
    elif len(args) == 2:
        return f"asm_{_slugify(args[0])}_{_slugify(args[1])}"
    return f"asm_{'_'.join(_slugify(str(a)) for a in args)}"


def build_timestamp_contract_id(name: str) -> str:
    return f"tac_{_slugify(name)}"


def build_session_calendar_id(name: str) -> str:
    return f"sca_{_slugify(name)}"


def build_feature_matrix_contract_id(matrix_name: str) -> str:
    return f"fmc_{_slugify(matrix_name)}"


def build_alignment_join_policy_id(policy_name: str) -> str:
    return f"ajp_{_slugify(policy_name)}"


def build_join_policy_id(name: str) -> str:
    return f"fmjp_{_slugify(name)}"


def build_cross_asset_feature_metadata_id(feature_name: str, aligned_domain: str) -> str:
    return f"cafm_{_slugify(feature_name)}_{_slugify(aligned_domain)}"


def build_aligned_feature_matrix_manifest_id(matrix_name: str) -> str:
    return f"afmm_{_slugify(matrix_name)}"


def build_cross_asset_alignment_finding_id(finding_type: str, alignment_family: str) -> str:
    return f"caaf_{_slugify(finding_type)}_{_slugify(alignment_family)}"



@dataclass
class CrossAssetAlignmentProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int = 119
    target_final_phase: int = 160
    next_phase: int = 120
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    dry_run: bool = True
    non_signal: bool = True
    status_label: str = "alignment_ready"
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CrossAssetAlignmentDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class AssetUniverseAlignment:
    universe_id: str
    asset_domain: str
    canonical_symbol: str
    related_symbols: List[str] = field(default_factory=list)
    related_macro_indicators: List[str] = field(default_factory=list)
    related_calendar_events: List[str] = field(default_factory=list)
    related_news_tags: List[str] = field(default_factory=list)
    alignment_note: str = ""
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class AssetSymbolMapping:
    mapping_id: str
    source_domain: str
    target_domain: str
    source_symbol: str
    canonical_symbol: str
    target_reference: str
    mapping_type: str = "one_to_one"
    confidence_label: str = "high"
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TimestampAlignmentContract:
    contract_id: str
    target_frequency: str = "daily"
    timezone: str = "UTC"
    format_standard: str = "ISO_8601"
    monotonicity_required: bool = True
    no_future_allowed: bool = True
    non_signal: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SessionCalendarAlignment:
    session_id: str
    session_name: str
    calendar_type: str = "fx_24_5"
    utc_bucket: str = "utc_day"
    non_signal: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FeatureMatrixContract:
    contract_id: str
    matrix_name: str
    base_domain: str
    aligned_domains: List[str]
    timestamp_field: str = "normalized_timestamp"
    symbol_field: str = "canonical_symbol"
    feature_namespace: str = "cross_asset"
    join_policy: str = "join_policy_asof_backward"
    no_lookahead_policy: str = "backward_only_no_future"
    non_signal: bool = True
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class AlignmentJoinPolicy:
    policy_id: str
    policy_name: str
    join_policy_label: str
    left_timestamp_field: str = "normalized_timestamp"
    right_timestamp_field: str = "normalized_timestamp"
    tolerance_note: str = "backward_exact_or_prior"
    backward_only: bool = True
    future_data_allowed: bool = False
    non_signal: bool = True
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


FeatureMatrixJoinPolicy = AlignmentJoinPolicy



@dataclass
class CrossAssetFeatureMetadata:
    metadata_id: str
    feature_name: str
    source_domain: str
    aligned_domain: str
    canonical_symbol: str
    timestamp_policy: str = "canonical_utc"
    namespace: str = "cross_domain"
    non_signal: bool = True
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class AlignedFeatureMatrixManifest:
    manifest_id: str
    matrix_name: str
    base_domain: str
    aligned_domains: List[str]
    row_count: int = 0
    feature_count: int = 0
    join_policy: str = "join_policy_asof_backward"
    source_preserved: bool = True
    non_signal: bool = True
    contains_target_or_prediction: bool = False
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CrossAssetAlignmentFinding:
    finding_id: str
    finding_type: str
    alignment_family: str
    severity_label: str = "info"
    status_label: str = "alignment_ready"
    message: str = ""
    recommendation: str = ""
    manual_review_required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


CrossAssetAlignmentValidationFinding = CrossAssetAlignmentFinding
build_cross_asset_validation_finding_id = build_cross_asset_alignment_finding_id

FORBIDDEN_OUTPUT_WORDS = [
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
    "future_return",
    "forward_return",
    "next_return",
]


