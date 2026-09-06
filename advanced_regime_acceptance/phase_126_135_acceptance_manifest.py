"""Phase 135: Phase 126-135 Regime Block Acceptance Manifest.

Defines and produces the canonical acceptance manifest for the entire
Phase 126-135 Regime Classification and Market Behavior block.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    PHASE_126_135_MANIFEST_DOMAIN,
)
from advanced_regime_acceptance.regime_acceptance_models import (
    Phase126135AcceptanceManifest,
)


def create_phase_126_135_acceptance_manifest(
    block_name: str = "Regime Classification and Market Behavior Block",
    phase_start: int = 126,
    phase_end: int = 135,
    module_count: int = 10,
    gate_count: int = 17,
    manual_review_count: int = 1,
    acceptance_score: float = 1.0,
    manual_review_required: bool = True,
) -> Phase126135AcceptanceManifest:
    """Instantiate a Phase126135AcceptanceManifest with strict governance constraints."""
    return Phase126135AcceptanceManifest(
        block_name=block_name,
        phase_start=phase_start,
        phase_end=phase_end,
        target_final_phase=160,
        next_phase=136,
        module_count=module_count,
        gate_count=gate_count,
        manual_review_count=manual_review_count,
        acceptance_score=acceptance_score,
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


def build_phase_126_135_acceptance_manifest(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Phase 126-135 acceptance manifest."""
    active = profile or get_regime_acceptance_profile()
    manifest_obj = create_phase_126_135_acceptance_manifest(
        block_name="Regime Classification and Market Behavior Block",
        phase_start=126,
        phase_end=135,
        module_count=10,
        gate_count=17,
        manual_review_count=1,
        acceptance_score=1.0,
        manual_review_required=True,
    )
    df = pd.DataFrame([manifest_obj.__dict__])
    summary: Dict[str, Any] = {
        "domain": PHASE_126_135_MANIFEST_DOMAIN,
        "active_profile": active.profile_name,
        "block_name": manifest_obj.block_name,
        "phase_start": manifest_obj.phase_start,
        "phase_end": manifest_obj.phase_end,
        "target_final_phase": manifest_obj.target_final_phase,
        "next_phase": manifest_obj.next_phase,
        "module_count": manifest_obj.module_count,
        "gate_count": manifest_obj.gate_count,
        "acceptance_score": manifest_obj.acceptance_score,
        "non_signal": manifest_obj.non_signal,
        "source_preserved": manifest_obj.source_preserved,
        "official_approval": manifest_obj.official_approval,
        "production_ready": manifest_obj.production_ready,
        "broker_ready": manifest_obj.broker_ready,
        "status": "READY",
    }
    return df, summary


def summarize_phase_126_135_acceptance_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize acceptance manifest DataFrame."""
    if df.empty:
        return {"manifest_valid": False, "non_signal": True}
    row = df.iloc[0]
    return {
        "block_name": str(row.get("block_name", "")),
        "acceptance_score": float(row.get("acceptance_score", 0.0)),
        "non_signal": bool(row.get("non_signal", True)),
        "official_approval": bool(row.get("official_approval", False)),
        "production_ready": bool(row.get("production_ready", False)),
        "broker_ready": bool(row.get("broker_ready", False)),
        "manifest_valid": True,
    }
