# -*- coding: utf-8 -*-
"""Phase 150: Backtest Performance Claim Boundaries.

Enforces strict prohibitions against strategy approval claims, guaranteed return
claims, production-ready assertions, and broker-ready approvals.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    PERFORMANCE_CLAIM_BOUNDARY_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

PERFORMANCE_BOUNDARIES: List[Dict[str, Any]] = [
    {
        "boundary_name": "boundary_block_guaranteed_return",
        "target_claim": "guaranteed_return",
        "policy": "Strictly prohibit any language implying return certainty or guaranteed profit.",
        "status": "ENFORCED_BLOCKED",
    },
    {
        "boundary_name": "boundary_block_proven_strategy",
        "target_claim": "proven_strategy",
        "policy": "Block claims that historical simulations constitute empirical proof of future profitability.",
        "status": "ENFORCED_BLOCKED",
    },
    {
        "boundary_name": "boundary_block_strategy_approval",
        "target_claim": "strategy_approved",
        "policy": "Block automated or premature strategy approval at Phase 150 governance level.",
        "status": "ENFORCED_BLOCKED",
    },
    {
        "boundary_name": "boundary_block_production_ready",
        "target_claim": "production_ready",
        "policy": "Block any assertion that governance readiness corresponds to production readiness.",
        "status": "ENFORCED_BLOCKED",
    },
    {
        "boundary_name": "boundary_block_broker_ready",
        "target_claim": "broker_ready",
        "policy": "Block broker integration and execution readiness claims.",
        "status": "ENFORCED_BLOCKED",
    },
    {
        "boundary_name": "boundary_block_official_approval",
        "target_claim": "official_approval",
        "policy": "Block official or regulatory approval assertions.",
        "status": "ENFORCED_BLOCKED",
    },
]

FORBIDDEN_PERFORMANCE_TOKENS = [
    "guaranteed_return",
    "guaranteed return",
    "proven_strategy",
    "proven strategy",
    "strategy_approved",
    "strategy approved",
    "approve_strategy",
    "production_ready",
    "production ready",
    "broker_ready",
    "broker ready",
    "official_approval",
    "official approval",
    "performance_claim",
    "performance claim",
]


def validate_performance_claim_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate a request against performance claim boundaries, blocking any performance claim."""
    text = str(request).lower()
    blocked = False
    violating_tokens: List[str] = []

    for token in FORBIDDEN_PERFORMANCE_TOKENS:
        if token in text:
            blocked = True
            violating_tokens.append(token)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "decision": "BLOCKED_BY_POLICY" if blocked else "ALLOWED_CONTRACT_METADATA_ONLY",
        "violating_tokens": violating_tokens,
        "policy_message": (
            "Performance and approval claims are strictly blocked by Phase 150 Backtest Governance policy. "
            "Governance readiness does NOT grant production or broker readiness."
            if blocked
            else "Request complies with non-claim governance boundaries."
        ),
        "non_signal": True,
    }


def summarize_backtest_performance_claim_boundaries(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize performance claim boundaries."""
    return {
        "domain": PERFORMANCE_CLAIM_BOUNDARY_DOMAIN,
        "total_boundaries": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "all_claims_blocked": bool((df["is_blocked"] == True).all()) if not df.empty else True,
        "all_approvals_disabled": bool((df["approval_allowed"] == False).all()) if not df.empty else True,
        "non_signal": True,
        "local_only": True,
    }


def build_backtest_performance_claim_boundary_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for performance claim boundaries."""
    rows: List[Dict[str, Any]] = []
    for b in PERFORMANCE_BOUNDARIES:
        rows.append({
            "boundary_name": b["boundary_name"],
            "target_claim": b["target_claim"],
            "policy": b["policy"],
            "is_blocked": True,
            "approval_allowed": False,
            "status": b["status"],
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = summarize_backtest_performance_claim_boundaries(df)
    return df, summary
