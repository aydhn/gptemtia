# -*- coding: utf-8 -*-
"""Phase 149: Noise Injection Placeholders Module.

Defines placeholders for synthetic market noise, quote jitter, and spread fuzzing
to test execution robustness without injecting actual data distortions.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    NOISE_INJECTION_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

NOISE_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "noise_type": "gaussian_quote_jitter",
        "noise_distribution": "N(0, sigma_microstructure^2)",
        "target_variable": "bid_ask_midpoint",
        "perturbation_magnitude": "0.5 * half_spread",
        "description": "Contracts adding zero-mean microstructure quote jitter to verify entry/exit threshold stability.",
    },
    {
        "noise_type": "laplace_spread_fuzzing",
        "noise_distribution": "Laplace(0, b_spread)",
        "target_variable": "effective_spread",
        "perturbation_magnitude": "1.0 * current_spread",
        "description": "Heavy-tailed noise added to instantaneous bid-ask spreads to model intraday liquidity evaporation.",
    },
    {
        "noise_type": "volume_stochastic_scaling",
        "noise_distribution": "LogNormal(0, 0.25)",
        "target_variable": "bar_volume",
        "perturbation_magnitude": "+/- 25% volume variance",
        "description": "Multiplicative stochastic volume scaling to evaluate participation rate sensitivity.",
    },
]


def build_noise_injection_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the noise injection placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for p in NOISE_PLACEHOLDERS:
        rows.append(
            {
                "noise_type": p["noise_type"],
                "noise_distribution": p["noise_distribution"],
                "target_variable": p["target_variable"],
                "perturbation_magnitude": p["perturbation_magnitude"],
                "description": p["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "noise_injected": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": NOISE_INJECTION_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": NOISE_INJECTION_PLACEHOLDER_DOMAIN,
        "total_placeholders": len(df),
        "all_unexecuted": bool((~df["noise_injected"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
