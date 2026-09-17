# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Scope Registry.

Catalogs the scope boundaries (included vs excluded) of the backtest governance layer.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    BACKTEST_GOVERNANCE_SCOPE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

SCOPES: List[Dict[str, Any]] = [
    {"scope_name": "offline_governance_contracts", "scope_type": "INCLUDED", "description": "Defining formal contracts for realistic backtest execution without running actual trades."},
    {"scope_name": "bias_detection_policies", "scope_type": "INCLUDED", "description": "Detecting lookahead, survivorship, snooping, overfitting, multiple testing, and coverage bias."},
    {"scope_name": "result_claim_boundaries", "scope_type": "INCLUDED", "description": "Explicit boundaries ensuring results are treated as research hypotheses, never verified returns."},
    {"scope_name": "metric_claim_boundaries", "scope_type": "INCLUDED", "description": "Explicit boundaries ensuring Sharpe, win-rate, and alpha are contract placeholders."},
    {"scope_name": "realism_governance", "scope_type": "INCLUDED", "description": "Validating cost, slippage, fill, and liquidity realism assumptions."},
    {"scope_name": "audit_and_evidence", "scope_type": "INCLUDED", "description": "Logging and evidence preservation standards for reproducibility."},
    {"scope_name": "manual_review_gates", "scope_type": "INCLUDED", "description": "Human review checkpoints before strategy evaluation progression."},
    {"scope_name": "phase_151_handoff", "scope_type": "INCLUDED", "description": "Preparing input contracts for Phase 151 benchmark comparison."},
    {"scope_name": "live_trading", "scope_type": "EXCLUDED", "description": "Live order execution, routing, or account integration."},
    {"scope_name": "broker_integration", "scope_type": "EXCLUDED", "description": "Interactive Brokers, MT5, or broker API interactions."},
    {"scope_name": "signal_generation", "scope_type": "EXCLUDED", "description": "Producing buy/sell/position trading recommendations."},
    {"scope_name": "real_backtest_execution", "scope_type": "EXCLUDED", "description": "Running backtest simulation engine on historical bars."},
    {"scope_name": "real_metric_calculation", "scope_type": "EXCLUDED", "description": "Calculating actual numerical performance metrics."},
    {"scope_name": "strategy_optimization", "scope_type": "EXCLUDED", "description": "Running grid/random/Bayesian parameter optimizers."},
    {"scope_name": "strategy_approval", "scope_type": "EXCLUDED", "description": "Issuing production-ready or official approval claims."},
    {"scope_name": "model_training", "scope_type": "EXCLUDED", "description": "Fitting ML/DL models or generating inference predictions."},
]


def summarize_backtest_governance_scopes(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance scopes."""
    included = len(df[df["scope_type"] == "INCLUDED"])
    excluded = len(df[df["scope_type"] == "EXCLUDED"])
    return {
        "domain": BACKTEST_GOVERNANCE_SCOPE_DOMAIN,
        "total_scopes": len(df),
        "included_scopes_count": included,
        "excluded_scopes_count": excluded,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }


def build_backtest_governance_scope_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for backtest governance scopes."""
    rows: List[Dict[str, Any]] = []
    for s in SCOPES:
        rows.append({
            "scope_name": s["scope_name"],
            "scope_type": s["scope_type"],
            "description": s["description"],
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = summarize_backtest_governance_scopes(df)
    return df, summary
