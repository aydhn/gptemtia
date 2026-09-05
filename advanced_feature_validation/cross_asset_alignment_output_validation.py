"""Cross-Asset Alignment Output Validation.

Validates Phase 119 Cross-Asset Alignment outputs against alignment contracts,
confirming backward-only asof joins, namespace delimiters, and cross-domain integrity.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)
from advanced_feature_validation.forbidden_feature_columns import validate_forbidden_feature_columns
from advanced_feature_validation.namespace_collision_validation import validate_required_domain_prefixes
from advanced_feature_validation.asof_join_validation import validate_backward_asof_join_result
from advanced_feature_validation.no_lookahead_rules import validate_no_forward_return_columns


def validate_cross_asset_alignment_output_dataframe(
    df: pd.DataFrame, feature_columns: List[str]
) -> Dict[str, Any]:
    """Validate a DataFrame containing Phase 119 cross-asset aligned features."""
    forb = validate_forbidden_feature_columns(df)
    pref = validate_required_domain_prefixes(feature_columns)
    fwd = validate_no_forward_return_columns(df)

    asof_ok = True
    if "timestamp" in df.columns and any("context_timestamp" in c for c in df.columns):
        asof_res = validate_backward_asof_join_result(df, "timestamp", "context_timestamp")
        asof_ok = asof_res["passed"]

    all_passed = forb["passed"] and pref["passed"] and fwd["passed"] and asof_ok

    return {
        "passed": all_passed,
        "status_label": "validation_pass" if all_passed else "validation_fail",
        "domain": "cross_asset_alignment",
        "total_rows": len(df),
        "total_aligned_features": len(feature_columns),
        "forbidden_clean": forb["passed"],
        "domain_prefixes_clean": pref["passed"],
        "backward_asof_verified": asof_ok,
        "manual_review_required": not all_passed,
        "non_signal": True,
    }


def build_cross_asset_alignment_validation_report(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dry-run or fixture cross-asset alignment validation report."""
    active_profile = profile or get_default_feature_validation_profile()

    sample_df = pd.DataFrame({
        "timestamp": pd.date_range("2025-01-01", periods=10, freq="D", tz="UTC"),
        "asset_id": ["EURUSD"] * 10,
        "context_timestamp": pd.date_range("2025-01-01", periods=10, freq="D", tz="UTC"),
        "fx__price__eur_usd__close__w1": [1.08, 1.082, 1.081, 1.083, 1.085, 1.084, 1.086, 1.087, 1.089, 1.088],
        "commodity__price__xau_usd__close__w1": [2600, 2605, 2602, 2610, 2608, 2615, 2612, 2620, 2618, 2625],
    })
    feat_cols = ["fx__price__eur_usd__close__w1", "commodity__price__xau_usd__close__w1"]
    res = validate_cross_asset_alignment_output_dataframe(sample_df, feat_cols)

    records = [{
        "domain": "cross_asset_alignment",
        "matrix_name": "sample_cross_asset_alignment_output",
        "status_label": res["status_label"],
        "rows": res["total_rows"],
        "features": res["total_aligned_features"],
        "forbidden_clean": res["forbidden_clean"],
        "prefixes_clean": res["domain_prefixes_clean"],
        "asof_verified": res["backward_asof_verified"],
        "non_signal": True,
    }]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "domain": "cross_asset_alignment",
        "validation_passed": res["passed"],
        "status": res["status_label"],
        "non_signal": True,
    }
    return df, summary


def summarize_cross_asset_alignment_output_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cross-asset alignment validation report."""
    return {
        "total_matrices_inspected": len(df),
        "status": "validation_pass" if not df.empty and df["status_label"].iloc[0] == "validation_pass" else "validation_fail",
        "non_signal": True,
    }


def validate_cross_asset_alignment_outputs(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate cross-asset alignment outputs for timestamp validity and alignment."""
    if "timestamp" not in df.columns:
        return {"is_valid": False, "current_phase": 121, "destructive_action_allowed": False}

    has_nat = df["timestamp"].isna().any()
    is_valid = not has_nat and len(df) > 0

    return {
        "is_valid": is_valid,
        "current_phase": 121,
        "destructive_action_allowed": False,
        "has_nat_timestamps": bool(has_nat),
    }

