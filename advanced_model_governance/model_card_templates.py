# -*- coding: utf-8 -*-
"""Phase 144: Model Card Templates."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

STANDARD_TEMPLATE_SECTIONS: List[str] = [
    "overview",
    "intended_use",
    "prohibited_use",
    "data_sources",
    "feature_dependencies",
    "model_family",
    "limitations",
    "risk_disclosures",
    "validation_evidence",
    "no_go_boundaries",
    "manual_review_requirements",
    "non_production_disclaimer",
]

TEMPLATE_FAMILIES: List[Dict[str, str]] = [
    {"template_name": "baseline_template", "model_family": "baseline_models"},
    {"template_name": "candidate_template", "model_family": "candidate_models"},
    {"template_name": "ensemble_template", "model_family": "ensemble_models"},
    {"template_name": "calibration_template", "model_family": "calibration_uncertainty"},
    {"template_name": "drift_template", "model_family": "drift_monitoring"},
    {"template_name": "explainability_template", "model_family": "explainability_attribution"},
    {"template_name": "acceptance_template", "model_family": "advanced_ml_acceptance"},
]


def build_model_card_template_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card templates."""
    prof = profile or get_model_governance_profile()
    records = []
    for tf in TEMPLATE_FAMILIES:
        records.append({
            "template_name": tf["template_name"],
            "model_family": tf["model_family"],
            "section_count": len(STANDARD_TEMPLATE_SECTIONS),
            "sections_csv": ",".join(STANDARD_TEMPLATE_SECTIONS),
            "is_dry_run": prof.dry_run_default,
            "non_production": prof.non_production,
            "manual_review_required": True,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary = summarize_model_card_templates(df)
    return df, summary


def summarize_model_card_templates(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card templates."""
    return {
        "total_templates": len(df),
        "standard_sections_count": len(STANDARD_TEMPLATE_SECTIONS),
        "all_dry_run": bool(df["is_dry_run"].all()),
        "all_non_production": bool(df["non_production"].all()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
    }
