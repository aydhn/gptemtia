# -*- coding: utf-8 -*-
"""Phase 144: Model Card Sections."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

SECTION_DEFINITIONS: List[Dict[str, Any]] = [
    {"section_id": "SEC-01", "section_name": "overview", "description": "High-level summary of model contract, purpose, and phase context.", "required": True},
    {"section_id": "SEC-02", "section_name": "intended_use", "description": "Designated research and offline analysis scope.", "required": True},
    {"section_id": "SEC-03", "section_name": "prohibited_use", "description": "Strict prohibition of live trading, broker actions, and advice.", "required": True},
    {"section_id": "SEC-04", "section_name": "data_sources", "description": "Lineage and references to Phase 137 dataset contracts.", "required": True},
    {"section_id": "SEC-05", "section_name": "feature_dependencies", "description": "Dependencies on FeatureStore and technical/macro factor spaces.", "required": True},
    {"section_id": "SEC-06", "section_name": "model_family", "description": "Specification of model architecture and hyperparameter contracts.", "required": True},
    {"section_id": "SEC-07", "section_name": "limitations", "description": "Known constraints, non-materialized state, and non-predictive status.", "required": True},
    {"section_id": "SEC-08", "section_name": "risk_disclosures", "description": "Identification of modeling, drift, and market regime risks.", "required": True},
    {"section_id": "SEC-09", "section_name": "validation_evidence", "description": "Evidence from prior phases (136-143) validation harnesses.", "required": True},
    {"section_id": "SEC-10", "section_name": "no_go_boundaries", "description": "Strict boundary conditions halting execution or deployment.", "required": True},
    {"section_id": "SEC-11", "section_name": "manual_review_requirements", "description": "Review procedures before accepting governance artifacts.", "required": True},
    {"section_id": "SEC-12", "section_name": "non_production_disclaimer", "description": "Explicit warning that artifact is not an approval or signal.", "required": True},
]


def build_model_card_section_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card sections."""
    prof = profile or get_model_governance_profile()
    records = []
    for s in SECTION_DEFINITIONS:
        row = dict(s)
        row["manual_review_gate"] = "review_required"
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_card_sections(df)
    return df, summary


def summarize_model_card_sections(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card sections."""
    return {
        "total_sections": len(df),
        "all_required": bool(df["required"].all()),
        "all_manual_review_gated": bool((df["manual_review_gate"] == "review_required").all()),
    }
