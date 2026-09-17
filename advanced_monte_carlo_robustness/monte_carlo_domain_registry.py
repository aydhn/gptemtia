# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Domain Registry Module.

Registers all analytical domains covered under Monte Carlo robustness and parameter stability contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    MONTE_CARLO_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
    ROBUSTNESS_CONTRACT_DOMAIN,
    BOOTSTRAP_CONTRACT_DOMAIN,
    BLOCK_BOOTSTRAP_CONTRACT_DOMAIN,
    STATIONARY_BOOTSTRAP_CONTRACT_DOMAIN,
    RETURN_PATH_RESAMPLING_DOMAIN,
    TRADE_SEQUENCE_RESHUFFLING_DOMAIN,
    RESIDUAL_RESAMPLING_PLACEHOLDER_DOMAIN,
    NOISE_INJECTION_PLACEHOLDER_DOMAIN,
    PATH_PERTURBATION_PLACEHOLDER_DOMAIN,
    PARAMETER_STABILITY_CONTRACT_DOMAIN,
    PARAMETER_SENSITIVITY_CONTRACT_DOMAIN,
    PARAMETER_PERTURBATION_CONTRACT_DOMAIN,
    PARAMETER_GRID_STABILITY_PLACEHOLDER_DOMAIN,
    PARAMETER_SURFACE_PLACEHOLDER_DOMAIN,
    PARAMETER_FRAGILITY_PLACEHOLDER_DOMAIN,
    ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN,
    STABILITY_BAND_PLACEHOLDER_DOMAIN,
    CONFIDENCE_INTERVAL_PLACEHOLDER_DOMAIN,
    DISTRIBUTION_PLACEHOLDER_DOMAIN,
    LINKAGE_DOMAIN,
    OUTPUT_CONTRACT_DOMAIN,
    DEPENDENCY_DOMAIN,
    BIAS_GUARD_DOMAIN,
    DISABLED_EXECUTION_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_150_HANDOFF_DOMAIN,
)

DOMAINS: List[Dict[str, Any]] = [
    {"domain_name": ROBUSTNESS_CONTRACT_DOMAIN, "description": "Core Monte Carlo robustness contracts across resampling families."},
    {"domain_name": BOOTSTRAP_CONTRACT_DOMAIN, "description": "Basic and IID bootstrap simulation contracts without execution."},
    {"domain_name": BLOCK_BOOTSTRAP_CONTRACT_DOMAIN, "description": "Moving block and circular block bootstrap contracts preserving serial correlation."},
    {"domain_name": STATIONARY_BOOTSTRAP_CONTRACT_DOMAIN, "description": "Politis-Romano stationary bootstrap contracts with random block lengths."},
    {"domain_name": RETURN_PATH_RESAMPLING_DOMAIN, "description": "Return series resampling and reshuffling contracts."},
    {"domain_name": TRADE_SEQUENCE_RESHUFFLING_DOMAIN, "description": "Trade order permutation and sequence reshuffling contracts."},
    {"domain_name": RESIDUAL_RESAMPLING_PLACEHOLDER_DOMAIN, "description": "Model residual bootstrapping and innovation resampling placeholders."},
    {"domain_name": NOISE_INJECTION_PLACEHOLDER_DOMAIN, "description": "Market noise injection and spread jitter placeholders."},
    {"domain_name": PATH_PERTURBATION_PLACEHOLDER_DOMAIN, "description": "Synthetic path perturbation metadata placeholders."},
    {"domain_name": PARAMETER_STABILITY_CONTRACT_DOMAIN, "description": "Parameter stability contracts across strategy hyperparameter grids."},
    {"domain_name": PARAMETER_SENSITIVITY_CONTRACT_DOMAIN, "description": "First-order sensitivity and local elasticity contracts."},
    {"domain_name": PARAMETER_PERTURBATION_CONTRACT_DOMAIN, "description": "Parameter perturbation and neighbor stability contracts."},
    {"domain_name": PARAMETER_GRID_STABILITY_PLACEHOLDER_DOMAIN, "description": "Grid neighborhood stability score placeholders."},
    {"domain_name": PARAMETER_SURFACE_PLACEHOLDER_DOMAIN, "description": "Parameter surface topology: plateau vs peak evaluation placeholders."},
    {"domain_name": PARAMETER_FRAGILITY_PLACEHOLDER_DOMAIN, "description": "Parameter fragility flag and cliff-edge detection placeholders."},
    {"domain_name": ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN, "description": "Robustness envelope bounds (upper/lower/median) placeholders."},
    {"domain_name": STABILITY_BAND_PLACEHOLDER_DOMAIN, "description": "Strategy stability tolerance band placeholders."},
    {"domain_name": CONFIDENCE_INTERVAL_PLACEHOLDER_DOMAIN, "description": "Empirical confidence interval (5%, 50%, 95%) placeholders."},
    {"domain_name": DISTRIBUTION_PLACEHOLDER_DOMAIN, "description": "Drawdown, return, and tail-risk distribution placeholders."},
    {"domain_name": LINKAGE_DOMAIN, "description": "Linkages to scenario resampling, stress testing, and walk-forward frameworks."},
    {"domain_name": OUTPUT_CONTRACT_DOMAIN, "description": "Strict output contracts ensuring zero signals and zero live results."},
    {"domain_name": DEPENDENCY_DOMAIN, "description": "Dependencies on Phase 146 realistic backtest, Phase 147 walk-forward, and Phase 148 stress testing."},
    {"domain_name": BIAS_GUARD_DOMAIN, "description": "Guards against lookahead, resampling leakage, data snooping, and overfitting."},
    {"domain_name": DISABLED_EXECUTION_DOMAIN, "description": "Audit trails proving simulation, training, optimization, and live trading are disabled."},
    {"domain_name": FINDING_DOMAIN, "description": "Diagnostic findings registry and governance warnings."},
    {"domain_name": READINESS_SCORE_DOMAIN, "description": "Aggregate readiness score evaluating contract completeness."},
    {"domain_name": MANIFEST_DOMAIN, "description": "Master Phase 149 integrity and negative invariants manifest."},
    {"domain_name": HEALTH_DOMAIN, "description": "Environment, dependency, and storage health check."},
    {"domain_name": VALIDATION_DOMAIN, "description": "Multi-stage contract validation and compliance reporting."},
    {"domain_name": SAFETY_DOMAIN, "description": "Strict NO-GO and SAFE-GO boundary definitions."},
    {"domain_name": PHASE_150_HANDOFF_DOMAIN, "description": "Handoff bundle for Phase 150 Backtest Governance and Bias Control."},
]


def build_monte_carlo_domain_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the Monte Carlo domain registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for d in DOMAINS:
        rows.append(
            {
                "domain_name": d["domain_name"],
                "description": d["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": MONTE_CARLO_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": MONTE_CARLO_DOMAIN,
        "total_domains": len(df),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
