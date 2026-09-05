"""Phase 122 Factor Validation Dependencies Registry.

Binds factors to Phase 121 validation checks ensuring lookahead-free,
non-signal, and clean feature inputs.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY

VALIDATION_DEPENDENCY_RULES: List[Dict[str, Any]] = [
    {
        "check_id": "val_dep_no_lookahead",
        "check_name": "No-Lookahead Prohibition",
        "source_phase": "Phase 121",
        "validator_module": "advanced_feature_validation.no_lookahead_rules",
        "applies_to_factors": ["ALL_FACTORS"],
        "severity": "CRITICAL",
        "description": "Verifies absence of shift(-1) and forward returns in input feature sets.",
    },
    {
        "check_id": "val_dep_forbidden_columns",
        "check_name": "Forbidden Column Tokens Guard",
        "source_phase": "Phase 121",
        "validator_module": "advanced_feature_validation.forbidden_feature_columns",
        "applies_to_factors": ["ALL_FACTORS"],
        "severity": "CRITICAL",
        "description": "Scans for prohibited keywords (signal, buy, sell, target, prediction, label).",
    },
    {
        "check_id": "val_dep_timestamp_order",
        "check_name": "Monotonic Timestamp Ordering",
        "source_phase": "Phase 121",
        "validator_module": "advanced_feature_validation.timestamp_order_validation",
        "applies_to_factors": ["ALL_FACTORS"],
        "severity": "HIGH",
        "description": "Guarantees strict ascending chronological order without time leaps.",
    },
    {
        "check_id": "val_dep_backward_asof_join",
        "check_name": "Backward-Only Asof Join Verification",
        "source_phase": "Phase 121",
        "validator_module": "advanced_feature_validation.asof_join_validation",
        "applies_to_factors": [
            "factor_macro_inflation_rate_context",
            "factor_cross_asset_context",
            "factor_composite_context_placeholder",
        ],
        "severity": "CRITICAL",
        "description": "Enforces backward-only causality when merging multi-domain matrices.",
    },
    {
        "check_id": "val_dep_macro_release_lag",
        "check_name": "Macro Release Lag Guarantee",
        "source_phase": "Phase 121",
        "validator_module": "advanced_feature_validation.macro_release_lag_validation",
        "applies_to_factors": ["factor_macro_inflation_rate_context"],
        "severity": "HIGH",
        "description": "Verifies macro features are lagged to publication timestamp.",
    },
    {
        "check_id": "val_dep_event_window",
        "check_name": "Calendar Event Window Causality",
        "source_phase": "Phase 121",
        "validator_module": "advanced_feature_validation.event_window_validation",
        "applies_to_factors": ["factor_event_release_context"],
        "severity": "HIGH",
        "description": "Guarantees scheduled event windows are strictly backward-referenced.",
    },
    {
        "check_id": "val_dep_news_metadata_only",
        "check_name": "News Metadata-Only Boundary",
        "source_phase": "Phase 121",
        "validator_module": "advanced_feature_validation.news_metadata_only_validation",
        "applies_to_factors": ["factor_news_attention_context"],
        "severity": "CRITICAL",
        "description": "Enforces zero raw article text, zero web scraping, and zero NLP model sentiment.",
    },
    {
        "check_id": "val_dep_warmup_nan",
        "check_name": "Warmup NaN Preservation",
        "source_phase": "Phase 121",
        "validator_module": "advanced_feature_validation.warmup_nan_validation",
        "applies_to_factors": [
            "factor_trend_multi_window_context",
            "factor_momentum_rsi_roc_context",
            "factor_volatility_atr_realized_context",
            "factor_mean_reversion_zscore_context",
        ],
        "severity": "MEDIUM",
        "description": "Preserves warmup NaNs and rejects destructive naive forward-fill operations.",
    },
    {
        "check_id": "val_dep_numeric_sanity",
        "check_name": "Numeric Sanity & Infinite Value Rejection",
        "source_phase": "Phase 121",
        "validator_module": "advanced_feature_validation.feature_infinite_value_validation",
        "applies_to_factors": ["ALL_FACTORS"],
        "severity": "HIGH",
        "description": "Rejects +inf/-inf and requires values to remain within defined numeric bounds.",
    },
]


def build_factor_validation_dependency_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Validation Dependency Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records: List[Dict[str, Any]] = []
    for rule in VALIDATION_DEPENDENCY_RULES:
        records.append(
            {
                "check_id": rule["check_id"],
                "check_name": rule["check_name"],
                "source_phase": rule["source_phase"],
                "validator_module": rule["validator_module"],
                "applies_to_count": len(rule["applies_to_factors"]),
                "applies_to_factors": rule["applies_to_factors"],
                "severity": rule["severity"],
                "description": rule["description"],
                "non_signal": True,
                "status_label": FACTOR_READY,
            }
        )

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_validation_dependencies": len(records),
        "critical_checks": sum(1 for r in records if r["severity"] == "CRITICAL"),
        "high_checks": sum(1 for r in records if r["severity"] == "HIGH"),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY,
    }
    return df, summary


def summarize_factor_validation_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor validation dependencies DataFrame."""
    return {
        "total_rules": len(df),
        "critical_rules": int((df["severity"] == "CRITICAL").sum()) if "severity" in df else 0,
        "non_signal": True,
    }
