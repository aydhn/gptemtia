"""Phase 127: Regime Feature Matrix Profile Registry.

Builds and audits operational profile records for Phase 127.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    REGIME_MATRIX_PROFILES,
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)


def build_regime_matrix_profile_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the operational profile registry for Phase 127."""
    active_profile = profile or get_default_regime_matrix_profile()

    rows = []
    for p_name, p in REGIME_MATRIX_PROFILES.items():
        rows.append(
            {
                "profile_name": p.profile_name,
                "description": p.description,
                "current_phase": p.current_phase,
                "target_final_phase": p.target_final_phase,
                "next_phase": p.next_phase,
                "dry_run_default": p.dry_run_default,
                "local_only": p.local_only,
                "non_production": p.non_production,
                "research_only": p.research_only,
                "min_readiness_score": p.min_readiness_score,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
                "model_training_executed": False,
                "clustering_executed": False,
                "unsupervised_execution": False,
                "destructive_action_allowed": False,
                "auto_fix_allowed": False,
                "auto_drop_allowed": False,
                "is_active": p.profile_name == active_profile.profile_name,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_profiles": len(df),
        "current_phase": active_profile.current_phase,
        "next_phase": active_profile.next_phase,
        "target_final_phase": active_profile.target_final_phase,
        "all_non_signal": bool(df["non_signal"].all()),
        "all_source_preserved": bool(df["source_preserved"].all()),
        "official_approval_guarantee": False,
        "production_ready_guarantee": False,
        "broker_ready_guarantee": False,
    }
    return df, summary
