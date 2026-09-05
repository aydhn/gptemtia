"""Phase 126: Phase 127 Regime Feature Matrix Handoff.

Defines the formal prerequisite handoff specification for Phase 127
(Regime Feature Matrix and State Dataset Contracts).
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

HANDOFF_ITEMS: List[Dict[str, Any]] = [
    {
        "item_id": "handoff_01_matrix_prereq",
        "title": "Regime Feature Matrix Prerequisites",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Phase 126 taxonomy and family definitions ready for multidimensional feature matrix structuring",
        "non_signal": True,
    },
    {
        "item_id": "handoff_02_state_dataset_contracts",
        "title": "Regime State Dataset Contract Prerequisites",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Standardized schema with mandatory regime_state_ prefix without supervised ML target labels",
        "non_signal": True,
    },
    {
        "item_id": "handoff_03_validated_inputs",
        "title": "Validated Feature and Factor Inputs",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Inputs from Phase 117-122 fully mapped and validated for matrix integration",
        "non_signal": True,
    },
    {
        "item_id": "handoff_04_feature_store_metadata",
        "title": "Feature Store Metadata Requirements",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Central Feature Store catalog and query contracts established for point-in-time reads",
        "non_signal": True,
    },
    {
        "item_id": "handoff_05_no_lookahead_matrix_guard",
        "title": "No-Lookahead Constraints for Regime Datasets",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Strict asof join semantics ensuring matrix features cannot peek forward into future bars",
        "non_signal": True,
    },
    {
        "item_id": "handoff_06_non_signal_mandate",
        "title": "Non-Signal Regime State Requirements",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Matrix rows represent environmental context; BUY/SELL and trade signals remain strictly prohibited",
        "non_signal": True,
    },
    {
        "item_id": "handoff_07_quality_drift_prereq",
        "title": "Quality and Drift Prerequisites",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Missingness thresholds (<5%) and drift bounds (<0.25 PSI) enforced prior to matrix inclusion",
        "non_signal": True,
    },
    {
        "item_id": "handoff_08_macro_event_news_metadata",
        "title": "Macro, Event, and News Metadata-Only Requirements",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Environmental context relies strictly on numerical metadata, lag-aware dates, and topic tags",
        "non_signal": True,
    },
    {
        "item_id": "handoff_09_cross_asset_context",
        "title": "Cross-Asset Context Requirements",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Multi-asset time-series synchronization across FX and commodities ready for joint matrix columns",
        "non_signal": True,
    },
    {
        "item_id": "handoff_10_namespace_schema",
        "title": "Regime Namespace and Schema Requirements",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Canonical lowercase snake_case naming standard with forbidden word filtering in place",
        "non_signal": True,
    },
    {
        "item_id": "handoff_11_manual_review_blockers",
        "title": "Manual Review Blockers Before Matrix Construction",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Zero active blocking review queue items required before Phase 127 matrix generation begins",
        "non_signal": True,
    },
    {
        "item_id": "handoff_12_no_model_training_invariant",
        "title": "Prohibition of Model Training in Phase 127",
        "source_phase": 126,
        "next_phase": 127,
        "status": "READY",
        "description": "Phase 127 remains a feature matrix and dataset contract phase; model training begins in later phases",
        "non_signal": True,
    },
]


def build_phase_127_regime_feature_matrix_handoff_report(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 127 handoff report."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(HANDOFF_ITEMS)
    ready_count = len(df[df["status"] == "READY"])

    summary = {
        "active_profile": active_profile.profile_name,
        "source_phase": 126,
        "next_phase": 127,
        "target_final_phase": active_profile.target_final_phase,
        "total_handoff_items": len(df),
        "ready_items": ready_count,
        "handoff_status": "READY" if ready_count == len(df) else "IN_PROGRESS",
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_phase_127_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 127 handoff DataFrame."""
    return {
        "total_items": len(df),
        "all_ready": bool((df["status"] == "READY").all()) if "status" in df.columns else False,
        "non_signal": True,
    }
