# -*- coding: utf-8 -*-
"""Phase 150: Backtest Audit Policies.

Governs immutable logging, parameter provenance, and code reproducibility.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    AUDIT_POLICY_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

AUDIT_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_id": "AUD_01_IMMUTABLE_PARAMETER_LOGGING",
        "name": "immutable_parameter_and_code_hash_logging",
        "description": "Log git commit hash, random seeds, and all hyperparameters before simulation start.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "policy_id": "AUD_02_TIME_STAMPED_EXPERIMENT_LOGS",
        "name": "time_stamped_experiment_audit_trail",
        "description": "Retain structured JSON logs of all dry runs with ISO 8601 timestamps.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "policy_id": "AUD_03_DATA_PROVENANCE_LINEAGE",
        "name": "data_provenance_and_lineage_verification",
        "description": "Link backtest inputs directly to Phase 114 lineage and Phase 124/134 FeatureStore identifiers.",
        "enforcement": "HIGH_AUDIT",
    },
]


def build_backtest_audit_policy_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for backtest audit policies."""
    rows: List[Dict[str, Any]] = []
    for p in AUDIT_POLICIES:
        rows.append({
            "policy_id": p["policy_id"],
            "name": p["name"],
            "description": p["description"],
            "enforcement": p["enforcement"],
            "retention_days": profile.audit_trail_retention_days,
            "status": "ACTIVE",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": AUDIT_POLICY_DOMAIN,
        "total_policies": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "retention_days": profile.audit_trail_retention_days,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
