# -*- coding: utf-8 -*-
"""Phase 150: Backtest Manual Review Gates.

Defines the 10 mandatory human review checkpoints before strategy evaluation progression.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    MANUAL_REVIEW_GATE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

REVIEW_GATES: List[Dict[str, Any]] = [
    {
        "gate_name": "realistic_backtest_contract_review_gate",
        "description": "Human inspection verifying that realistic backtest contracts from Phase 146 are appropriately linked.",
        "focus_area": "realistic_backtest_contract",
    },
    {
        "gate_name": "transaction_cost_realism_review_gate",
        "description": "Human inspection verifying non-zero commission tiers and regulatory fees.",
        "focus_area": "transaction_cost_realism",
    },
    {
        "gate_name": "slippage_realism_review_gate",
        "description": "Human inspection verifying non-linear market impact and spread-widening factors.",
        "focus_area": "slippage_realism",
    },
    {
        "gate_name": "walk_forward_oos_review_gate",
        "description": "Human inspection checking purge/embargo boundaries and single-pass OOS quarantine.",
        "focus_area": "walk_forward_oos",
    },
    {
        "gate_name": "benchmark_selection_review_gate",
        "description": "Human inspection verifying neutral benchmark pre-commitment and absence of cherry-picking.",
        "focus_area": "benchmark_selection",
    },
    {
        "gate_name": "stress_scenario_review_gate",
        "description": "Human inspection verifying inclusion of historical and synthetic stress shocks.",
        "focus_area": "stress_scenario",
    },
    {
        "gate_name": "monte_carlo_robustness_review_gate",
        "description": "Human inspection checking bootstrap resampling and path reshuffling coverage.",
        "focus_area": "monte_carlo_robustness",
    },
    {
        "gate_name": "parameter_stability_review_gate",
        "description": "Human inspection confirming plateau stability and absence of cliff effects.",
        "focus_area": "parameter_stability",
    },
    {
        "gate_name": "result_claim_review_gate",
        "description": "Human inspection guaranteeing that results are presented as empirical hypotheses, not proven returns.",
        "focus_area": "result_claim",
    },
    {
        "gate_name": "performance_claim_review_gate",
        "description": "Human inspection guaranteeing zero production-ready or broker-ready approval assertions.",
        "focus_area": "performance_claim",
    },
]


def build_backtest_manual_review_gate_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for manual review gates."""
    rows: List[Dict[str, Any]] = []
    for g in REVIEW_GATES:
        rows.append({
            "gate_name": g["gate_name"],
            "description": g["description"],
            "focus_area": g["focus_area"],
            "requires_human_signoff": True,
            "auto_pass_prohibited": True,
            "status": "PENDING_MANUAL_REVIEW",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": MANUAL_REVIEW_GATE_DOMAIN,
        "total_gates": len(df),
        "all_require_human_signoff": True,
        "auto_pass_strictly_prohibited": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
