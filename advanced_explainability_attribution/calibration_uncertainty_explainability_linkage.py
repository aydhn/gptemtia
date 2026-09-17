# -*- coding: utf-8 -*-
"""Phase 143: Calibration and Uncertainty Explainability Linkage."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_calibration_uncertainty_explainability_linkage_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of calibration/uncertainty explainability linkage contracts."""
    prof = profile or get_explainability_profile()

    linkages = [
        ("calib_linkage_uncertainty_dispersion", "uncertainty_dispersion", "phase_141_calibration_uncertainty", "Attribution dispersion linked to epistemic uncertainty"),
        ("calib_linkage_brier_score_context", "brier_score_context", "phase_141_calibration_uncertainty", "Attribution confidence conditioned on Brier score reliability"),
        ("calib_linkage_ece_reliability_bands", "ece_reliability_bands", "phase_141_calibration_uncertainty", "Attribution validity conditional on expected calibration error bands"),
    ]

    rows: List[Dict[str, Any]] = []
    for lid, ltype, sourceref, desc in linkages:
        rows.append({
            "linkage_id": lid,
            "linkage_type": ltype,
            "source_calibration_ref": sourceref,
            "description": desc,
            "is_linkage_contract": True,
            "calibration_linked": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_calibration_uncertainty_explainability_linkage(df)
    return df, summary


def summarize_calibration_uncertainty_explainability_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration and uncertainty explainability linkage contracts."""
    return {
        "total_calibration_linkages": len(df),
        "all_linkage_contract": bool(df["is_linkage_contract"].all()) if not df.empty else True,
        "all_calibration_linked": bool(df["calibration_linked"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
