# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Performance Claim Disabled Report Module.

Provides audit trail and request validator confirming marketing claims,
performance guarantees, and live/broker-ready claims are prohibited.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISABLED_EXECUTION_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)


def validate_no_monte_carlo_performance_claim_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming requests do not assert performance or readiness claims."""
    req_str = str(request).lower()
    prohibited = [
        "guaranteed_return",
        "robustness_claim",
        "sharpe_claim",
        "win_rate_claim",
        "production_ready",
        "broker_ready",
        "official_approval",
    ]
    for p in prohibited:
        if p in req_str:
            return {
                "claim_allowed": False,
                "reason": f"Prohibited performance or readiness claim detected: {p}",
                "status": "BLOCKED_BY_POLICY",
            }
    return {
        "claim_allowed": False,
        "reason": "Performance claims prohibited under Phase 149 contract layer.",
        "status": "PASS_NO_CLAIMS_DETECTED",
    }


def build_monte_carlo_performance_claim_disabled_report(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the performance claim disabled report DataFrame and summary."""
    rows: List[Dict[str, Any]] = [
        {
            "claim_type": "guaranteed_return_claim",
            "claim_allowed": profile.allow_performance_claim,
            "policy_reference": "POLICY_PHASE_149_ZERO_CLAIMS",
            "status": "BLOCKED_BY_POLICY",
            "description": "Prohibits promising future profit or return stability.",
        },
        {
            "claim_type": "production_readiness_claim",
            "claim_allowed": profile.allow_production_ready_claim,
            "policy_reference": "POLICY_PHASE_149_ZERO_CLAIMS",
            "status": "BLOCKED_BY_POLICY",
            "description": "Prohibits presenting robustness envelopes as production-ready approval.",
        },
        {
            "claim_type": "broker_readiness_claim",
            "claim_allowed": profile.allow_broker_ready_claim,
            "policy_reference": "POLICY_PHASE_149_ZERO_CLAIMS",
            "status": "BLOCKED_BY_POLICY",
            "description": "Prohibits asserting broker or live-trading readiness.",
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "total_claims": len(df),
        "all_claims_blocked": bool((~df["claim_allowed"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
