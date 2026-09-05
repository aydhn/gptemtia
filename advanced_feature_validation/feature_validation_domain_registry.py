"""Domain Registry for Phase 121 Feature Validation Layer.

Defines all functional domains covered by validation and integrity checks.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)
from advanced_feature_validation.feature_validation_models import (
    FeatureValidationDomain,
    build_feature_validation_domain_id,
)

RAW_DOMAINS = [
    {
        "label": "feature_validation_profile_domain",
        "name": "Feature Validation Profile Domain",
        "desc": "Validates profile configuration, phase invariants, and execution boundaries.",
        "outputs": ["validation_profile_manifest", "profile_health_status"],
    },
    {
        "label": "forbidden_column_domain",
        "name": "Forbidden Feature Column Domain",
        "desc": "Detects prohibited terminology such as signals, targets, labels, and full article text.",
        "outputs": ["forbidden_column_registry", "forbidden_column_scan_report"],
    },
    {
        "label": "no_lookahead_domain",
        "name": "No-Lookahead Guard Domain",
        "desc": "Scans code and DataFrames for shift(-1), future returns, and future timestamp leakages.",
        "outputs": ["no_lookahead_rule_registry", "lookahead_finding_report"],
    },
    {
        "label": "timestamp_order_domain",
        "name": "Timestamp Order Validation Domain",
        "desc": "Validates timestamp monotonicity, null checks, and context-vs-base timestamp ordering.",
        "outputs": ["timestamp_order_registry", "timestamp_integrity_report"],
    },
    {
        "label": "asof_join_domain",
        "name": "Asof Join Validation Domain",
        "desc": "Ensures join operations strictly use backward-only direction without future lookup.",
        "outputs": ["asof_join_registry", "asof_direction_report"],
    },
    {
        "label": "macro_release_lag_domain",
        "name": "Macro Release Lag Domain",
        "desc": "Enforces macro release lag rules (release_timestamp <= base_timestamp) and revision checks.",
        "outputs": ["macro_release_lag_registry", "release_lag_compliance_report"],
    },
    {
        "label": "event_window_domain",
        "name": "Calendar Event Window Domain",
        "desc": "Validates scheduled vs actual release event ordering and event window bounds.",
        "outputs": ["event_window_registry", "event_window_timing_report"],
    },
    {
        "label": "news_metadata_only_domain",
        "name": "News Metadata Only Domain",
        "desc": "Enforces metadata-only news boundaries (zero full text, zero raw content, zero scraping).",
        "outputs": ["news_metadata_only_registry", "news_boundary_report"],
    },
    {
        "label": "warmup_nan_domain",
        "name": "Warmup NaN Validation Domain",
        "desc": "Ensures warmup NaNs are preserved transparently without illegal fills or destructive drops.",
        "outputs": ["warmup_nan_registry", "warmup_integrity_report"],
    },
    {
        "label": "duplicate_feature_domain",
        "name": "Duplicate Feature Domain",
        "desc": "Scans for duplicate column names and identical feature value series across matrices.",
        "outputs": ["duplicate_feature_registry", "duplicate_scan_report"],
    },
    {
        "label": "namespace_collision_domain",
        "name": "Namespace Collision Domain",
        "desc": "Validates standard double-underscore prefixes and identifies column namespace collisions.",
        "outputs": ["namespace_collision_registry", "namespace_integrity_report"],
    },
    {
        "label": "numeric_sanity_domain",
        "name": "Feature Numeric Sanity Domain",
        "desc": "Verifies that all numerical feature columns contain strictly numeric types within sane ranges.",
        "outputs": ["numeric_sanity_registry", "numeric_outlier_report"],
    },
    {
        "label": "missingness_domain",
        "name": "Feature Missingness Domain",
        "desc": "Calculates missingness ratios across feature columns and raises warnings when exceeding threshold.",
        "outputs": ["feature_missingness_registry", "missingness_threshold_report"],
    },
    {
        "label": "infinite_value_domain",
        "name": "Feature Infinite Value Domain",
        "desc": "Detects positive/negative infinite values and all-NaN degenerate feature series.",
        "outputs": ["infinite_value_registry", "infinite_value_report"],
    },
    {
        "label": "matrix_integrity_domain",
        "name": "Feature Matrix Integrity Domain",
        "desc": "Evaluates feature matrices against formal integrity contracts and generates manifests.",
        "outputs": ["matrix_integrity_contracts", "matrix_integrity_manifest"],
    },
    {
        "label": "validation_finding_domain",
        "name": "Validation Finding Domain",
        "desc": "Collects, categorizes, and tracks validation findings and severity classifications.",
        "outputs": ["validation_finding_registry", "finding_severity_breakdown"],
    },
    {
        "label": "manual_review_domain",
        "name": "Validation Manual Review Domain",
        "desc": "Organizes flagged items requiring human inspection into a non-destructive review queue.",
        "outputs": ["manual_review_queue", "review_recommendations"],
    },
    {
        "label": "validation_scoring_domain",
        "name": "Validation Scoring Domain",
        "desc": "Calculates normalized 0.0-1.0 feature validation score as an internal quality metric.",
        "outputs": ["validation_score_report", "score_classification_summary"],
    },
    {
        "label": "indicator_output_validation_domain",
        "name": "Indicator Output Validation Domain",
        "desc": "Validates technical indicator calculation outputs from Phase 117 against schema contracts.",
        "outputs": ["indicator_output_validation_report"],
    },
    {
        "label": "feature_grid_validation_domain",
        "name": "Feature Grid Validation Domain",
        "desc": "Validates multi-window feature grid matrices from Phase 118 against window contracts.",
        "outputs": ["feature_grid_validation_report"],
    },
    {
        "label": "cross_asset_alignment_validation_domain",
        "name": "Cross-Asset Alignment Validation Domain",
        "desc": "Validates cross-asset aligned feature matrices from Phase 119 against alignment contracts.",
        "outputs": ["cross_asset_alignment_validation_report"],
    },
    {
        "label": "fusion_feature_validation_domain",
        "name": "Fusion Feature Validation Domain",
        "desc": "Validates macro/calendar/news fusion feature matrices from Phase 120 against fusion contracts.",
        "outputs": ["fusion_feature_validation_report"],
    },
    {
        "label": "no_leakage_guard_domain",
        "name": "No-Leakage Guard Domain",
        "desc": "Provides consolidated real-time and offline leakage defense across all domains.",
        "outputs": ["no_leakage_guard_report"],
    },
    {
        "label": "non_signal_validation_domain",
        "name": "Non-Signal Validation Domain",
        "desc": "Audits feature names, reports, and code to guarantee 100% compliance with non-signal invariants.",
        "outputs": ["non_signal_validation_report"],
    },
    {
        "label": "feature_validation_health_domain",
        "name": "Feature Validation Health Domain",
        "desc": "Assesses pipeline and subsystem operational readiness for validation facilities.",
        "outputs": ["feature_validation_health_check"],
    },
    {
        "label": "feature_validation_safety_domain",
        "name": "Feature Validation Safety Domain",
        "desc": "Maintains strict NO-GO and SAFE-GO boundary invariants across validation operations.",
        "outputs": ["feature_validation_safety_boundary"],
    },
    {
        "label": "phase_122_handoff_domain",
        "name": "Phase 122 Handoff Domain",
        "desc": "Compiles validated feature specifications for downstream Factor Metadata and Families.",
        "outputs": ["phase_122_factor_metadata_handoff_report"],
    },
]


def build_feature_validation_domain_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of all validation domains."""
    active_profile = profile or get_default_feature_validation_profile()

    records = []
    for d in RAW_DOMAINS:
        dom_id = build_feature_validation_domain_id(d["label"])
        domain_item = FeatureValidationDomain(
            domain_id=dom_id,
            domain_label=d["label"],
            domain_name=d["name"],
            description=d["desc"],
            required_outputs=d["outputs"],
            warnings=[],
        )
        records.append(domain_item.to_dict())

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_domains": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
        "domain_names": [d["label"] for d in RAW_DOMAINS],
    }
    return df, summary


def get_feature_validation_domains_registry(
    profile: FeatureValidationProfile | None = None,
) -> Dict[str, Any]:
    """Return dictionary of feature validation domains."""
    return {
        "fx": {"domain": "fx", "name": "FX Domain"},
        "commodity": {"domain": "commodity", "name": "Commodity Domain"},
        "macro": {"domain": "macro", "name": "Macro Domain"},
        "calendar": {"domain": "calendar", "name": "Calendar Domain"},
        "news_metadata": {"domain": "news_metadata", "name": "News Metadata Domain"},
        "cross_asset": {"domain": "cross_asset", "name": "Cross-Asset Domain"},
    }


def get_feature_validation_domains_summary(
    profile: FeatureValidationProfile | None = None,
) -> Dict[str, Any]:
    """Return summary of feature validation domains."""
    return {
        "total_domains": 6,
        "current_phase": 121,
        "target_final_phase": 160,
        "next_phase": 122,
        "non_signal": True,
    }


