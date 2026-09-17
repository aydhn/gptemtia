# -*- coding: utf-8 -*-
"""Phase 150: Parameter Stability Governance.

Governs sensitivity analysis and stability validation under zero parameter-sweeping.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    PARAMETER_FISHING_BIAS_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

PARAMETER_STABILITY_ITEMS: List[Dict[str, Any]] = [
    {
        "stability_id": "PST_01_PERTURBATION_TOLERANCE",
        "name": "parameter_perturbation_tolerance_contract",
        "description": "Requires strategy performance to remain stable under +/- 10-20% parameter shifts.",
    },
    {
        "stability_id": "PST_02_CLIFF_EFFECT_PROHIBITION",
        "name": "cliff_effect_and_knife_edge_prohibition",
        "description": "Rejects strategies whose returns depend on razor-thin threshold values that collapse on minor perturbations.",
    },
    {
        "stability_id": "PST_03_OPTIMIZER_SWEEP_BAN",
        "name": "parameter_optimizer_sweep_lock",
        "description": "Prohibits running active automated parameter search loops at governance contract level.",
    },
]


def build_parameter_stability_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for parameter stability governance."""
    rows: List[Dict[str, Any]] = []
    for item in PARAMETER_STABILITY_ITEMS:
        rows.append({
            "stability_id": item["stability_id"],
            "name": item["name"],
            "description": item["description"],
            "execution_allowed": False,
            "status": "GOVERNANCE_CONTRACT_READY",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": PARAMETER_FISHING_BIAS_DOMAIN,
        "subdomain": "parameter_stability_governance",
        "total_rules": len(df),
        "execution_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
