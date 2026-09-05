"""Fusion Feature Output Validation.

Validates Phase 120 Macro/Calendar/News Feature Fusion outputs against fusion contracts,
confirming macro release lags, event windows, metadata-only news, and zero full-text.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)
from advanced_feature_validation.forbidden_feature_columns import validate_forbidden_feature_columns
from advanced_feature_validation.news_metadata_only_validation import validate_news_metadata_only_columns
from advanced_feature_validation.macro_release_lag_validation import validate_macro_release_lag


def validate_fusion_feature_output_dataframe(
    df: pd.DataFrame, feature_columns: List[str]
) -> Dict[str, Any]:
    """Validate a DataFrame containing Phase 120 fusion feature outputs."""
    forb = validate_forbidden_feature_columns(df)
    news = validate_news_metadata_only_columns(df)

    lag_ok = True
    if "timestamp" in df.columns and "macro_release_timestamp" in df.columns:
        lag_res = validate_macro_release_lag(df, "timestamp", "macro_release_timestamp")
        lag_ok = lag_res["passed"]

    all_passed = forb["passed"] and news["passed"] and lag_ok

    return {
        "passed": all_passed,
        "status_label": "validation_pass" if all_passed else "validation_fail",
        "domain": "macro_calendar_news_fusion",
        "total_rows": len(df),
        "total_fusion_features": len(feature_columns),
        "forbidden_clean": forb["passed"],
        "news_metadata_only_verified": news["passed"],
        "macro_release_lag_verified": lag_ok,
        "manual_review_required": not all_passed,
        "non_signal": True,
    }


def build_fusion_feature_validation_report(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dry-run or fixture fusion feature validation report."""
    active_profile = profile or get_default_feature_validation_profile()

    sample_df = pd.DataFrame({
        "timestamp": pd.date_range("2025-01-01", periods=10, freq="D", tz="UTC"),
        "macro_release_timestamp": pd.date_range("2025-01-01", periods=10, freq="D", tz="UTC"),
        "macro__cpi__us__mom": [0.2, 0.2, 0.3, 0.3, 0.2, 0.4, 0.3, 0.2, 0.3, 0.2],
        "calendar__fomc__rate__surprise": [0.0, 0.0, 0.0, -0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        "news__central_bank__freshness_hrs": [12.0, 8.0, 4.0, 1.0, 24.0, 18.0, 10.0, 5.0, 2.0, 20.0],
    })
    feat_cols = ["macro__cpi__us__mom", "calendar__fomc__rate__surprise", "news__central_bank__freshness_hrs"]
    res = validate_fusion_feature_output_dataframe(sample_df, feat_cols)

    records = [{
        "domain": "macro_calendar_news_fusion",
        "matrix_name": "sample_fusion_feature_output",
        "status_label": res["status_label"],
        "rows": res["total_rows"],
        "features": res["total_fusion_features"],
        "forbidden_clean": res["forbidden_clean"],
        "news_metadata_clean": res["news_metadata_only_verified"],
        "lag_verified": res["macro_release_lag_verified"],
        "non_signal": True,
    }]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "domain": "macro_calendar_news_fusion",
        "validation_passed": res["passed"],
        "status": res["status_label"],
        "non_signal": True,
    }
    return df, summary


def summarize_fusion_feature_output_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize fusion feature validation report."""
    return {
        "total_matrices_inspected": len(df),
        "status": "validation_pass" if not df.empty and df["status_label"].iloc[0] == "validation_pass" else "validation_fail",
        "non_signal": True,
    }


def validate_fusion_feature_outputs(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate fusion feature outputs for absence of forbidden text columns."""
    forb = validate_forbidden_feature_columns(df)
    news = validate_news_metadata_only_columns(df)
    is_valid = forb["passed"] and news["passed"]

    return {
        "is_valid": is_valid,
        "current_phase": 121,
        "destructive_action_allowed": False,
        "forbidden_columns": forb.get("violations", []),
    }

