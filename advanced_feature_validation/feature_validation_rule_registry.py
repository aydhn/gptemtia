"""Rule Registry for Phase 121 Feature Validation Layer.

Registers comprehensive rules for forbidden columns, lookahead prevention,
timestamp ordering, asof joins, lag compliance, news boundaries, and matrix hygiene.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)
from advanced_feature_validation.feature_validation_models import (
    FeatureValidationRule,
    build_feature_validation_rule_id,
)

RAW_RULES: List[Dict[str, Any]] = [
    {
        "name": "forbidden_column_validation",
        "family": "validation_family_forbidden_columns",
        "severity": "validation_critical",
        "desc": "Detects prohibited column names such as signal, buy, sell, long, short, position.",
        "inputs": ["column_names"],
        "patterns": ["signal", "buy", "sell", "long", "short", "position"],
    },
    {
        "name": "no_negative_shift_validation",
        "family": "validation_family_no_lookahead",
        "severity": "validation_critical",
        "desc": "Prohibits shift(-1) or future index alignment in feature generation logic.",
        "inputs": ["source_code", "feature_expressions"],
        "patterns": ["shift(-1)", "shift(-", "lead("],
    },
    {
        "name": "no_forward_return_validation",
        "family": "validation_family_no_lookahead",
        "severity": "validation_critical",
        "desc": "Detects forward-looking returns such as forward_return, future_return, next_return.",
        "inputs": ["column_names"],
        "patterns": ["future_return", "forward_return", "next_return", "fwd_ret"],
    },
    {
        "name": "no_target_prediction_validation",
        "family": "validation_family_forbidden_columns",
        "severity": "validation_critical",
        "desc": "Detects target, label, prediction, or recommendation columns in feature matrices.",
        "inputs": ["column_names"],
        "patterns": ["target", "label", "prediction", "recommendation"],
    },
    {
        "name": "timestamp_monotonic_order_validation",
        "family": "validation_family_timestamp_order",
        "severity": "validation_high",
        "desc": "Validates that base timestamp column is strictly non-null and monotonically increasing.",
        "inputs": ["base_timestamp_series"],
        "patterns": ["null_timestamp", "unordered_timestamp"],
    },
    {
        "name": "backward_only_asof_join_validation",
        "family": "validation_family_no_lookahead",
        "severity": "validation_critical",
        "desc": "Enforces that all asof joins specify direction='backward' and never 'nearest' or 'forward'.",
        "inputs": ["join_policies", "context_timestamps"],
        "patterns": ["forward", "nearest", "future_join"],
    },
    {
        "name": "macro_release_lag_validation",
        "family": "validation_family_no_lookahead",
        "severity": "validation_critical",
        "desc": "Ensures macro indicators are joined only on or after their actual release timestamp.",
        "inputs": ["macro_release_timestamp", "base_timestamp"],
        "patterns": ["release_ts_gt_base_ts"],
    },
    {
        "name": "calendar_event_window_validation",
        "family": "validation_family_timestamp_order",
        "severity": "validation_high",
        "desc": "Validates scheduled vs actual event release order and event window bounds.",
        "inputs": ["scheduled_timestamp", "actual_timestamp"],
        "patterns": ["actual_before_scheduled"],
    },
    {
        "name": "news_metadata_only_validation",
        "family": "validation_family_news_metadata_only",
        "severity": "validation_critical",
        "desc": "Enforces metadata-only news usage, blocking full_text, article_body, and raw_content.",
        "inputs": ["column_names", "news_fields"],
        "patterns": ["full_text", "article_body", "raw_content", "scraped_html", "page_html"],
    },
    {
        "name": "warmup_nan_preservation_validation",
        "family": "validation_family_matrix_integrity",
        "severity": "validation_medium",
        "desc": "Ensures warmup NaNs are neither naively filled nor destructively dropped.",
        "inputs": ["feature_series", "window_size"],
        "patterns": ["auto_dropped_nan", "naive_ffill_warmup"],
    },
    {
        "name": "duplicate_feature_validation",
        "family": "validation_family_matrix_integrity",
        "severity": "validation_medium",
        "desc": "Detects duplicate feature column names and perfectly identical feature value series.",
        "inputs": ["column_names", "feature_values"],
        "patterns": ["duplicate_column_name", "identical_series"],
    },
    {
        "name": "namespace_collision_validation",
        "family": "validation_family_namespace",
        "severity": "validation_medium",
        "desc": "Validates double-underscore domain prefixes and prevents namespace collisions.",
        "inputs": ["column_names"],
        "patterns": ["missing_domain_prefix", "namespace_conflict"],
    },
    {
        "name": "numeric_finite_validation",
        "family": "validation_family_numeric_sanity",
        "severity": "validation_high",
        "desc": "Verifies that all numerical feature columns contain strictly finite numeric values.",
        "inputs": ["feature_dtypes", "feature_values"],
        "patterns": ["non_numeric_feature", "string_in_numeric_column"],
    },
    {
        "name": "infinite_value_validation",
        "family": "validation_family_numeric_sanity",
        "severity": "validation_high",
        "desc": "Detects positive or negative infinity and all-NaN degenerated feature columns.",
        "inputs": ["feature_values"],
        "patterns": ["inf", "-inf", "all_nan"],
    },
    {
        "name": "feature_missingness_validation",
        "family": "validation_family_missingness",
        "severity": "validation_medium",
        "desc": "Flags feature columns where missing value ratio exceeds configured threshold.",
        "inputs": ["missing_ratios"],
        "patterns": ["excessive_missingness"],
    },
    {
        "name": "matrix_integrity_contract_validation",
        "family": "validation_family_matrix_integrity",
        "severity": "validation_high",
        "desc": "Validates feature matrix against its registered formal integrity contract.",
        "inputs": ["matrix_dataframe", "integrity_contract"],
        "patterns": ["contract_violation"],
    },
    {
        "name": "non_signal_compliance_validation",
        "family": "validation_family_non_signal",
        "severity": "validation_critical",
        "desc": "Audits feature names and documentation to ensure strict non-signal compliance.",
        "inputs": ["feature_names", "report_text"],
        "patterns": ["kesin al", "kesin sat", "buy signal", "sell signal", "trading recommendation"],
    },
]


def build_feature_validation_rule_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of all validation rules."""
    active_profile = profile or get_default_feature_validation_profile()

    records = []
    for r in RAW_RULES:
        rule_id = build_feature_validation_rule_id(r["name"], r["family"])
        rule_item = FeatureValidationRule(
            rule_id=rule_id,
            rule_name=r["name"],
            validation_family=r["family"],
            severity_label=r["severity"],
            description=r["desc"],
            required_inputs=r["inputs"],
            forbidden_patterns=r["patterns"],
            non_signal_required=True,
            manual_review_required=True,
        )
        records.append(rule_item.to_dict())

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_rules": len(records),
        "enabled_rules": len(records),
        "critical_rules": sum(1 for r in RAW_RULES if r["severity"] == "validation_critical"),
        "high_rules": sum(1 for r in RAW_RULES if r["severity"] == "validation_high"),
        "medium_rules": sum(1 for r in RAW_RULES if r["severity"] == "validation_medium"),
        "validation_families": list({r["family"] for r in RAW_RULES}),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
    }
    return df, summary


def get_feature_validation_rule_registry(
    profile: FeatureValidationProfile | None = None,
) -> List[FeatureValidationRule]:
    """Return list of FeatureValidationRule objects."""
    rules = []
    for i, r in enumerate(RAW_RULES, start=1):
        rid = f"RULE-VAL-{i:03d}"
        rule_item = FeatureValidationRule(
            rule_id=rid,
            rule_name=r["name"],
            validation_family=r["family"],
            severity_label=r["severity"],
            description=r["desc"],
            required_inputs=r["inputs"],
            forbidden_patterns=r["patterns"],
            non_signal_required=True,
            manual_review_required=True,
        )
        rules.append(rule_item)
    return rules


def get_feature_validation_rules_summary(
    profile: FeatureValidationProfile | None = None,
) -> Dict[str, Any]:
    """Return summary of validation rules registry."""
    rules = get_feature_validation_rule_registry(profile)
    return {
        "total_rules": len(rules),
        "enabled_rules": len(rules),
        "current_phase": 121,
        "target_final_phase": 160,
        "next_phase": 122,
        "non_signal": True,
    }


