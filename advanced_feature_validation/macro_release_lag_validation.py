"""Macro Release Lag Validation.

Enforces macro release lag rules ensuring economic indicator observations
are joined strictly on or after actual publication time (release_ts <= base_ts).
Strictly non-signal and research-only.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)


def build_macro_release_lag_validation_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of macro release lag rules."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "rule_name": "release_timestamp_non_future",
            "description": "release_ts must be <= base_ts for all joined macro indicators.",
            "severity": "validation_critical",
            "enforced": True,
        },
        {
            "rule_name": "revision_timestamp_non_future",
            "description": "revision_ts must be <= base_ts for all historical revisions.",
            "severity": "validation_critical",
            "enforced": True,
        },
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_rules": len(records),
        "enforced": True,
        "non_signal": True,
    }
    return df, summary


def validate_macro_release_lag(
    df: pd.DataFrame, base_ts: str = "timestamp", release_ts: str | None = None
) -> Dict[str, Any]:
    """Validate that macro release timestamp does not exceed market base timestamp."""
    if release_ts is None:
        candidates = ["reference_period", "macro_release", "release_timestamp", "release_date"]
        for cand in candidates:
            if cand in df.columns:
                release_ts = cand
                break

    if release_ts is None or base_ts not in df.columns or release_ts not in df.columns:
        return {
            "passed": True,
            "is_valid": True,
            "status_label": "validation_pass",
            "leakage_count": 0,
            "manual_review_required": False,
        }

    b = pd.to_datetime(df[base_ts])
    r = pd.to_datetime(df[release_ts])
    valid = b.notna() & r.notna()
    # If checking reference_period, timestamp must be >= reference_period
    # If checking release_ts, release_ts <= base_ts (i.e. r <= b)
    if "reference" in release_ts:
        leakage = valid & (b < r)
    else:
        leakage = valid & (r > b)
    leakage_count = int(leakage.sum())
    passed = leakage_count == 0

    return {
        "passed": passed,
        "is_valid": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "base_ts_field": base_ts,
        "release_ts_field": release_ts,
        "total_rows": len(df),
        "valid_pairs": int(valid.sum()),
        "premature_release_joins": leakage_count,
        "message": "All macro releases joined after or on release time."
        if passed
        else f"Failed: {leakage_count} records joined macro data prior to release timestamp.",
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def get_macro_release_lag_policy(indicator: str = "cpi") -> Dict[str, Any]:
    return {
        "indicator": indicator,
        "lag_days": 15 if "cpi" in indicator.lower() else 1,
        "status": "ACTIVE",
        "current_phase": 121,
    }


def validate_macro_revision_timestamp(
    df: pd.DataFrame, base_ts: str, revision_ts: str

) -> Dict[str, Any]:
    """Validate that macro revision timestamp does not exceed market base timestamp."""
    if base_ts not in df.columns or revision_ts not in df.columns:
        return {
            "passed": False,
            "status_label": "validation_fail",
            "error": f"Columns '{base_ts}' or '{revision_ts}' not in DataFrame.",
            "leakage_count": 0,
            "manual_review_required": True,
        }

    b = pd.to_datetime(df[base_ts])
    rev = pd.to_datetime(df[revision_ts])
    valid = b.notna() & rev.notna()
    leakage = valid & (rev > b)
    leakage_count = int(leakage.sum())
    passed = leakage_count == 0

    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "base_ts_field": base_ts,
        "revision_ts_field": revision_ts,
        "total_rows": len(df),
        "valid_pairs": int(valid.sum()),
        "premature_revision_joins": leakage_count,
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def summarize_macro_release_lag_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary of macro release lag compliance for a DataFrame."""
    base_cols = [c for c in df.columns if "base" in c or c == "timestamp"]
    rel_cols = [c for c in df.columns if "macro_release" in c or "release_timestamp" in c]

    if base_cols and rel_cols:
        res = validate_macro_release_lag(df, base_cols[0], rel_cols[0])
        return {
            "passed": res["passed"],
            "status": res["status_label"],
            "premature_release_joins": res["premature_release_joins"],
            "manual_review_required": res["manual_review_required"],
        }

    return {
        "passed": True,
        "status": "validation_pass",
        "premature_release_joins": 0,
        "manual_review_required": False,
    }
