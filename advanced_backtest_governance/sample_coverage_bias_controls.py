# -*- coding: utf-8 -*-
"""Phase 150: Sample Coverage Bias Controls.

Governs observational sample length, bar density, and unrepresentative time window bias.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    SAMPLE_COVERAGE_BIAS_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

SAMPLE_CONTROLS: List[Dict[str, Any]] = [
    {
        "control_id": "SMP_01_MINIMUM_OBSERVATION_SPAN",
        "name": "minimum_observation_span_policy",
        "description": "Enforce minimum sample duration (e.g. at least 5 years of daily bars or equivalent tick density).",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "control_id": "SMP_02_CALENDAR_ANOMALY_AUDIT",
        "name": "holiday_weekend_session_gap_audit",
        "description": "Verify treatment of market holidays, session closures, and non-trading intervals.",
        "enforcement": "HIGH_AUDIT",
    },
    {
        "control_id": "SMP_03_SELECTIVE_CHOPPING_BAN",
        "name": "selective_period_chopping_prohibition",
        "description": "Prohibit carving out unpalatable market episodes (e.g. flash crashes, liquidity droughts) from evaluation.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
]


def build_sample_coverage_bias_control_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for sample coverage bias controls."""
    rows: List[Dict[str, Any]] = []
    for c in SAMPLE_CONTROLS:
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
        "domain": SAMPLE_COVERAGE_BIAS_DOMAIN,
        "total_controls": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
