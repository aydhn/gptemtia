# -*- coding: utf-8 -*-
"""Phase 150: Backtest Evidence Policies.

Defines evidentiary standards required before any backtest result can be reviewed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    EVIDENCE_POLICY_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

EVIDENCE_POLICIES: List[Dict[str, Any]] = [
    {
        "evidence_id": "EVD_01_INPUT_DATA_CONTRACT_PRESENT",
        "name": "input_data_contract_verification",
        "description": "Validation evidence showing historical price data meets Phase 112 data quality standards.",
    },
    {
        "evidence_id": "EVD_02_COST_REALISM_EVIDENCE",
        "name": "transaction_cost_model_attachment",
        "description": "Validation evidence documenting tiered fees and non-zero slippage assumptions.",
    },
    {
        "evidence_id": "EVD_03_LOOKAHEAD_AUDIT_CERTIFICATE",
        "name": "lookahead_clean_audit_evidence",
        "description": "Validation evidence verifying zero forward leakage and strict timestamp ordering.",
    },
    {
        "evidence_id": "EVD_04_DISABLED_EXECUTION_EVIDENCE",
        "name": "disabled_execution_compliance_evidence",
        "description": "Formal proof that live trading, broker, optimizer, and prediction were locked during research.",
    },
]


def build_backtest_evidence_policy_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for backtest evidence policies."""
    rows: List[Dict[str, Any]] = []
    for e in EVIDENCE_POLICIES:
        rows.append({
            "evidence_id": e["evidence_id"],
            "name": e["name"],
            "description": e["description"],
            "status": "ACTIVE",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": EVIDENCE_POLICY_DOMAIN,
        "total_evidence_policies": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
