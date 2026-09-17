# -*- coding: utf-8 -*-
"""Phase 150: Walk-Forward Governance.

Governs anchored and rolling walk-forward validation contracts under Phase 147 linkage.
Zero walk-forward execution in Phase 150.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    WALK_FORWARD_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

WALK_FORWARD_GOVERNANCE_ITEMS: List[Dict[str, Any]] = [
    {
        "governance_id": "WF_01_WINDOW_EXPANSION_CONTRACT",
        "title": "anchored_vs_rolling_window_policy",
        "description": "Formally specify anchored (expanding) or fixed-width rolling windows with explicit step sizes.",
        "phase_147_ref": "PHASE_147_ROLLING_EXPANDING_CONTRACTS",
    },
    {
        "governance_id": "WF_02_OUT_OF_SAMPLE_STEP_ISOLATION",
        "title": "oos_step_forward_isolation",
        "description": "Each walk-forward test block must be evaluated exactly once without backward re-tuning.",
        "phase_147_ref": "PHASE_147_OOS_SPLIT_CONTRACTS",
    },
    {
        "governance_id": "WF_03_EXECUTION_LOCK",
        "title": "walk_forward_execution_lock_policy",
        "description": "Prohibit executing real walk-forward optimization runs at Phase 150 governance layer.",
        "phase_147_ref": "PHASE_147_DISABLED_EXECUTION_SPECS",
    },
]


def build_walk_forward_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for walk-forward governance."""
    rows: List[Dict[str, Any]] = []
    for item in WALK_FORWARD_GOVERNANCE_ITEMS:
        rows.append({
            "governance_id": item["governance_id"],
            "title": item["title"],
            "description": item["description"],
            "phase_147_ref": item["phase_147_ref"],
            "execution_allowed": False,
            "status": "GOVERNANCE_CONTRACT_READY",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": WALK_FORWARD_GOVERNANCE_DOMAIN,
        "total_items": len(df),
        "execution_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
