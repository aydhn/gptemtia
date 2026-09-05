"""Phase 124 Feature Store Catalog Reports."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_feature_registry import build_feature_store_feature_registry
from advanced_feature_store_integration.feature_store_factor_registry import build_feature_store_factor_registry
from advanced_feature_store_integration.feature_store_quality_scores import build_feature_store_quality_score_registry
from advanced_feature_store_integration.feature_store_drift_scores import build_feature_store_drift_score_registry
from advanced_feature_store_integration.feature_store_validation_status import build_feature_store_validation_status_registry


def build_feature_store_feature_catalog_report(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build comprehensive feature catalog report."""
    df, s = build_feature_store_feature_registry(profile)
    summary = {
        "catalog_type": "feature_catalog",
        "total_features": len(df),
        "source_phases": s.get("source_phases", []),
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def build_feature_store_factor_catalog_report(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build comprehensive factor catalog report."""
    df, s = build_feature_store_factor_registry(profile)
    summary = {
        "catalog_type": "factor_catalog",
        "total_factors": len(df),
        "factor_families": s.get("factor_families", []),
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def build_feature_store_quality_drift_catalog_report(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build combined quality and drift catalog report."""
    df_q, sq = build_feature_store_quality_score_registry(profile)
    df_d, sd = build_feature_store_drift_score_registry(profile)

    merged = pd.merge(df_q, df_d, on=["feature_name", "entity_id"], suffixes=("_quality", "_drift"), how="outer")
    summary = {
        "catalog_type": "quality_drift_catalog",
        "total_items": len(merged),
        "mean_quality_score": sq.get("mean_quality_score", 1.0),
        "mean_drift_score": sd.get("mean_drift_score", 0.0),
        "non_signal": True,
        "source_preserved": True,
    }
    return merged, summary


def build_feature_store_validation_catalog_report(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build validation catalog report."""
    df, s = build_feature_store_validation_status_registry(profile)
    summary = {
        "catalog_type": "validation_catalog",
        "total_validations": len(df),
        "pass_count": s.get("pass_count", 0),
        "review_required_count": s.get("review_required_count", 0),
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_store_catalog_report(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize catalog DataFrame."""
    return {
        "total_records": len(df) if not df.empty else 0,
        "non_signal": True,
        "source_preserved": True,
    }
