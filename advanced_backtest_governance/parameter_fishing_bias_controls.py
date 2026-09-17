# -*- coding: utf-8 -*-
"""Phase 150: Parameter Fishing Bias Controls.

Governs p-hacking and parameter cherry-picking prohibitions.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    PARAMETER_FISHING_BIAS_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

PARAMETER_FISHING_CONTROLS: List[Dict[str, Any]] = [
    {
        "control_id": "FSH_01_PRE_REGISTERED_HYPOTHESIS",
        "name": "pre_registered_parameter_space_mandate",
        "description": "Require parameter search boundaries to be pre-registered based on financial theory before backtest iteration.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "control_id": "FSH_02_SURFACE_STABILITY_CHECK",
        "name": "parameter_plateau_smoothness_requirement",
        "description": "Reject isolated parameter spikes surrounded by collapse; mandate broad performance plateaus.",
        "enforcement": "HIGH_AUDIT",
    },
    {
        "control_id": "FSH_03_OPTIMIZER_SWEEP_EXCLUSION",
        "name": "optimizer_execution_lock_policy",
        "description": "Strictly block automated parameter grid/random optimization runs in Phase 150 governance layer.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
]


def build_parameter_fishing_bias_control_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for parameter fishing bias controls."""
    rows: List[Dict[str, Any]] = []
    for c in PARAMETER_FISHING_CONTROLS:
        rows.append({
            "control_id": c["control_id"],
            "name": c["name"],
            "description": c["description"],
            "enforcement": c["enforcement"],
            "status": "ACTIVE",
            "execution_allowed": False,
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": PARAMETER_FISHING_BIAS_DOMAIN,
        "total_controls": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
