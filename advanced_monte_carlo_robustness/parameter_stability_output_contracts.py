# -*- coding: utf-8 -*-
"""Phase 149: Parameter Stability Output Contracts Module.

Defines schemas for parameter stability summary outputs: formula metadata,
neighborhood specifications, and fragility flag definitions without calculated values.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    OUTPUT_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

STABILITY_OUTPUTS: List[Dict[str, Any]] = [
    {
        "output_type": "parameter_stability_metadata_output",
        "allowed_payload": "contract_validation_status, parameter_name, perturbation_range, plateau_detection_rule, manual_review_required",
        "prohibited_payload": "actual_parameter_stability_score, optimized_parameter, best_parameter, heatmap_matrix",
        "status": MONTE_CARLO_CONTRACT_READY,
    },
    {
        "output_type": "parameter_fragility_flag_output",
        "allowed_payload": "flag_id, detection_rule, severity_level, status",
        "prohibited_payload": "trade_recommendation, position_scale_factor, execution_action",
        "status": MONTE_CARLO_CONTRACT_READY,
    },
]


def build_parameter_stability_output_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the parameter stability output contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for s in STABILITY_OUTPUTS:
        rows.append(
            {
                "output_type": s["output_type"],
                "allowed_payload": s["allowed_payload"],
                "prohibited_payload": s["prohibited_payload"],
                "status": s["status"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "domain": OUTPUT_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": OUTPUT_CONTRACT_DOMAIN,
        "total_stability_output_contracts": len(df),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
