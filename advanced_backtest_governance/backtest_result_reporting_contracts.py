# -*- coding: utf-8 -*-
"""Phase 150: Backtest Result Reporting Contracts.

Defines reporting governance contracts ensuring results are treated as research
hypotheses with full disclosure, mandatory disclaimers, and zero performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    RESULT_REPORTING_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

REPORTING_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "hypothesis_treatment_contract",
        "description": "All backtest outputs must be explicitly labeled as unverified empirical hypotheses.",
        "requirement": "Preclude affirmative performance guarantees or forward efficacy assertions.",
    },
    {
        "contract_name": "mandatory_full_period_disclosure_contract",
        "description": "Mandatory disclosure of entire evaluated timeline including severe drawdown windows.",
        "requirement": "Prohibit truncation of unprofitable periods or selective date trimming.",
    },
    {
        "contract_name": "negative_performance_disclosure_contract",
        "description": "Exhaustive reporting of loss clusters, continuous losing streaks, and worst-case paths.",
        "requirement": "Highlight stress periods and parameter fragility alongside central tendencies.",
    },
    {
        "contract_name": "transaction_friction_breakdown_contract",
        "description": "Detailed line-item reporting of simulated fees, financing carry, and execution slippage.",
        "requirement": "Demonstrate net returns under zero-cost vs realistic cost models.",
    },
    {
        "contract_name": "benchmark_relative_disclosure_contract",
        "description": "Mandatory side-by-side comparison against pre-committed passive and cash baselines.",
        "requirement": "Forbid reporting strategy returns in isolation without standard benchmark context.",
    },
    {
        "contract_name": "uncalculated_metric_placeholder_contract",
        "description": "All numerical metric fields (Sharpe, win-rate, alpha) remain placeholders in Phase 150.",
        "requirement": "Block numerical performance calculation until formal validation in Phase 151-152.",
    },
]


def summarize_backtest_result_reporting_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize result reporting contracts."""
    return {
        "domain": RESULT_REPORTING_DOMAIN,
        "total_reporting_contracts": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "all_hypotheses_required": True,
        "all_claims_blocked": True,
        "zero_actual_metrics_calculated": True,
        "non_signal": True,
        "local_only": True,
    }


def build_backtest_result_reporting_contract_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for result reporting contracts."""
    rows: List[Dict[str, Any]] = []
    for r in REPORTING_CONTRACTS:
        rows.append({
            "contract_name": r["contract_name"],
            "description": r["description"],
            "requirement": r["requirement"],
            "actual_metrics_calculated": False,
            "performance_claim_allowed": False,
            "result_claim_allowed": False,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = summarize_backtest_result_reporting_contracts(df)
    return df, summary
