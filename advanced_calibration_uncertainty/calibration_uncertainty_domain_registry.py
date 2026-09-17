# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Domain Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)
from advanced_calibration_uncertainty.calibration_uncertainty_labels import (
    CALIBRATION_UNCERTAINTY_DOMAINS,
)


def build_calibration_uncertainty_domain_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all calibration and uncertainty domains."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for domain in CALIBRATION_UNCERTAINTY_DOMAINS:
        if domain == "unknown_calibration_uncertainty_domain":
            continue
        
        category = "governance"
        if "calibration" in domain and "metric" not in domain and "quality" not in domain:
            category = "probability_calibration"
        elif "uncertainty" in domain and "metric" not in domain and "quality" not in domain:
            category = "uncertainty_estimation"
        elif "metric" in domain or "evaluation" in domain:
            category = "metrics_and_evaluation"
        elif "guard" in domain or "policy" in domain:
            category = "safety_guards"
        elif "dependency" in domain:
            category = "dependencies"
        elif "placeholder" in domain:
            category = "placeholders"

        rows.append(
            {
                "domain_name": domain,
                "domain_category": category,
                "current_phase": prof.current_phase,
                "target_final_phase": prof.target_final_phase,
                "next_phase": prof.next_phase,
                "zero_execution_enforced": True,
                "non_signal": True,
                "dry_run_only": True,
                "status": "REGISTERED",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_uncertainty_domains(df)
    return df, summary


def summarize_calibration_uncertainty_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize domain registry DataFrame."""
    return {
        "total_domains": len(df),
        "domains": df["domain_name"].tolist() if not df.empty else [],
        "categories": df["domain_category"].unique().tolist() if not df.empty else [],
        "all_zero_execution": bool(df["zero_execution_enforced"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
