"""Phase 123 Feature Quality and Drift Manifest.

Assembles an immutable governance manifest detailing quality diagnostics, drift metrics,
factor-level readiness, and safety invariants for handoff to Phase 124 Feature Store integration.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)


def create_feature_quality_drift_manifest(
    manifest_id: str = "manifest_phase_123_quality_drift",
    matrix_or_factor_name: str = "cross_asset_factor_matrix_v1",
    source_phase_refs: List[int] | None = None,
    feature_count: int = 42,
    factor_family_count: int = 10,
    missingness_warning_count: int = 0,
    infinite_value_count: int = 0,
    all_nan_count: int = 0,
    zero_variance_count: int = 0,
    duplicate_warning_count: int = 0,
    drift_warning_count: int = 0,
    manual_review_count: int = 0,
) -> Dict[str, Any]:
    """Create a dictionary manifest record enforcing non-signal and source-preservation invariants."""
    refs = source_phase_refs or [116, 117, 118, 119, 120, 121, 122]
    return {
        "manifest_id": manifest_id,
        "matrix_or_factor_name": matrix_or_factor_name,
        "source_phase_refs": ",".join(str(r) for r in refs),
        "feature_count": feature_count,
        "factor_family_count": factor_family_count,
        "missingness_warning_count": missingness_warning_count,
        "infinite_value_count": infinite_value_count,
        "all_nan_count": all_nan_count,
        "zero_variance_count": zero_variance_count,
        "duplicate_warning_count": duplicate_warning_count,
        "drift_warning_count": drift_warning_count,
        "manual_review_count": manual_review_count,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "source_preserved": True,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    }


def build_feature_quality_drift_manifest(
    profile: FeatureQualityDriftProfile | None = None,
    matrices: List[Dict[str, Any]] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for the feature quality drift manifest."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    if matrices is None:
        matrices = [
            create_feature_quality_drift_manifest(
                manifest_id="manifest_fx_technical_grid",
                matrix_or_factor_name="fx_technical_multi_window_grid",
                feature_count=24,
            ),
            create_feature_quality_drift_manifest(
                manifest_id="manifest_commodity_cross_asset_fusion",
                matrix_or_factor_name="commodity_macro_news_aligned_matrix",
                feature_count=32,
            ),
            create_feature_quality_drift_manifest(
                manifest_id="manifest_comprehensive_factor_pool",
                matrix_or_factor_name="comprehensive_10_family_factor_pool",
                feature_count=56,
            ),
        ]

    df = pd.DataFrame(matrices)
    summary = summarize_feature_quality_drift_manifest(df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return df, summary


def summarize_feature_quality_drift_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from manifest DataFrame."""
    if df.empty:
        return {
            "total_matrices": 0,
            "total_features": 0,
            "total_manual_reviews": 0,
            "all_source_preserved": True,
            "all_non_signal": True,
            "status": "diagnostic_pass",
        }

    total_m = len(df)
    total_feats = int(df["feature_count"].sum()) if "feature_count" in df.columns else 0
    total_reviews = int(df["manual_review_count"].sum()) if "manual_review_count" in df.columns else 0
    all_preserved = bool(df["source_preserved"].all()) if "source_preserved" in df.columns else True
    all_non_sig = bool(df["non_signal"].all()) if "non_signal" in df.columns else True

    return {
        "total_matrices": total_m,
        "total_features": total_feats,
        "total_manual_reviews": total_reviews,
        "all_source_preserved": all_preserved,
        "all_non_signal": all_non_sig,
        "status": "diagnostic_pass",
    }
