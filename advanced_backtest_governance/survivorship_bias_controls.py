# -*- coding: utf-8 -*-
"""Phase 150: Survivorship Bias Controls.

Enforces point-in-time universe reconstitution and prevents evaluating only
assets that survived until the current date.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    SURVIVORSHIP_BIAS_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

SURVIVORSHIP_CONTROLS: List[Dict[str, Any]] = [
    {
        "control_id": "SRV_01_POINT_IN_TIME_UNIVERSE",
        "name": "point_in_time_constituent_reconstitution",
        "description": "Ensure historical simulations include delisted, liquidated, or merged instruments actively trading at bar date.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "control_id": "SRV_02_DELISTING_RETURN_TREATMENT",
        "name": "delisting_and_liquidation_loss_inclusion",
        "description": "Incorporate delisting events, terminal payouts, and final liquidation pricing to avoid upward survivorship drift.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "control_id": "SRV_03_RETROACTIVE_ADDITION_BAN",
        "name": "retroactive_universe_addition_prohibition",
        "description": "Prohibit retroactively back-extrapolating newly added instruments into eras prior to their inception date.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
]


def build_survivorship_bias_control_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for survivorship bias controls."""
    rows: List[Dict[str, Any]] = []
    for c in SURVIVORSHIP_CONTROLS:
        rows.append({
            "control_id": c["control_id"],
            "name": c["name"],
            "description": c["description"],
            "enforcement": c["enforcement"],
            "policy_mode": profile.survivorship_policy_mode,
            "status": "ACTIVE",
            "execution_allowed": False,
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": SURVIVORSHIP_BIAS_DOMAIN,
        "total_controls": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "policy_mode": profile.survivorship_policy_mode,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
