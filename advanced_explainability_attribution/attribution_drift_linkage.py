# -*- coding: utf-8 -*-
"""Phase 143: Attribution Drift Linkage."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_attribution_drift_linkage_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of attribution drift linkage contracts."""
    prof = profile or get_explainability_profile()

    linkages = [
        ("linkage_psi_attribution_shift", "population_stability_index", "phase_142_drift_monitoring", "Attribution distribution shift tracked via PSI placeholder"),
        ("linkage_ks_attribution_shift", "kolmogorov_smirnov", "phase_142_drift_monitoring", "Attribution distribution shift tracked via KS placeholder"),
        ("linkage_wasserstein_attribution_shift", "wasserstein_distance", "phase_142_drift_monitoring", "Attribution distribution shift tracked via Wasserstein placeholder"),
        ("linkage_ranking_inversion_shift", "kendall_tau_ranking_inversion", "phase_142_drift_monitoring", "Top feature ranking inversion drift tracked via Kendall tau placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for lid, dmethod, sourceref, desc in linkages:
        rows.append({
            "linkage_id": lid,
            "drift_method": dmethod,
            "drift_source_ref": sourceref,
            "description": desc,
            "drift_calculated": False,
            "is_linkage_contract": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_attribution_drift_linkage(df)
    return df, summary


def summarize_attribution_drift_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize attribution drift linkage contracts."""
    return {
        "total_drift_linkages": len(df),
        "all_linkage_contract": bool(df["is_linkage_contract"].all()) if not df.empty else True,
        "all_drift_calculated_false": bool((~df["drift_calculated"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
