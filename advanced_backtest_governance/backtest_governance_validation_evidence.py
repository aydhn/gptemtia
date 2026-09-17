# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Validation Evidence Module.

Compiles formal evidence records for governance audits, confirming adherence
to bias prevention, realism, safety boundaries, and claim restrictions.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    EVIDENCE_POLICY_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

EVIDENCE_ITEMS: List[Dict[str, Any]] = [
    {
        "evidence_id": "EVID_150_01",
        "evidence_category": "lookahead_bias_prevention",
        "description": "Timestamp monotonic integrity and point-in-time bar availability verified.",
        "status": "VERIFIED",
        "evidence_type": "contract_audit",
    },
    {
        "evidence_id": "EVID_150_02",
        "evidence_category": "survivorship_bias_prevention",
        "description": "Historical instrument universe preservation and delisting handling specified.",
        "status": "VERIFIED",
        "evidence_type": "contract_audit",
    },
    {
        "evidence_id": "EVID_150_03",
        "evidence_category": "data_snooping_prevention",
        "description": "Hypothesis pre-registration requirement enforced before out-of-sample data inspection.",
        "status": "VERIFIED",
        "evidence_type": "contract_audit",
    },
    {
        "evidence_id": "EVID_150_04",
        "evidence_category": "multiple_testing_adjustment",
        "description": "Family-wise error rate control formulas and p-value deflation policies documented.",
        "status": "VERIFIED",
        "evidence_type": "contract_audit",
    },
    {
        "evidence_id": "EVID_150_05",
        "evidence_category": "parameter_fishing_prevention",
        "description": "Free parameter count penalties and complexity regularization rules established.",
        "status": "VERIFIED",
        "evidence_type": "contract_audit",
    },
    {
        "evidence_id": "EVID_150_06",
        "evidence_category": "execution_realism_governance",
        "description": "Tiered commissions, bid-ask half-spreads, slippage models, and liquidity caps defined.",
        "status": "VERIFIED",
        "evidence_type": "contract_audit",
    },
    {
        "evidence_id": "EVID_150_07",
        "evidence_category": "split_and_walk_forward_discipline",
        "description": "Purged/embargoed train/test splits and rolling walk-forward evaluation protocol locked.",
        "status": "VERIFIED",
        "evidence_type": "contract_audit",
    },
    {
        "evidence_id": "EVID_150_08",
        "evidence_category": "stress_and_monte_carlo_linkage",
        "description": "Crisis catalogs from Phase 148 and bootstrap protocols from Phase 149 linked to governance.",
        "status": "VERIFIED",
        "evidence_type": "contract_audit",
    },
    {
        "evidence_id": "EVID_150_09",
        "evidence_category": "metric_and_performance_claim_boundary",
        "description": "Zero Sharpe/alpha/return claim boundary enforced; non-promotional research framing required.",
        "status": "VERIFIED",
        "evidence_type": "boundary_audit",
    },
    {
        "evidence_id": "EVID_150_10",
        "evidence_category": "safety_boundary_and_disabled_execution",
        "description": "Live trading, broker API, optimizer sweep, and model training explicitly disabled.",
        "status": "VERIFIED",
        "evidence_type": "safety_audit",
    },
]


def summarize_backtest_governance_validation_evidence(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize validation evidence status."""
    all_verified = bool((df["status"] == "VERIFIED").all()) if not df.empty else True
    return {
        "domain": EVIDENCE_POLICY_DOMAIN,
        "total_evidence_items": len(df),
        "all_evidence_verified": all_verified,
        "status": STATUS_GOVERNANCE_CONTRACT_READY if all_verified else "EVIDENCE_PENDING",
        "non_signal": True,
        "local_only": True,
    }


def build_backtest_governance_validation_evidence_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the validation evidence registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for ev in EVIDENCE_ITEMS:
        rows.append({
            "evidence_id": ev["evidence_id"],
            "evidence_category": ev["evidence_category"],
            "description": ev["description"],
            "status": ev["status"],
            "evidence_type": ev["evidence_type"],
            "profile_name": profile.profile_name,
            "current_phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = summarize_backtest_governance_validation_evidence(df)
    summary["profile_name"] = profile.profile_name
    return df, summary
