# -*- coding: utf-8 -*-
"""Phase 150: Benchmark Selection Bias Controls.

Governs neutral benchmark baseline assignment and prohibits post-hoc benchmark switching.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    BENCHMARK_SELECTION_BIAS_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

BENCHMARK_CONTROLS: List[Dict[str, Any]] = [
    {
        "control_id": "BMK_01_PRE_COMMITTED_BASELINES",
        "name": "pre_committed_benchmark_specification",
        "description": "Mandate selection of neutral benchmark (buy-and-hold underlying and cash baseline) prior to backtesting.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "control_id": "BMK_02_POST_HOC_SWAP_BAN",
        "name": "post_hoc_benchmark_switching_prohibition",
        "description": "Prohibit changing benchmark baselines to artificially enhance relative alpha or Sharpe claims.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "control_id": "BMK_03_RISK_ADJUSTED_EQUIVALENCE",
        "name": "volatility_matched_benchmark_contract",
        "description": "Require leverage-matched or volatility-adjusted benchmark comparisons for leveraged strategy designs.",
        "enforcement": "HIGH_AUDIT",
    },
]


def build_benchmark_selection_bias_control_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for benchmark selection bias controls."""
    rows: List[Dict[str, Any]] = []
    for c in BENCHMARK_CONTROLS:
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
        "domain": BENCHMARK_SELECTION_BIAS_DOMAIN,
        "total_controls": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
