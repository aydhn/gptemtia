"""Phase 124 Feature Store Metadata Manifest."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_integration_models import (
    FeatureStoreMetadataManifest,
)


def create_feature_store_metadata_manifest(
    store_name: str = "central_feature_store_v124",
    entity_count: int = 7,
    feature_count: int = 9,
    factor_count: int = 6,
    validation_status_count: int = 5,
    quality_score_count: int = 6,
    drift_score_count: int = 6,
    manual_review_blocker_count: int = 4,
    manual_review_required: bool = True,
) -> FeatureStoreMetadataManifest:
    """Create a structured FeatureStoreMetadataManifest instance."""
    return FeatureStoreMetadataManifest(
        store_name=store_name,
        entity_count=entity_count,
        feature_count=feature_count,
        factor_count=factor_count,
        validation_status_count=validation_status_count,
        quality_score_count=quality_score_count,
        drift_score_count=drift_score_count,
        manual_review_blocker_count=manual_review_blocker_count,
        source_phase_refs=[116, 117, 118, 119, 120, 121, 122, 123],
        non_signal=True,
        source_preserved=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        contains_full_article_text=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        manual_review_required=manual_review_required,
    )


def build_feature_store_metadata_manifest(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for feature store metadata manifest."""
    manifest_item = create_feature_store_metadata_manifest()
    record = {
        "store_name": manifest_item.store_name,
        "entity_count": manifest_item.entity_count,
        "feature_count": manifest_item.feature_count,
        "factor_count": manifest_item.factor_count,
        "validation_status_count": manifest_item.validation_status_count,
        "quality_score_count": manifest_item.quality_score_count,
        "drift_score_count": manifest_item.drift_score_count,
        "manual_review_blocker_count": manifest_item.manual_review_blocker_count,
        "source_phase_refs": ",".join(str(x) for x in manifest_item.source_phase_refs),
        "non_signal": manifest_item.non_signal,
        "source_preserved": manifest_item.source_preserved,
        "official_approval": manifest_item.official_approval,
        "production_ready": manifest_item.production_ready,
        "broker_ready": manifest_item.broker_ready,
        "contains_target_or_prediction": manifest_item.contains_target_or_prediction,
        "contains_trading_recommendation": manifest_item.contains_trading_recommendation,
        "contains_full_article_text": manifest_item.contains_full_article_text,
        "auto_fix_allowed": manifest_item.auto_fix_allowed,
        "auto_drop_allowed": manifest_item.auto_drop_allowed,
        "manual_review_required": manifest_item.manual_review_required,
    }

    df = pd.DataFrame([record])
    summary = {
        "store_name": manifest_item.store_name,
        "total_features": manifest_item.feature_count,
        "total_factors": manifest_item.factor_count,
        "total_entities": manifest_item.entity_count,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
        "destructive_action_allowed": False,
    }
    return df, summary


def summarize_feature_store_metadata_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize metadata manifest DataFrame."""
    if df.empty:
        return {"store_name": "empty", "non_signal": True, "source_preserved": True}
    row = df.iloc[0].to_dict()
    return {
        "store_name": row.get("store_name", "unknown"),
        "total_features": row.get("feature_count", 0),
        "total_factors": row.get("factor_count", 0),
        "total_entities": row.get("entity_count", 0),
        "all_non_signal": bool(row.get("non_signal", True)),
        "all_source_preserved": bool(row.get("source_preserved", True)),
        "official_approval": bool(row.get("official_approval", False)),
        "production_ready": bool(row.get("production_ready", False)),
        "broker_ready": bool(row.get("broker_ready", False)),
    }
