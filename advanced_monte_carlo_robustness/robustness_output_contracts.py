# -*- coding: utf-8 -*-
"""Phase 149: Robustness Output Contracts Module.

Defines schemas for robustness envelope outputs: bounds, formulas, metadata only.
Zero actual robustness scores or distribution values permitted.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    OUTPUT_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

ROBUSTNESS_OUTPUTS: List[Dict[str, Any]] = [
    {
        "output_type": "robustness_envelope_metadata_output",
        "allowed_payload": "contract_validation_status, envelope_bounds_defined, formula_reference, manual_review_required",
        "prohibited_payload": "actual_envelope_points, terminal_wealth_array, drawdown_distribution_values",
        "status": MONTE_CARLO_CONTRACT_READY,
    },
    {
        "output_type": "tail_risk_formula_metadata_output",
        "allowed_payload": "confidence_level, formula_specification, estimation_method, status",
        "prohibited_payload": "actual_var_value, actual_cvar_value, loss_distribution_points",
        "status": MONTE_CARLO_CONTRACT_READY,
    },
]


def build_robustness_output_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the robustness output contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for r in ROBUSTNESS_OUTPUTS:
        rows.append(
            {
                "output_type": r["output_type"],
                "allowed_payload": r["allowed_payload"],
                "prohibited_payload": r["prohibited_payload"],
                "status": r["status"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "domain": OUTPUT_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": OUTPUT_CONTRACT_DOMAIN,
        "total_robustness_output_contracts": len(df),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
