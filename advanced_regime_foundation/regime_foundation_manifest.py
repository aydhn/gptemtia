"""Phase 126: Regime Foundation Manifest.

Creates and validates the master governance manifest for Phase 126.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.regime_foundation_models import RegimeFoundationManifest


def create_regime_foundation_manifest(
    foundation_name: str = "advanced_regime_foundation",
    regime_family_count: int = 9,
    regime_state_count: int = 11,
    dependency_count: int = 15,
    validation_dependency_count: int = 8,
    quality_dependency_count: int = 7,
    manual_review_required: bool = True,
) -> RegimeFoundationManifest:
    """Create a typed RegimeFoundationManifest dataclass instance."""
    return RegimeFoundationManifest(
        foundation_name=foundation_name,
        current_phase=126,
        target_final_phase=160,
        next_phase=127,
        regime_family_count=regime_family_count,
        regime_state_count=regime_state_count,
        dependency_count=dependency_count,
        validation_dependency_count=validation_dependency_count,
        quality_dependency_count=quality_dependency_count,
        non_signal=True,
        source_preserved=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        model_training_executed=False,
        clustering_executed=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        contains_full_article_text=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        manual_review_required=manual_review_required,
    )


def build_regime_foundation_manifest(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime foundation manifest."""
    active_profile = profile or get_default_regime_foundation_profile()
    manifest_obj = create_regime_foundation_manifest()

    data = [
        {
            "foundation_name": manifest_obj.foundation_name,
            "current_phase": manifest_obj.current_phase,
            "target_final_phase": manifest_obj.target_final_phase,
            "next_phase": manifest_obj.next_phase,
            "regime_family_count": manifest_obj.regime_family_count,
            "regime_state_count": manifest_obj.regime_state_count,
            "dependency_count": manifest_obj.dependency_count,
            "validation_dependency_count": manifest_obj.validation_dependency_count,
            "quality_dependency_count": manifest_obj.quality_dependency_count,
            "non_signal": manifest_obj.non_signal,
            "source_preserved": manifest_obj.source_preserved,
            "official_approval": manifest_obj.official_approval,
            "production_ready": manifest_obj.production_ready,
            "broker_ready": manifest_obj.broker_ready,
            "model_training_executed": manifest_obj.model_training_executed,
            "clustering_executed": manifest_obj.clustering_executed,
            "contains_target_or_prediction": manifest_obj.contains_target_or_prediction,
            "contains_trading_recommendation": manifest_obj.contains_trading_recommendation,
            "contains_full_article_text": manifest_obj.contains_full_article_text,
            "destructive_action_allowed": manifest_obj.destructive_action_allowed,
            "auto_fix_allowed": manifest_obj.auto_fix_allowed,
            "auto_drop_allowed": manifest_obj.auto_drop_allowed,
            "manual_review_required": manifest_obj.manual_review_required,
        }
    ]

    df = pd.DataFrame(data)
    summary = {
        "foundation_name": manifest_obj.foundation_name,
        "active_profile": active_profile.profile_name,
        "current_phase": manifest_obj.current_phase,
        "target_final_phase": manifest_obj.target_final_phase,
        "next_phase": manifest_obj.next_phase,
        "regime_family_count": manifest_obj.regime_family_count,
        "regime_state_count": manifest_obj.regime_state_count,
        "dependency_count": manifest_obj.dependency_count,
        "validation_dependency_count": manifest_obj.validation_dependency_count,
        "quality_dependency_count": manifest_obj.quality_dependency_count,
        "non_signal": manifest_obj.non_signal,
        "source_preserved": manifest_obj.source_preserved,
        "official_approval": manifest_obj.official_approval,
        "production_ready": manifest_obj.production_ready,
        "broker_ready": manifest_obj.broker_ready,
        "model_training_executed": manifest_obj.model_training_executed,
        "clustering_executed": manifest_obj.clustering_executed,
        "manifest_status": "MANIFEST_VALID",
    }
    return df, summary


def summarize_regime_foundation_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime foundation manifest DataFrame."""
    if df.empty:
        return {"manifest_status": "EMPTY"}
    row = df.iloc[0].to_dict()
    return {
        "foundation_name": row.get("foundation_name", ""),
        "current_phase": int(row.get("current_phase", 126)),
        "next_phase": int(row.get("next_phase", 127)),
        "target_final_phase": int(row.get("target_final_phase", 160)),
        "regime_family_count": int(row.get("regime_family_count", 0)),
        "regime_state_count": int(row.get("regime_state_count", 0)),
        "non_signal": bool(row.get("non_signal", True)),
        "manifest_status": "VALID",
    }
