# -*- coding: utf-8 -*-
"""Phase 143: Explainability Experiment Linkage."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_explainability_experiment_linkage_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of explainability experiment linkage records."""
    prof = profile or get_explainability_profile()

    experiments = [
        ("exp_link_brent_attribution_run_001", "exp_brent_crude_rf_baseline", "exp_report_tree_shap_brent", "offline_research_run"),
        ("exp_link_gold_attribution_run_001", "exp_gold_gbdt_baseline", "exp_report_permutation_gold", "offline_research_run"),
        ("exp_link_fx_attribution_run_001", "exp_usd_try_mlp_baseline", "exp_report_pdp_usd_try", "offline_research_run"),
    ]

    rows: List[Dict[str, Any]] = []
    for elid, erun, erep, rtype in experiments:
        rows.append({
            "experiment_linkage_id": elid,
            "experiment_run_id": erun,
            "explainability_report_ref": erep,
            "run_type": rtype,
            "is_experiment_linked": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_explainability_experiment_linkage(df)
    return df, summary


def summarize_explainability_experiment_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize explainability experiment linkages."""
    return {
        "total_experiment_linkages": len(df),
        "all_linked": bool(df["is_experiment_linked"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
