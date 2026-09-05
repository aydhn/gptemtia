"""Phase 125: Phase 116-125 Feature/Factor Engine Acceptance Manifest.

Produces the immutable block acceptance manifest finalizing the Phase 116-125 block
and enabling handoff to Phase 126.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_models import (
    Phase116125AcceptanceManifest,
)
from advanced_feature_factor_acceptance.feature_engine_block_acceptance_scoring import (
    build_feature_engine_block_acceptance_score_report,
)


def create_phase_116_125_acceptance_manifest(
    block_name: str = "advanced_feature_factor_engine_block",
    phase_start: int = 116,
    phase_end: int = 125,
    module_count: int = 10,
    gate_count: int = 16,
    manual_review_count: int = 0,
    acceptance_score: float = 1.0,
    manual_review_required: bool = False,
) -> Phase116125AcceptanceManifest:
    """Factory creating a typed Phase 116-125 Acceptance Manifest."""
    return Phase116125AcceptanceManifest(
        block_name=block_name,
        phase_start=phase_start,
        phase_end=phase_end,
        target_final_phase=160,
        next_phase=126,
        module_count=module_count,
        gate_count=gate_count,
        manual_review_count=manual_review_count,
        acceptance_score=acceptance_score,
        manual_review_required=manual_review_required,
        non_signal=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        source_preserved=True,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        contains_full_article_text=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
    )


def build_phase_116_125_acceptance_manifest(
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the acceptance manifest DataFrame and summary."""
    active_profile = profile or get_default_feature_factor_acceptance_profile()
    _, score_summary = build_feature_engine_block_acceptance_score_report(active_profile)

    overall_score = score_summary.get("overall_score", 1.0)
    failed_gates = score_summary.get("failed_gates", 0)

    manifest = create_phase_116_125_acceptance_manifest(
        block_name="advanced_feature_factor_engine_block",
        phase_start=116,
        phase_end=125,
        module_count=10,
        gate_count=score_summary.get("total_gates", 16),
        manual_review_count=0,
        acceptance_score=overall_score,
        manual_review_required=failed_gates > 0,
    )
    df = pd.DataFrame([manifest.__dict__])

    summary = {
        "block_name": manifest.block_name,
        "phase_start": manifest.phase_start,
        "phase_end": manifest.phase_end,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "acceptance_score": manifest.acceptance_score,
        "non_signal": manifest.non_signal,
        "official_approval": manifest.official_approval,
        "production_ready": manifest.production_ready,
        "broker_ready": manifest.broker_ready,
        "source_preserved": manifest.source_preserved,
    }
    return df, summary


def summarize_phase_116_125_acceptance_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the manifest DataFrame."""
    if df.empty:
        return {"manifest_status": "EMPTY", "non_signal": True}
    row = df.iloc[0]
    return {
        "block_name": str(row.get("block_name", "unknown")),
        "acceptance_score": float(row.get("acceptance_score", 0.0)),
        "non_signal": bool(row.get("non_signal", True)),
        "official_approval": bool(row.get("official_approval", False)),
    }
