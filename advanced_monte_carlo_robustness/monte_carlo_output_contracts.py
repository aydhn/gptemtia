# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Output Contracts Module.

Defines strict schema contracts for Phase 149 outputs. Prohibits actual simulation results,
live signals, VaR/ES metrics, or trading recommendations from being emitted.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    OUTPUT_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

OUTPUT_SPECS: List[Dict[str, Any]] = [
    {
        "output_schema_name": "monte_carlo_contract_validation_output",
        "permitted_fields": "contract_validation_status, blocked_reason, manual_review_required, current_phase, next_phase",
        "prohibited_fields": "monte_carlo_return, actual_var, simulation_path, pnl_distribution, trade_signal",
        "zero_signals_mandated": True,
        "description": "Standard output contract returning only contract validation status and safety boundaries.",
    },
    {
        "output_schema_name": "monte_carlo_readiness_output",
        "permitted_fields": "readiness_score, classification, passed_checks, total_checks, manual_review_required",
        "prohibited_fields": "production_approval, broker_ready, live_trading_ready, performance_guarantee",
        "zero_signals_mandated": True,
        "description": "Readiness scoring output strictly categorized as non-production research diagnostic.",
    },
]


def build_monte_carlo_output_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the Monte Carlo output contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for s in OUTPUT_SPECS:
        rows.append(
            {
                "output_schema_name": s["output_schema_name"],
                "permitted_fields": s["permitted_fields"],
                "prohibited_fields": s["prohibited_fields"],
                "zero_signals_mandated": s["zero_signals_mandated"],
                "description": s["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": OUTPUT_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": OUTPUT_CONTRACT_DOMAIN,
        "total_output_contracts": len(df),
        "zero_signals_enforced": bool(df["zero_signals_mandated"].all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
