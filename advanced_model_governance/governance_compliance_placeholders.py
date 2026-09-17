# -*- coding: utf-8 -*-
"""Phase 144: Governance Compliance Placeholders Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

COMPLIANCE_PLACEHOLDER_ITEMS: List[Dict[str, str]] = [
    {"placeholder_id": "CMP-01", "regulatory_framework": "EU_AI_ACT_SIMULATION", "scope": "Risk categorization placeholder for algorithmic systems.", "legal_opinion": "NONE", "official_approval": "NONE"},
    {"placeholder_id": "CMP-02", "regulatory_framework": "SR_11_7_MODEL_RISK", "scope": "Model inventory and conceptual soundness placeholder.", "legal_opinion": "NONE", "official_approval": "NONE"},
    {"placeholder_id": "CMP-03", "regulatory_framework": "NIST_AI_RMF", "scope": "Govern, Map, Measure, Manage governance mapping placeholder.", "legal_opinion": "NONE", "official_approval": "NONE"},
]


def build_governance_compliance_placeholder_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance compliance placeholders."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in COMPLIANCE_PLACEHOLDER_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["is_placeholder"] = True
        row["is_legal_opinion"] = False
        row["is_regulatory_approval"] = False
        row["is_production_approval"] = False
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_compliance_placeholders(df)
    return df, summary


def summarize_governance_compliance_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance compliance placeholders."""
    return {
        "total_placeholders": len(df),
        "all_placeholders": bool(df["is_placeholder"].all()),
        "zero_legal_opinions": not bool(df["is_legal_opinion"].any()),
        "zero_regulatory_approvals": not bool(df["is_regulatory_approval"].any()),
        "zero_production_approvals": not bool(df["is_production_approval"].any()),
    }
