# -*- coding: utf-8 -*-
"""Phase 150: Data Snooping Bias Controls.

Governs reuse of datasets across strategy iterations and mitigates data mining biases.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    DATA_SNOOPING_BIAS_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

DATA_SNOOPING_CONTROLS: List[Dict[str, Any]] = [
    {
        "control_id": "SNP_01_TEST_SET_QUARANTINE",
        "name": "strict_test_set_quarantine",
        "description": "Quarantine out-of-sample data so that parameters and rules are strictly fixed before OOS contact.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "control_id": "SNP_02_REUSE_TRACKING",
        "name": "dataset_reuse_and_iteration_tracking",
        "description": "Log each hypothesis evaluation against identical time slices to track cumulative search intensity.",
        "enforcement": "HIGH_AUDIT",
    },
    {
        "control_id": "SNP_03_HAIRCUT_PENALTY",
        "name": "white_reality_check_haircut_placeholder",
        "description": "Enforce theoretical haircut discount on strategy performance proportional to iteration count.",
        "enforcement": "HIGH_AUDIT",
    },
]


def build_data_snooping_bias_control_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for data snooping bias controls."""
    rows: List[Dict[str, Any]] = []
    for c in DATA_SNOOPING_CONTROLS:
        rows.append({
            "control_id": c["control_id"],
            "name": c["name"],
            "description": c["description"],
            "enforcement": c["enforcement"],
            "snooping_penalty_rate": profile.snooping_penalty_rate,
            "status": "ACTIVE",
            "execution_allowed": False,
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": DATA_SNOOPING_BIAS_DOMAIN,
        "total_controls": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "snooping_penalty_rate": profile.snooping_penalty_rate,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
