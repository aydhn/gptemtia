# -*- coding: utf-8 -*-
"""Phase 150: Backtest Metric Claim Boundaries.

Blocks attempts to compute or claim real numerical backtest metrics (Sharpe,
win-rate, alpha, drawdown, returns) within the Phase 150 contract layer.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    METRIC_CLAIM_BOUNDARY_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

METRIC_BOUNDARIES: List[Dict[str, Any]] = [
    {
        "boundary_name": "boundary_block_actual_sharpe",
        "target_metric": "actual_sharpe",
        "policy": "Block calculation of realized Sharpe ratio in Phase 150.",
        "status": "ENFORCED_BLOCKED",
    },
    {
        "boundary_name": "boundary_block_actual_win_rate",
        "target_metric": "actual_win_rate",
        "policy": "Block calculation of realized trade win rates in Phase 150.",
        "status": "ENFORCED_BLOCKED",
    },
    {
        "boundary_name": "boundary_block_actual_alpha",
        "target_metric": "actual_alpha",
        "policy": "Block calculation of annualized strategy alpha in Phase 150.",
        "status": "ENFORCED_BLOCKED",
    },
    {
        "boundary_name": "boundary_block_actual_return",
        "target_metric": "actual_return",
        "policy": "Block calculation of cumulative or CAGR strategy return in Phase 150.",
        "status": "ENFORCED_BLOCKED",
    },
    {
        "boundary_name": "boundary_block_actual_drawdown",
        "target_metric": "actual_drawdown",
        "policy": "Block calculation of realized maximum drawdown in Phase 150.",
        "status": "ENFORCED_BLOCKED",
    },
    {
        "boundary_name": "boundary_block_actual_var_es",
        "target_metric": "actual_var_es",
        "policy": "Block calculation of realized VaR and Expected Shortfall in Phase 150.",
        "status": "ENFORCED_BLOCKED",
    },
]

FORBIDDEN_METRIC_KEYWORDS = [
    "calculate_sharpe",
    "calculate_win_rate",
    "calculate_alpha",
    "calculate_return",
    "calculate_drawdown",
    "calculate_var",
    "actual_sharpe",
    "actual_win_rate",
    "actual_alpha",
    "actual_return",
    "actual_drawdown",
]


def validate_metric_claim_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate a request against metric claim boundaries, blocking any real calculation."""
    text = str(request).lower()
    blocked = False
    violating_tokens: List[str] = []

    for token in FORBIDDEN_METRIC_KEYWORDS:
        if token in text:
            blocked = True
            violating_tokens.append(token)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "decision": "BLOCKED_BY_POLICY" if blocked else "ALLOWED_CONTRACT_METADATA_ONLY",
        "violating_tokens": violating_tokens,
        "policy_message": (
            "Metric calculation is strictly blocked by Phase 150 Backtest Governance policy. "
            "All numerical metric values remain contract placeholders."
            if blocked
            else "Request complies with metadata-only governance boundaries."
        ),
        "non_signal": True,
    }


def summarize_backtest_metric_claim_boundaries(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize metric claim boundaries."""
    return {
        "domain": METRIC_CLAIM_BOUNDARY_DOMAIN,
        "total_boundaries": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "all_metrics_blocked": bool((df["is_blocked"] == True).all()) if not df.empty else True,
        "all_calculations_disabled": bool((df["calculation_allowed"] == False).all()) if not df.empty else True,
        "non_signal": True,
        "local_only": True,
    }


def build_backtest_metric_claim_boundary_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for metric claim boundaries."""
    rows: List[Dict[str, Any]] = []
    for b in METRIC_BOUNDARIES:
        rows.append({
            "boundary_name": b["boundary_name"],
            "target_metric": b["target_metric"],
            "policy": b["policy"],
            "is_blocked": True,
            "calculation_allowed": False,
            "status": b["status"],
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = summarize_backtest_metric_claim_boundaries(df)
    return df, summary
