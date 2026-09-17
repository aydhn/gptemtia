# -*- coding: utf-8 -*-
"""Phase 150: Monte Carlo Governance.

Governs integration with Phase 149 Monte Carlo robustness and resampling contracts.
Zero Monte Carlo simulation in Phase 150.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    MONTE_CARLO_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

MONTE_CARLO_GOVERNANCE_ITEMS: List[Dict[str, Any]] = [
    {
        "governance_id": "MC_01_RESAMPLING_CONTRACT_MANDATE",
        "name": "mandatory_bootstrap_resampling_coverage",
        "description": "Backtest evaluation must include return path resampling and trade reshuffling contracts from Phase 149.",
        "phase_149_ref": "PHASE_149_BOOTSTRAP_CONTRACTS",
    },
    {
        "governance_id": "MC_02_ROBUSTNESS_ENVELOPE_MANDATE",
        "name": "robustness_envelope_specification",
        "description": "Require parameter sensitivity envelope boundaries and stability confidence intervals.",
        "phase_149_ref": "PHASE_149_PARAMETER_STABILITY_CONTRACTS",
    },
    {
        "governance_id": "MC_03_EXECUTION_LOCK",
        "name": "monte_carlo_execution_lock_policy",
        "description": "Block actual Monte Carlo iterations and bootstrap resamplings at Phase 150 governance layer.",
        "phase_149_ref": "PHASE_149_DISABLED_EXECUTION_SPECS",
    },
]


def build_monte_carlo_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Monte Carlo governance."""
    rows: List[Dict[str, Any]] = []
    for item in MONTE_CARLO_GOVERNANCE_ITEMS:
        rows.append({
            "governance_id": item["governance_id"],
            "name": item["name"],
            "description": item["description"],
            "phase_149_ref": item["phase_149_ref"],
            "execution_allowed": False,
            "status": "GOVERNANCE_CONTRACT_READY",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": MONTE_CARLO_GOVERNANCE_DOMAIN,
        "total_items": len(df),
        "execution_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
