# -*- coding: utf-8 -*-
"""Phase 143: Drift Explainability Linkage."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_drift_explainability_linkage_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of drift explainability linkage contracts."""
    prof = profile or get_explainability_profile()

    linkages = [
        ("drift_linkage_feature_drift_to_attribution", "feature_drift_to_attribution", "phase_142_drift_monitoring", "Linkage between detected feature drift and attribution change"),
        ("drift_linkage_concept_drift_to_attribution", "concept_drift_to_attribution", "phase_142_drift_monitoring", "Linkage between detected concept drift and attribution change"),
        ("drift_linkage_prediction_drift_to_attribution", "prediction_drift_to_attribution", "phase_142_drift_monitoring", "Linkage between prediction drift and attribution change"),
    ]

    rows: List[Dict[str, Any]] = []
    for lid, dtype, sourceref, desc in linkages:
        rows.append({
            "linkage_id": lid,
            "drift_type": dtype,
            "source_drift_ref": sourceref,
            "description": desc,
            "is_linkage_contract": True,
            "drift_investigation_allowed": False,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_drift_explainability_linkage(df)
    return df, summary


def summarize_drift_explainability_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize drift explainability linkage contracts."""
    return {
        "total_drift_linkages": len(df),
        "all_linkage_contract": bool(df["is_linkage_contract"].all()) if not df.empty else True,
        "all_investigation_blocked": bool((~df["drift_investigation_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
