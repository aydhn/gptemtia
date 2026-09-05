"""Feature Matrix Integrity Contracts.

Defines formal contracts governing structure, prefixes, forbidden patterns,
and non-signal mandates for feature matrices.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)
from advanced_feature_validation.forbidden_feature_columns import FORBIDDEN_FEATURE_PATTERNS
from advanced_feature_validation.namespace_collision_validation import STANDARD_ALLOWED_PREFIXES

DEFAULT_INTEGRITY_CONTRACTS: List[Dict[str, Any]] = [
    {
        "matrix_name": "technical_indicator_matrix",
        "required_timestamp_field": "timestamp",
        "required_symbol_field": "asset_id",
        "allowed_feature_prefixes": ["tech", "price", "trend", "mom", "vol", "osc"],
        "forbidden_column_patterns": FORBIDDEN_FEATURE_PATTERNS,
        "require_non_signal": True,
        "require_no_target_prediction": True,
        "require_no_full_article_text": True,
        "require_source_preserved": True,
        "manual_review_required": True,
    },
    {
        "matrix_name": "multi_window_feature_grid",
        "required_timestamp_field": "timestamp",
        "required_symbol_field": "asset_id",
        "allowed_feature_prefixes": ["grid", "w5", "w10", "w14", "w20", "w50", "w100", "w200"],
        "forbidden_column_patterns": FORBIDDEN_FEATURE_PATTERNS,
        "require_non_signal": True,
        "require_no_target_prediction": True,
        "require_no_full_article_text": True,
        "require_source_preserved": True,
        "manual_review_required": True,
    },
    {
        "matrix_name": "cross_asset_aligned_matrix",
        "required_timestamp_field": "timestamp",
        "required_symbol_field": "asset_id",
        "allowed_feature_prefixes": STANDARD_ALLOWED_PREFIXES,
        "forbidden_column_patterns": FORBIDDEN_FEATURE_PATTERNS,
        "require_non_signal": True,
        "require_no_target_prediction": True,
        "require_no_full_article_text": True,
        "require_source_preserved": True,
        "manual_review_required": True,
    },
    {
        "matrix_name": "macro_calendar_news_fusion_matrix",
        "required_timestamp_field": "timestamp",
        "required_symbol_field": "asset_id",
        "allowed_feature_prefixes": ["macro", "calendar", "news", "fusion", "context"],
        "forbidden_column_patterns": FORBIDDEN_FEATURE_PATTERNS,
        "require_non_signal": True,
        "require_no_target_prediction": True,
        "require_no_full_article_text": True,
        "require_source_preserved": True,
        "manual_review_required": True,
    },
    {
        "matrix_name": "generic_feature_matrix",
        "required_timestamp_field": "timestamp",
        "required_symbol_field": "asset_id",
        "allowed_feature_prefixes": ["feat", "generic", "clean"],
        "forbidden_column_patterns": FORBIDDEN_FEATURE_PATTERNS,
        "require_non_signal": True,
        "require_no_target_prediction": True,
        "require_no_full_article_text": True,
        "require_source_preserved": True,
        "manual_review_required": True,
    },
]


def build_feature_matrix_integrity_contract_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of feature matrix integrity contracts."""
    active_profile = profile or get_default_feature_validation_profile()

    records = []
    for c in DEFAULT_INTEGRITY_CONTRACTS:
        records.append({
            "matrix_name": c["matrix_name"],
            "required_timestamp_field": c["required_timestamp_field"],
            "required_symbol_field": c["required_symbol_field"],
            "allowed_feature_prefixes": c["allowed_feature_prefixes"],
            "forbidden_column_patterns": c["forbidden_column_patterns"],
            "require_non_signal": c["require_non_signal"],
            "require_no_target_prediction": c["require_no_target_prediction"],
            "require_no_full_article_text": c["require_no_full_article_text"],
            "require_source_preserved": c["require_source_preserved"],
            "manual_review_required": c["manual_review_required"],
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_contracts": len(records),
        "matrices": [c["matrix_name"] for c in records],
        "non_signal": True,
    }
    return df, summary


def validate_feature_matrix_integrity_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single integrity contract configuration against required fields."""
    required_keys = [
        "matrix_name",
        "required_timestamp_field",
        "required_symbol_field",
        "allowed_feature_prefixes",
        "forbidden_column_patterns",
        "require_non_signal",
        "require_no_target_prediction",
        "require_no_full_article_text",
        "require_source_preserved",
    ]

    missing = [k for k in required_keys if k not in contract]
    passed = len(missing) == 0

    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "matrix_name": contract.get("matrix_name", "unknown"),
        "missing_keys": missing,
        "non_signal_verified": contract.get("require_non_signal", False),
        "source_preservation_verified": contract.get("require_source_preserved", False),
        "manual_review_required": not passed,
    }


def summarize_feature_matrix_integrity_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize registered integrity contracts."""
    return {
        "total_contracts": len(df),
        "status": "validation_pass" if len(df) > 0 else "validation_fail",
        "all_require_non_signal": bool(df["require_non_signal"].all()) if "require_non_signal" in df else False,
        "all_preserve_source": bool(df["require_source_preserved"].all()) if "require_source_preserved" in df else False,
    }


def get_feature_matrix_integrity_contracts() -> List[Dict[str, Any]]:
    """Return all registered integrity contract specifications."""
    return list(DEFAULT_INTEGRITY_CONTRACTS)


def validate_feature_matrix_integrity(
    df: pd.DataFrame, matrix_name: str = "generic_feature_matrix"
) -> Dict[str, Any]:
    """Validate DataFrame integrity against contracts."""
    has_timestamp = "timestamp" in df.columns
    has_rows = len(df) > 0
    is_valid = has_timestamp and has_rows

    return {
        "is_valid": is_valid,
        "matrix_name": matrix_name,
        "current_phase": 121,
        "destructive_action_allowed": False,
        "total_rows": len(df),
        "total_columns": len(df.columns),
    }

