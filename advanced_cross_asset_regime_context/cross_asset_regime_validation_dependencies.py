"""Phase 131: Cross-Asset Regime Validation Dependencies.

Defines formal validation dependencies connecting upstream validation gates
(Phase 121, 127, 128, 129, 130, metadata boundaries, and source preservation).
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

VALIDATION_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "val_dep_p121_no_lookahead",
        "dependency_name": "Phase 121 No-Lookahead Validation Gate",
        "source_phase": 121,
        "required_status": "PASSED",
        "is_blocking": True,
        "description": "Upstream feature validation ensuring zero negative shift and zero forward leakage.",
        "verified": True,
    },
    {
        "dependency_id": "val_dep_p127_regime_matrix",
        "dependency_name": "Phase 127 Regime Matrix Integrity Gate",
        "source_phase": 127,
        "required_status": "PASSED",
        "is_blocking": True,
        "description": "Dataset schema and candidate context non-signal verification.",
        "verified": True,
    },
    {
        "dependency_id": "val_dep_p128_candidate_state",
        "dependency_name": "Phase 128 Candidate State No-Lookahead Gate",
        "source_phase": 128,
        "required_status": "PASSED",
        "is_blocking": True,
        "description": "Candidate state sequence temporal order verification.",
        "verified": True,
    },
    {
        "dependency_id": "val_dep_p129_behavior_validation",
        "dependency_name": "Phase 129 Behavior Validation Gate",
        "source_phase": 129,
        "required_status": "PASSED",
        "is_blocking": True,
        "description": "Market behavior diagnostic quality gates verification.",
        "verified": True,
    },
    {
        "dependency_id": "val_dep_p130_transition_no_lookahead",
        "dependency_name": "Phase 130 Transition No-Lookahead Gate",
        "source_phase": 130,
        "required_status": "PASSED",
        "is_blocking": True,
        "description": "State transition continuity and strictly backward-looking sequence contracts.",
        "verified": True,
    },
    {
        "dependency_id": "val_dep_metadata_news_boundary",
        "dependency_name": "Metadata-Only News Boundary Gate",
        "source_phase": 111,
        "required_status": "PASSED",
        "is_blocking": True,
        "description": "Guaranteed absence of full article body, scraped content, or sentiment models.",
        "verified": True,
    },
    {
        "dependency_id": "val_dep_source_preservation",
        "dependency_name": "Source Preservation & Non-Destruction Gate",
        "source_phase": 131,
        "required_status": "PASSED",
        "is_blocking": True,
        "description": "Prohibition of in-place mutation, auto-imputation, and auto-feature-drop.",
        "verified": True,
    },
]


def build_cross_asset_regime_validation_dependency_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build validation dependency registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in VALIDATION_DEPENDENCIES:
        row = dict(item)
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        row["contains_target_or_prediction"] = False
        row["contains_trading_recommendation"] = False
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_cross_asset_validation_dependencies(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_validation_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize validation dependencies."""
    return {
        "total_dependencies": len(df),
        "all_verified": bool(df["verified"].all()) if not df.empty else True,
        "blocking_count": int(df["is_blocking"].sum()) if not df.empty else 0,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
    }
