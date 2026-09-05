"""Phase 127: Regime Matrix Integrity Manifest.

Creates and manages the immutable governance manifest record for Phase 127.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)
from advanced_regime_matrix.regime_matrix_models import RegimeMatrixIntegrityManifest


def create_regime_matrix_integrity_manifest(
    matrix_name: str = "regime_feature_matrix_master",
    feature_contract_count: int = 7,
    dataset_contract_count: int = 5,
    input_feature_count: int = 11,
    dependency_count: int = 17,
    manual_review_required: bool = True,
) -> RegimeMatrixIntegrityManifest:
    """Create a validated RegimeMatrixIntegrityManifest instance."""
    return RegimeMatrixIntegrityManifest(
        manifest_name=matrix_name,
        current_phase=127,
        target_final_phase=160,
        next_phase=128,
        feature_contract_count=feature_contract_count,
        dataset_contract_count=dataset_contract_count,
        input_feature_count=input_feature_count,
        dependency_count=dependency_count,
        manifest_status="MANIFEST_VALID",
        non_signal=True,
        source_preserved=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        contains_full_article_text=False,
        model_training_executed=False,
        clustering_executed=False,
        unsupervised_execution=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        manual_review_required=manual_review_required,
    )


def build_regime_matrix_integrity_manifest(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame and summary dictionary for Phase 127 manifest."""
    manifest = create_regime_matrix_integrity_manifest()

    row = {
        "manifest_name": manifest.manifest_name,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "feature_contract_count": manifest.feature_contract_count,
        "dataset_contract_count": manifest.dataset_contract_count,
        "input_feature_count": manifest.input_feature_count,
        "dependency_count": manifest.dependency_count,
        "manifest_status": manifest.manifest_status,
        "non_signal": manifest.non_signal,
        "source_preserved": manifest.source_preserved,
        "official_approval": manifest.official_approval,
        "production_ready": manifest.production_ready,
        "broker_ready": manifest.broker_ready,
        "contains_target_or_prediction": manifest.contains_target_or_prediction,
        "contains_trading_recommendation": manifest.contains_trading_recommendation,
        "contains_full_article_text": manifest.contains_full_article_text,
        "model_training_executed": manifest.model_training_executed,
        "clustering_executed": manifest.clustering_executed,
        "unsupervised_execution": manifest.unsupervised_execution,
        "destructive_action_allowed": manifest.destructive_action_allowed,
        "auto_fix_allowed": manifest.auto_fix_allowed,
        "auto_drop_allowed": manifest.auto_drop_allowed,
        "manual_review_required": manifest.manual_review_required,
    }

    df = pd.DataFrame([row])
    summary = summarize_regime_matrix_integrity_manifest(df)
    return df, summary


def summarize_regime_matrix_integrity_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the integrity manifest DataFrame."""
    if df.empty:
        return {"manifest_status": "EMPTY"}

    row = df.iloc[0]
    return {
        "manifest_name": str(row["manifest_name"]),
        "current_phase": int(row["current_phase"]),
        "next_phase": int(row["next_phase"]),
        "target_final_phase": int(row["target_final_phase"]),
        "manifest_status": str(row["manifest_status"]),
        "non_signal": bool(row["non_signal"]),
        "source_preserved": bool(row["source_preserved"]),
        "official_approval": bool(row["official_approval"]),
        "production_ready": bool(row["production_ready"]),
        "broker_ready": bool(row["broker_ready"]),
        "model_training_executed": bool(row["model_training_executed"]),
        "clustering_executed": bool(row["clustering_executed"]),
        "unsupervised_execution": bool(row["unsupervised_execution"]),
        "feature_contract_count": int(row["feature_contract_count"]),
        "dataset_contract_count": int(row["dataset_contract_count"]),
        "input_feature_count": int(row["input_feature_count"]),
        "dependency_count": int(row["dependency_count"]),
    }
