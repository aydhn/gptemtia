"""Phase 133 -> Phase 134 Handoff Report.

Hands off validation-aware, no-lookahead accepted, and metadata-only accepted regime assets
to Phase 134: Regime FeatureStore Integration.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)

HANDOFF_ITEMS = [
    {
        "item_id": "HANDOFF_01_FS_PREREQUISITES",
        "topic": "regime FeatureStore integration prerequisites",
        "requirement": "All Phase 126-132 regime catalogs and metadata contracts must be fully accepted without lookahead.",
        "status": "READY",
        "target_phase": 134,
    },
    {
        "item_id": "HANDOFF_02_NO_LOOKAHEAD_REGISTRY",
        "topic": "no-lookahead accepted registry requirements",
        "requirement": "Zero forward-looking joins, negative shifts, or lookahead return series permitted in FeatureStore views.",
        "status": "READY",
        "target_phase": 134,
    },
    {
        "item_id": "HANDOFF_03_METADATA_ONLY_NEWS",
        "topic": "metadata-only news accepted registry requirements",
        "requirement": "FeatureStore news entities must only contain metadata (tags, topics, IDs, timestamps); zero raw content.",
        "status": "READY",
        "target_phase": 134,
    },
    {
        "item_id": "HANDOFF_04_FORBIDDEN_COLUMN_METADATA",
        "topic": "forbidden column acceptance metadata",
        "requirement": "FeatureStore schemas must reject signal, buy, sell, target, label, prediction, and return columns.",
        "status": "READY",
        "target_phase": 134,
    },
    {
        "item_id": "HANDOFF_05_COMPONENT_METADATA",
        "topic": "component acceptance metadata",
        "requirement": "Matrix, candidate-state, pseudo-state, transition, cross-asset, and macro regime components accepted.",
        "status": "READY",
        "target_phase": 134,
    },
    {
        "item_id": "HANDOFF_06_VALIDATION_DEPENDENCIES",
        "topic": "validation dependency acceptance metadata",
        "requirement": "Point-in-time timestamp integrity and upstream Phase 121-132 validation gates satisfied.",
        "status": "READY",
        "target_phase": 134,
    },
    {
        "item_id": "HANDOFF_07_QUALITY_DEPENDENCIES",
        "topic": "quality dependency acceptance metadata",
        "requirement": "Quality drift, completeness, stationarity, and row-stochasticity thresholds verified.",
        "status": "READY",
        "target_phase": 134,
    },
    {
        "item_id": "HANDOFF_08_SOURCE_PRESERVATION",
        "topic": "source preservation requirements",
        "requirement": "FeatureStore storage must act as an immutable projection without altering raw DataLake source assets.",
        "status": "READY",
        "target_phase": 134,
    },
    {
        "item_id": "HANDOFF_09_MANUAL_REVIEW_BLOCKERS",
        "topic": "manual review blockers before Phase 134",
        "requirement": "Zero unresolved critical manual review blockers before FeatureStore registration.",
        "status": "READY",
        "target_phase": 134,
    },
    {
        "item_id": "HANDOFF_10_ACCEPTANCE_SCORE_STORAGE",
        "topic": "acceptance score storage requirements",
        "requirement": "Acceptance scores must be archived strictly as non-signal diagnostic metadata in FeatureStore.",
        "status": "READY",
        "target_phase": 134,
    },
    {
        "item_id": "HANDOFF_11_REGIME_MANIFEST_STORAGE",
        "topic": "regime manifest storage requirements",
        "requirement": "Phase 133 acceptance manifest must be indexed in FeatureStore catalog as proof of compliance.",
        "status": "READY",
        "target_phase": 134,
    },
    {
        "item_id": "HANDOFF_12_NON_SIGNAL_BOUNDARY",
        "topic": "clear boundary: Phase 134 stores regime metadata in FeatureStore, not trade signals",
        "requirement": "Reiterate that FeatureStore holds descriptive regime metadata, never execution orders or recommendations.",
        "status": "READY",
        "target_phase": 134,
    },
]


def build_phase_134_regime_featurestore_integration_handoff_report(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 134 Handoff."""
    p = profile or get_default_regime_validation_acceptance_profile()

    rows = []
    for item in HANDOFF_ITEMS:
        rows.append(
            {
                "item_id": item["item_id"],
                "topic": item["topic"],
                "requirement": item["requirement"],
                "status": item["status"],
                "target_phase": item["target_phase"],
                "source_phase": 133,
                "target_final_phase": 160,
                "profile_name": p.profile_name,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    ready_count = int((df["status"] == "READY").sum())
    summary = {
        "total_items": len(df),
        "ready_items": ready_count,
        "all_ready": ready_count == len(df),
        "handoff_status": "READY" if ready_count == len(df) else "PENDING",
        "source_phase": 133,
        "next_phase": 134,
        "target_final_phase": 160,
        "profile_name": p.profile_name,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_phase_134_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 134 handoff DataFrame."""
    total = len(df)
    ready = int((df["status"] == "READY").sum()) if "status" in df.columns else 0
    return {
        "total_items": total,
        "ready_items": ready,
        "all_ready": total == ready,
        "handoff_status": "READY" if total == ready else "PENDING",
    }
