"""Feature Namespace Collision Validation.

Validates that feature columns adhere to double-underscore delimiter standards
and do not collide across domain or family hierarchies.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)

STANDARD_ALLOWED_PREFIXES = [
    "fx",
    "commodity",
    "macro",
    "calendar",
    "news",
    "tech",
    "feature",
    "grid",
    "cross",
    "fusion",
]


def build_namespace_collision_validation_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of namespace collision validation rules."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "rule_name": "double_underscore_hierarchy",
            "description": "Cross-domain features must follow <domain>__<family>__... format.",
            "severity": "validation_medium",
            "enforced": True,
        },
        {
            "rule_name": "allowed_domain_prefix",
            "description": "Feature column prefixes must belong to registered domain prefixes.",
            "severity": "validation_medium",
            "enforced": True,
        },
        {
            "rule_name": "no_name_stem_collision",
            "description": "Features from different families must not have colliding trailing stems.",
            "severity": "validation_low",
            "enforced": True,
        },
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_rules": len(records),
        "allowed_prefixes": STANDARD_ALLOWED_PREFIXES,
        "non_signal": True,
    }
    return df, summary


def validate_feature_namespace_collisions(feature_columns: List[str]) -> Dict[str, Any]:
    """Check for naming collisions in feature column names."""
    collisions: List[Dict[str, str]] = []
    seen_stems: Dict[str, str] = {}

    for col in feature_columns:
        if "__" in col:
            parts = col.split("__")
            stem = parts[-1]
            if stem in seen_stems and seen_stems[stem] != col:
                collisions.append({
                    "column_a": seen_stems[stem],
                    "column_b": col,
                    "colliding_stem": stem,
                    "severity": "validation_low",
                })
            else:
                seen_stems[stem] = col

    passed = len(collisions) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_pass_with_warnings",
        "total_columns": len(feature_columns),
        "collision_count": len(collisions),
        "collisions": collisions,
        "manual_review_required": not passed,
    }


def validate_required_domain_prefixes(
    feature_columns: List[str], allowed_prefixes: List[str] | None = None
) -> Dict[str, Any]:
    """Verify that namespaced columns start with one of the allowed domain prefixes."""
    allowed = allowed_prefixes or STANDARD_ALLOWED_PREFIXES
    violations: List[Dict[str, str]] = []

    for col in feature_columns:
        if "__" in col:
            prefix = col.split("__")[0]
            if prefix not in allowed:
                violations.append({
                    "column": col,
                    "prefix": prefix,
                    "severity": "validation_medium",
                })

    passed = len(violations) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_pass_with_warnings",
        "total_namespaced_columns": sum(1 for c in feature_columns if "__" in c),
        "violation_count": len(violations),
        "violations": violations,
        "allowed_prefixes": allowed,
        "manual_review_required": not passed,
    }


def summarize_namespace_collision_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize namespace compliance for DataFrame feature columns."""
    feat_cols = [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    res_coll = validate_feature_namespace_collisions(feat_cols)
    res_pref = validate_required_domain_prefixes(feat_cols)

    passed = res_coll["passed"] and res_pref["passed"]
    return {
        "passed": passed,
        "status": "validation_pass" if passed else "validation_pass_with_warnings",
        "stem_collision_count": res_coll["collision_count"],
        "prefix_violation_count": res_pref["violation_count"],
        "manual_review_required": not passed,
    }


def validate_namespace_collisions(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate case-insensitive collisions and ambiguous naming collisions."""
    cols = [str(c) for c in df.columns]
    seen_lower: Dict[str, str] = {}
    collisions: List[Dict[str, str]] = []

    for col in cols:
        low = col.lower()
        if low in seen_lower and seen_lower[low] != col:
            collisions.append({
                "column_a": seen_lower[low],
                "column_b": col,
                "reason": "case_insensitive_collision",
            })
        else:
            seen_lower[low] = col

    # Also check double-underscore collisions
    feat_cols = [c for c in cols if c not in ("timestamp", "asset_id", "symbol")]
    stem_res = validate_feature_namespace_collisions(feat_cols)
    collisions.extend(stem_res["collisions"])

    collision_count = len(collisions)
    is_valid = collision_count == 0

    return {
        "is_valid": is_valid,
        "collision_count": collision_count,
        "collisions": collisions,
        "destructive_action_allowed": False,
        "current_phase": 121,
    }

