# -*- coding: utf-8 -*-
"""Phase 150: Multiple Testing Bias Controls.

Governs multiple comparison corrections and false discovery rate control.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    MULTIPLE_TESTING_BIAS_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

MULTIPLE_TESTING_CONTROLS: List[Dict[str, Any]] = [
    {
        "control_id": "MLT_01_TRIAL_COUNT_CAPPING",
        "name": "maximum_allowable_trials_threshold",
        "description": "Cap cumulative strategy variations evaluated on a given asset/timeframe pair.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "control_id": "MLT_02_BONFERRONI_HOLM_HAIRCUT",
        "name": "familywise_error_rate_adjustment",
        "description": "Require Bonferroni or Holm step-down critical value adjustments for multi-rule screening.",
        "enforcement": "HIGH_AUDIT",
    },
    {
        "control_id": "MLT_03_FDR_BENJAMINI_HOCHBERG",
        "name": "false_discovery_rate_control_placeholder",
        "description": "Establish Benjamini-Hochberg-Yekutieli FDR thresholds for multi-asset strategy evaluations.",
        "enforcement": "HIGH_AUDIT",
    },
]


def build_multiple_testing_bias_control_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for multiple testing bias controls."""
    rows: List[Dict[str, Any]] = []
    for c in MULTIPLE_TESTING_CONTROLS:
        rows.append({
            "control_id": c["control_id"],
            "name": c["name"],
            "description": c["description"],
            "enforcement": c["enforcement"],
            "max_allowable_tests": profile.max_allowable_multiple_tests,
            "status": "ACTIVE",
            "execution_allowed": False,
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": MULTIPLE_TESTING_BIAS_DOMAIN,
        "total_controls": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "max_allowable_multiple_tests": profile.max_allowable_multiple_tests,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
