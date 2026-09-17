# -*- coding: utf-8 -*-
"""Phase 150: Overfitting Bias Controls.

Governs strategy complexity bounds and detects parameter curve-fitting fragility.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    OVERFITTING_BIAS_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

OVERFITTING_CONTROLS: List[Dict[str, Any]] = [
    {
        "control_id": "OVF_01_DEGREES_OF_FREEDOM_BOUND",
        "name": "parameter_to_sample_size_ratio_bound",
        "description": "Limit total tunable strategy parameters relative to independent trade observations (e.g. min 50 trades per parameter).",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "control_id": "OVF_02_IN_SAMPLE_OUT_SAMPLE_SPREAD",
        "name": "is_oos_performance_degradation_envelope",
        "description": "Flag strategies where simulated out-of-sample degradation exceeds 50% of in-sample performance.",
        "enforcement": "HIGH_AUDIT",
    },
    {
        "control_id": "OVF_03_CSC_PROBABILITY_PLACEHOLDER",
        "name": "combinatorial_purged_cross_validation_placeholder",
        "description": "Enforce Combinatorially Symmetric Cross-Validation (CSCV) and Probability of Backtest Overfitting (PBO) framework.",
        "enforcement": "HIGH_AUDIT",
    },
]


def build_overfitting_bias_control_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for overfitting bias controls."""
    rows: List[Dict[str, Any]] = []
    for c in OVERFITTING_CONTROLS:
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
        "domain": OVERFITTING_BIAS_DOMAIN,
        "total_controls": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
