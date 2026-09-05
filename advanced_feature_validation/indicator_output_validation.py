"""Technical Indicator Output Validation.

Validates Phase 117 Technical Indicator calculation outputs against contract schemas,
confirming non-signal labels, numeric sanity, warmup preservation, and lookahead guards.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)
from advanced_feature_validation.forbidden_feature_columns import validate_forbidden_feature_columns
from advanced_feature_validation.no_lookahead_rules import validate_no_forward_return_columns
from advanced_feature_validation.feature_numeric_sanity_validation import validate_numeric_feature_columns
from advanced_feature_validation.feature_infinite_value_validation import validate_no_infinite_values


def validate_indicator_output_dataframe(
    df: pd.DataFrame, feature_columns: List[str]
) -> Dict[str, Any]:
    """Validate a DataFrame containing Phase 117 technical indicator outputs."""
    forb = validate_forbidden_feature_columns(df)
    fwd = validate_no_forward_return_columns(df)
    num = validate_numeric_feature_columns(df, feature_columns)
    inf = validate_no_infinite_values(df, feature_columns)

    all_passed = forb["passed"] and fwd["passed"] and num["passed"] and inf["passed"]

    return {
        "passed": all_passed,
        "status_label": "validation_pass" if all_passed else "validation_fail",
        "domain": "technical_indicators",
        "total_rows": len(df),
        "total_features": len(feature_columns),
        "forbidden_columns_clean": forb["passed"],
        "no_forward_returns": fwd["passed"],
        "numeric_sanity_passed": num["passed"],
        "no_infinite_values": inf["passed"],
        "manual_review_required": not all_passed,
        "non_signal": True,
    }


def build_indicator_output_validation_report(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dry-run or fixture indicator output validation report."""
    active_profile = profile or get_default_feature_validation_profile()

    # Synthetic sample indicators
    sample_df = pd.DataFrame({
        "timestamp": pd.date_range("2025-01-01", periods=10, freq="D", tz="UTC"),
        "asset_id": ["EURUSD"] * 10,
        "sma_20": [1.08, 1.082, 1.081, 1.083, 1.085, 1.084, 1.086, 1.087, 1.089, 1.088],
        "rsi_14": [52.1, 53.4, 51.8, 54.2, 56.1, 55.0, 57.2, 58.0, 60.1, 59.4],
        "atr_14": [0.0045, 0.0046, 0.0044, 0.0047, 0.0048, 0.0046, 0.0049, 0.0050, 0.0051, 0.0049],
    })
    feat_cols = ["sma_20", "rsi_14", "atr_14"]
    res = validate_indicator_output_dataframe(sample_df, feat_cols)

    records = [{
        "domain": "technical_indicators",
        "matrix_name": "sample_indicator_output",
        "status_label": res["status_label"],
        "rows": res["total_rows"],
        "features": res["total_features"],
        "forbidden_clean": res["forbidden_columns_clean"],
        "numeric_clean": res["numeric_sanity_passed"],
        "infinite_clean": res["no_infinite_values"],
        "non_signal": True,
    }]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "domain": "technical_indicators",
        "validation_passed": res["passed"],
        "status": res["status_label"],
        "non_signal": True,
    }
    return df, summary


def summarize_indicator_output_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize technical indicator output validation report."""
    return {
        "total_matrices_inspected": len(df),
        "status": "validation_pass" if not df.empty and df["status_label"].iloc[0] == "validation_pass" else "validation_fail",
        "non_signal": True,
    }


def validate_indicator_outputs(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate indicator outputs for bounds and structural integrity."""
    feat_cols = [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    is_valid = True
    violations = []

    for col in feat_cols:
        col_lower = str(col).lower()
        if "rsi" in col_lower:
            s = df[col].dropna()
            if (s < 0).any() or (s > 100).any():
                is_valid = False
                violations.append(f"{col} values out of bounds [0, 100]")

    return {
        "is_valid": is_valid,
        "current_phase": 121,
        "destructive_action_allowed": False,
        "violations": violations,
    }

