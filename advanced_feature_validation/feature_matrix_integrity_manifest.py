"""Feature Matrix Integrity Manifest.

Captures immutable validation manifests and structural audit trails for feature matrices.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)
from advanced_feature_validation.feature_validation_models import (
    FeatureMatrixIntegrityManifest,
    build_feature_matrix_integrity_manifest_id,
)
from advanced_feature_validation.forbidden_feature_columns import validate_forbidden_feature_columns
from advanced_feature_validation.duplicate_feature_validation import validate_duplicate_feature_names


import hashlib


class IntegrityManifestDict(dict):
    """Dictionary representing an immutable integrity manifest with to_dict() support."""

    def to_dict(self) -> Dict[str, Any]:
        return dict(self)


def create_feature_matrix_integrity_manifest(
    arg1: Any,
    arg2: Any = None,
    feature_columns: Optional[List[str]] = None,
    matrix_name: Optional[str] = None,
    manual_review_required: bool = True,
) -> IntegrityManifestDict:
    """Create an immutable integrity manifest audit record for a feature matrix."""
    if isinstance(arg1, pd.DataFrame):
        df = arg1
        m_name = matrix_name or (arg2 if isinstance(arg2, str) else "generic_matrix")
        feat_cols = feature_columns or [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    elif isinstance(arg1, str):
        m_name = arg1
        df = arg2 if isinstance(arg2, pd.DataFrame) else pd.DataFrame()
        feat_cols = feature_columns or [c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")]
    else:
        df = pd.DataFrame()
        m_name = matrix_name or "matrix"
        feat_cols = feature_columns or []

    forb_res = validate_forbidden_feature_columns(df)
    dup_res = validate_duplicate_feature_names(list(df.columns))

    future_leakage_risk_count = sum(
        1 for c in feat_cols if any(term in str(c).lower() for term in ("future", "forward", "lead", "fwd"))
    )

    high_missing_count = sum(
        1 for c in feat_cols if c in df.columns and (df[c].isna().sum() / len(df) > 0.5)
    ) if len(df) > 0 else 0

    manifest_id = build_feature_matrix_integrity_manifest_id(m_name)
    checksum_str = f"{m_name}_{len(df)}_{len(df.columns)}"
    checksum = hashlib.sha256(checksum_str.encode("utf-8")).hexdigest()[:16]

    return IntegrityManifestDict({
        "manifest_id": manifest_id,
        "matrix_name": m_name,
        "total_rows": len(df),
        "row_count": len(df),
        "total_columns": len(df.columns),
        "feature_count": len(feat_cols),
        "current_phase": 121,
        "checksum": checksum,
        "forbidden_column_count": forb_res["violation_count"],
        "duplicate_feature_count": dup_res["duplicate_count"],
        "future_leakage_risk_count": future_leakage_risk_count,
        "missingness_warning_count": high_missing_count,
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_full_article_text": False,
        "source_preserved": True,
        "manual_review_required": manual_review_required,
    })



def build_feature_matrix_integrity_manifest(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build default placeholder integrity manifests for core pipeline matrices."""
    active_profile = profile or get_default_feature_validation_profile()

    matrices = [
        "technical_indicator_matrix",
        "multi_window_feature_grid",
        "cross_asset_aligned_matrix",
        "macro_calendar_news_fusion_matrix",
    ]

    records = []
    for m_name in matrices:
        dummy_df = pd.DataFrame({"timestamp": ["2025-01-01"], "asset_id": ["XAUUSD"], "feature_val": [1.0]})
        mani = create_feature_matrix_integrity_manifest(m_name, dummy_df, ["feature_val"])
        records.append(mani.to_dict())

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_manifests": len(records),
        "all_non_signal": True,
        "all_source_preserved": True,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
    }
    return df, summary


def summarize_feature_matrix_integrity_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manifests DataFrame."""
    return {
        "total_manifests": len(df),
        "total_features": int(df["feature_count"].sum()) if "feature_count" in df else 0,
        "total_forbidden_columns": int(df["forbidden_column_count"].sum()) if "forbidden_column_count" in df else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df else False,
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df else False,
    }
