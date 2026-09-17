# -*- coding: utf-8 -*-
"""Phase 144: Governance Non-Production Boundaries Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

NON_PRODUCTION_RULES: List[Dict[str, str]] = [
    {"rule_id": "NPR-01", "rule_name": "local_offline_only", "enforcement": "All modules operate strictly on local file systems without external cloud deployments."},
    {"rule_id": "NPR-02", "rule_name": "zero_broker_connectivity", "enforcement": "Network sockets to broker order gateways or trade execution endpoints are blocked."},
    {"rule_id": "NPR-03", "rule_name": "non_signal_invariance", "enforcement": "No metric, score, or model card may produce trade recommendations or directional bias."},
    {"rule_id": "NPR-04", "rule_name": "audit_placeholder_only", "enforcement": "Audit records are governance placeholders and do not represent regulatory compliance logs."},
]


def build_governance_non_production_boundary_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance non-production boundaries."""
    prof = profile or get_model_governance_profile()
    records = []
    for r in NON_PRODUCTION_RULES:
        row = dict(r)
        row["phase"] = prof.current_phase
        row["is_enforced"] = True
        row["non_production"] = prof.non_production
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_non_production_boundaries(df)
    return df, summary


def summarize_governance_non_production_boundaries(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance non-production boundaries."""
    return {
        "total_rules": len(df),
        "all_enforced": bool(df["is_enforced"].all()),
        "non_production_active": bool(df["non_production"].all()),
    }
