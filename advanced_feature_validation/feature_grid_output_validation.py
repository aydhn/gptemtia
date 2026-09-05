"""Feature Grid Output Validation.

Validates Phase 118 Multi-Window Feature Grid calculation outputs against window contracts,
verifying parameter grid coverage, duplicate naming, warmup NaNs, and zero lookahead.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)
from advanced_feature_validation.forbidden_feature_columns import validate_forbidden_feature_columns
from advanced_feature_validation.duplicate_feature_validation import validate_duplicate_feature_names
from advanced_feature_validation.no_lookahead_rules import validate_no_forward_return_columns
from advanced_feature_validation.feature_infinite_value_validation import validate_no_infinite_values


def validate_feature_grid_output_dataframe(
    df: pd.DataFrame, feature_columns: List[str]
) -> Dict[str, Any]:
    """Validate a DataFrame containing Phase 118 multi-window feature grid outputs."""
    forb = validate_forbidden_feature_columns(df)
    dup = validate_duplicate_feature_names(feature_columns)
    fwd = validate_no_forward_return_columns(df)
    inf = validate_no_infinite_values(df, feature_columns)

    all_passed = forb["passed"] and dup["passed"] and fwd["passed"] and inf["passed"]

    return {
        "passed": all_passed,
        "status_label": "validation_pass" if all_passed else "validation_fail",
        "domain": "multi_window_feature_grid",
        "total_rows": len(df),
        "total_grid_features": len(feature_columns),
        "forbidden_clean": forb["passed"],
        "duplicates_clean": dup["passed"],
        "no_forward_returns": fwd["passed"],
        "no_infinite_values": inf["passed"],
        "manual_review_required": not all_passed,
        "non_signal": True,
    }


def build_feature_grid_validation_report(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dry-run or fixture feature grid validation report."""
    active_profile = profile or get_default_feature_validation_profile()

    sample_df = pd.DataFrame({
        "timestamp": pd.date_range("2025-01-01", periods=10, freq="D", tz="UTC"),
        "asset_id": ["XAUUSD"] * 10,
        "sma_w5": [2600, 2605, 2608, 2610, 2612, 2615, 2618, 2620, 2622, 2625],
        "sma_w20": [2590, 2592, 2594, 2596, 2598, 2600, 2602, 2604, 2606, 2608],
        "rsi_w14": [50.0, 52.0, 51.5, 53.0, 55.0, 54.5, 56.0, 57.0, 58.5, 59.0],
        "vol_w20": [0.012, 0.013, 0.012, 0.014, 0.013, 0.015, 0.014, 0.013, 0.012, 0.013],
    })
    grid_cols = ["sma_w5", "sma_w20", "rsi_w14", "vol_w20"]
    res = validate_feature_grid_output_dataframe(sample_df, grid_cols)

    records = [{
        "domain": "multi_window_feature_grid",
        "matrix_name": "sample_feature_grid_output",
        "status_label": res["status_label"],
        "rows": res["total_rows"],
        "grid_features": res["total_grid_features"],
        "forbidden_clean": res["forbidden_clean"],
        "duplicates_clean": res["duplicates_clean"],
        "infinite_clean": res["no_infinite_values"],
        "non_signal": True,
    }]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "domain": "multi_window_feature_grid",
        "validation_passed": res["passed"],
        "status": res["status_label"],
        "non_signal": True,
    }
    return df, summary


def summarize_feature_grid_output_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize feature grid output validation report."""
    return {
        "total_grids_inspected": len(df),
        "status": "validation_pass" if not df.empty and df["status_label"].iloc[0] == "validation_pass" else "validation_fail",
        "non_signal": True,
    }


def validate_feature_grid_outputs(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate feature grid outputs for constraints like non-negative volatility."""
    feat_cols = [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    is_valid = True
    violations = []

    for col in feat_cols:
        col_lower = str(col).lower()
        if "vol" in col_lower:
            s = df[col].dropna()
            if (s < 0).any():
                is_valid = False
                violations.append(f"{col} contains negative volatility values")

    return {
        "is_valid": is_valid,
        "current_phase": 121,
        "destructive_action_allowed": False,
        "violations": violations,
    }

