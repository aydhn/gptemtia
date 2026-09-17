# -*- coding: utf-8 -*-
"""Phase 144: Model Card Intended Use Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

INTENDED_USE_ITEMS: List[Dict[str, str]] = [
    {
        "use_id": "USE-001",
        "intended_domain": "offline_research",
        "description": "Local offline exploration of machine learning model contracts, interfaces, and architecture schemas.",
        "target_audience": "Quantitative researchers and ML engineers.",
    },
    {
        "use_id": "USE-002",
        "intended_domain": "governance_simulation",
        "description": "Verification of model card templates, approval boundary checks, and audit trail placeholders.",
        "target_audience": "Governance analysts and compliance officers.",
    },
    {
        "use_id": "USE-003",
        "intended_domain": "pipeline_integration_testing",
        "description": "Dry-run validation of inputs, dependencies, and contract compliance across Phases 136-144.",
        "target_audience": "System integration engineers.",
    },
    {
        "use_id": "USE-004",
        "intended_domain": "acceptance_preparation",
        "description": "Packaging evidence, findings, and checklists for Phase 145 Advanced ML Acceptance Report handoff.",
        "target_audience": "System architects and reviewers.",
    },
]


def build_model_card_intended_use_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card intended uses."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in INTENDED_USE_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["local_only"] = prof.local_only
        row["non_production"] = prof.non_production
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_card_intended_use(df)
    return df, summary


def summarize_model_card_intended_use(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card intended uses."""
    return {
        "total_intended_uses": len(df),
        "all_local_only": bool(df["local_only"].all()),
        "all_non_production": bool(df["non_production"].all()),
    }
