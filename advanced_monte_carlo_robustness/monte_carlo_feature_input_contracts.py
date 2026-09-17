# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Feature Input Contracts Module.

Defines schemas and requirements for feature inputs from FeatureStore.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    OUTPUT_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

FEATURE_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "feature_contract_name": "regime_indicator_feature_contract",
        "feature_family": "regime_classification",
        "source_registry": "Phase 135 Regime Acceptance Feature Store",
        "leakage_guard": "AS_OF_TIMESTAMP_ONLY",
        "description": "Historical market regime indicators conditioning stratified block bootstrap sampling.",
    },
    {
        "feature_contract_name": "volatility_cluster_feature_contract",
        "feature_family": "realized_volatility",
        "source_registry": "Phase 134 Feature Store",
        "leakage_guard": "LAGGED_VOLATILITY_ONLY",
        "description": "Historical realized volatility series used to stratify volatility regimes.",
    },
]


def build_monte_carlo_feature_input_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the Monte Carlo feature input contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for f in FEATURE_INPUT_CONTRACTS:
        rows.append(
            {
                "feature_contract_name": f["feature_contract_name"],
                "feature_family": f["feature_family"],
                "source_registry": f["source_registry"],
                "leakage_guard": f["leakage_guard"],
                "description": f["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": OUTPUT_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": OUTPUT_CONTRACT_DOMAIN,
        "total_feature_input_contracts": len(df),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
