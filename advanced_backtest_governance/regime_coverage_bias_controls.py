# -*- coding: utf-8 -*-
"""Phase 150: Regime Coverage Bias Controls.

Ensures backtest evaluation spans diverse market regimes and avoids single-regime bias.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    REGIME_COVERAGE_BIAS_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

REGIME_CONTROLS: List[Dict[str, Any]] = [
    {
        "control_id": "RGM_01_MULTI_REGIME_SPAN",
        "name": "multi_regime_breadth_validation",
        "description": "Require backtest timeline to intersect multiple Phase 126-135 regime states (bull, bear, sideways, high-vol).",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "control_id": "RGM_02_REGIME_PROPORTION_AUDIT",
        "name": "regime_proportionality_audit",
        "description": "Detect backtests where >80% of bars reside in a single regime state and flag regime concentration risk.",
        "enforcement": "HIGH_AUDIT",
    },
    {
        "control_id": "RGM_03_REGIME_CONDITIONAL_METRICS_PLACEHOLDER",
        "name": "regime_conditioned_metric_disclosure_placeholder",
        "description": "Require performance reporting broken down by individual regime state rather than single aggregated average.",
        "enforcement": "HIGH_AUDIT",
    },
]


def build_regime_coverage_bias_control_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime coverage bias controls."""
    rows: List[Dict[str, Any]] = []
    for c in REGIME_CONTROLS:
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
        "domain": REGIME_COVERAGE_BIAS_DOMAIN,
        "total_controls": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
