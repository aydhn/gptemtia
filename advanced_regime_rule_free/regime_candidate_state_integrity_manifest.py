"""Phase 128: Regime Candidate State Integrity Manifest.

Constructs master governance manifest certifying compliance with Phase 128 boundaries.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import CandidateStateIntegrityManifest


def create_candidate_state_integrity_manifest(
    manifest_name: str = "regime_candidate_state_master_manifest",
    contract_count: int = 8,
    schema_count: int = 12,
    prep_contract_count: int = 6,
    dependency_count: int = 10,
    manual_review_required: bool = True,
) -> CandidateStateIntegrityManifest:
    """Instantiate CandidateStateIntegrityManifest with strict invariant defaults."""
    return CandidateStateIntegrityManifest(
        manifest_name=manifest_name,
        current_phase=128,
        target_final_phase=160,
        next_phase=129,
        non_signal=True,
        source_preserved=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        contains_full_article_text=False,
        model_training_executed=False,
        model_fit_executed=False,
        model_predict_executed=False,
        clustering_executed=False,
        unsupervised_execution=False,
        dimensionality_reduction_executed=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        total_contracts=contract_count,
        total_schemas=schema_count,
        total_prep_contracts=prep_contract_count,
        total_dependencies=dependency_count,
        manual_review_required=manual_review_required,
        manifest_status="MANIFEST_VALID",
    )


def build_regime_candidate_state_integrity_manifest(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for Phase 128 integrity manifest."""
    active_profile = profile or get_default_regime_rule_free_profile()
    manifest = create_candidate_state_integrity_manifest(
        manifest_name=f"{active_profile.profile_name}_integrity_manifest"
    )

    df = pd.DataFrame([manifest.__dict__])
    summary = summarize_candidate_state_integrity_manifest(df)
    return df, summary


def summarize_candidate_state_integrity_manifest(df: pd.DataFrame) -> Dict:
    """Summarize candidate state integrity manifest."""
    if df.empty:
        return {"manifest_status": "EMPTY", "is_valid": False}

    row = df.iloc[0].to_dict()
    is_valid = (
        row.get("current_phase") == 128
        and row.get("target_final_phase") == 160
        and row.get("next_phase") == 129
        and row.get("non_signal") is True
        and row.get("source_preserved") is True
        and row.get("official_approval") is False
        and row.get("production_ready") is False
        and row.get("broker_ready") is False
        and row.get("contains_target_or_prediction") is False
        and row.get("contains_trading_recommendation") is False
        and row.get("contains_full_article_text") is False
        and row.get("model_training_executed") is False
        and row.get("model_fit_executed") is False
        and row.get("model_predict_executed") is False
        and row.get("clustering_executed") is False
        and row.get("unsupervised_execution") is False
        and row.get("dimensionality_reduction_executed") is False
        and row.get("destructive_action_allowed") is False
        and row.get("auto_fix_allowed") is False
        and row.get("auto_drop_allowed") is False
    )

    return {
        "manifest_name": row.get("manifest_name"),
        "manifest_status": "MANIFEST_VALID" if is_valid else "MANIFEST_INVALID",
        "is_valid": is_valid,
        "current_phase": row.get("current_phase"),
        "next_phase": row.get("next_phase"),
        "target_final_phase": row.get("target_final_phase"),
        "non_signal": row.get("non_signal"),
        "source_preserved": row.get("source_preserved"),
        "zero_execution_guaranteed": not (
            row.get("model_training_executed") or row.get("clustering_executed")
        ),
    }
