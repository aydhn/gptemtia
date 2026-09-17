# -*- coding: utf-8 -*-
"""Phase 143: Explainability Lineage."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_explainability_lineage_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of explainability lineage records."""
    prof = profile or get_explainability_profile()

    lineage_items = [
        ("lineage_candidate_models", "phase_138_baseline_models", "phase_143_explainability", "models_to_attribution"),
        ("lineage_ensembles", "phase_140_ensemble_contracts", "phase_143_explainability", "ensembles_to_attribution"),
        ("lineage_datasets", "phase_137_dataset_contracts", "phase_143_explainability", "datasets_to_attribution"),
        ("lineage_drift_monitoring", "phase_142_drift_contracts", "phase_143_explainability", "drift_to_attribution"),
        ("lineage_calibration", "phase_141_calibration_contracts", "phase_143_explainability", "calibration_to_attribution"),
        ("lineage_phase_144_handoff", "phase_143_explainability", "phase_144_governance_model_cards", "explainability_to_governance"),
    ]

    rows: List[Dict[str, Any]] = []
    for lid, src, tgt, rel in lineage_items:
        rows.append({
            "lineage_id": lid,
            "source_node": src,
            "target_node": tgt,
            "relationship_type": rel,
            "is_verified": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_explainability_lineage(df)
    return df, summary


def summarize_explainability_lineage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize explainability lineage records."""
    return {
        "total_lineage_records": len(df),
        "all_verified": bool(df["is_verified"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
