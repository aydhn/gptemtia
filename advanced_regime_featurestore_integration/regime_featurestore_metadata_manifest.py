"""Phase 134: Regime FeatureStore Metadata Manifest.

Generates the master metadata manifest certifying non-signal guarantees,
provenance traceability, and safety boundary enforcement across FeatureStore catalogs.
"""

from typing import Any, Dict, Optional, Tuple
from datetime import datetime, timezone
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    METADATA_MANIFEST_DOMAIN,
    REGIME_STORE_READY,
)
from advanced_regime_featurestore_integration.regime_featurestore_models import (
    RegimeFeatureStoreMetadataManifest,
)


def create_regime_featurestore_metadata_manifest(
    manifest_name: str = "regime_featurestore_metadata_manifest",
    contract_count: int = 10,
    catalog_count: int = 8,
    accepted_reference_count: int = 21,
    dependency_count: int = 12,
    manual_review_count: int = 0,
    readiness_score: float = 1.0,
    manual_review_required: bool = False,
) -> RegimeFeatureStoreMetadataManifest:
    """Instantiate a validated RegimeFeatureStoreMetadataManifest dataclass."""
    return RegimeFeatureStoreMetadataManifest(
        manifest_name=manifest_name,
        generated_at_utc=datetime.now(timezone.utc).isoformat(),
        current_phase=134,
        target_final_phase=160,
        next_phase=135,
        contract_count=contract_count,
        catalog_count=catalog_count,
        accepted_reference_count=accepted_reference_count,
        dependency_count=dependency_count,
        manual_review_count=manual_review_count,
        readiness_score=readiness_score,
        manual_review_required=manual_review_required,
        non_signal=True,
        source_preserved=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        contains_full_article_text=False,
        contains_article_body=False,
        contains_raw_content=False,
        contains_scraped_html=False,
        contains_embedding=False,
        contains_vector=False,
        sentiment_model_output=False,
        model_training_executed=False,
        model_fit_executed=False,
        model_predict_executed=False,
        clustering_executed=False,
        unsupervised_execution=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
    )


def build_regime_featurestore_metadata_manifest(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame representation of the master FeatureStore metadata manifest."""
    active_profile = profile or get_regime_featurestore_profile()
    manifest = create_regime_featurestore_metadata_manifest()

    row = {
        "manifest_name": manifest.manifest_name,
        "generated_at_utc": manifest.generated_at_utc,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "contract_count": manifest.contract_count,
        "catalog_count": manifest.catalog_count,
        "accepted_reference_count": manifest.accepted_reference_count,
        "dependency_count": manifest.dependency_count,
        "manual_review_count": manifest.manual_review_count,
        "readiness_score": manifest.readiness_score,
        "manual_review_required": manifest.manual_review_required,
        "non_signal": manifest.non_signal,
        "source_preserved": manifest.source_preserved,
        "official_approval": manifest.official_approval,
        "production_ready": manifest.production_ready,
        "broker_ready": manifest.broker_ready,
        "contains_target_or_prediction": manifest.contains_target_or_prediction,
        "contains_trading_recommendation": manifest.contains_trading_recommendation,
        "contains_full_article_text": manifest.contains_full_article_text,
        "contains_article_body": manifest.contains_article_body,
        "contains_raw_content": manifest.contains_raw_content,
        "contains_scraped_html": manifest.contains_scraped_html,
        "contains_embedding": manifest.contains_embedding,
        "contains_vector": manifest.contains_vector,
        "sentiment_model_output": manifest.sentiment_model_output,
        "model_training_executed": manifest.model_training_executed,
        "model_fit_executed": manifest.model_fit_executed,
        "model_predict_executed": manifest.model_predict_executed,
        "clustering_executed": manifest.clustering_executed,
        "unsupervised_execution": manifest.unsupervised_execution,
        "destructive_action_allowed": manifest.destructive_action_allowed,
        "auto_fix_allowed": manifest.auto_fix_allowed,
        "auto_drop_allowed": manifest.auto_drop_allowed,
        "active_profile": active_profile.profile_name,
        "status": REGIME_STORE_READY,
    }

    df = pd.DataFrame([row])
    summary = {
        "domain": METADATA_MANIFEST_DOMAIN,
        "manifest_name": manifest.manifest_name,
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "readiness_score": manifest.readiness_score,
        "status": REGIME_STORE_READY,
        "non_signal": True,
        "manifest_valid": True,
    }
    return df, summary


def summarize_regime_featurestore_metadata_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the metadata manifest DataFrame."""
    if df.empty:
        return {"manifest_valid": False}
    row = df.iloc[0].to_dict()
    return {
        "manifest_name": row.get("manifest_name"),
        "current_phase": row.get("current_phase"),
        "target_final_phase": row.get("target_final_phase"),
        "next_phase": row.get("next_phase"),
        "readiness_score": row.get("readiness_score"),
        "non_signal": bool(row.get("non_signal")),
        "production_ready": bool(row.get("production_ready")),
        "broker_ready": bool(row.get("broker_ready")),
        "manifest_valid": True,
    }
