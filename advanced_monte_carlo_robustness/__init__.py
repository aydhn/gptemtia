# -*- coding: utf-8 -*-
"""Phase 149: Advanced Monte Carlo Robustness and Parameter Stability Contract Layer.

Provides local/offline research contracts, bootstrap simulation definitions,
return path resampling schemas, trade sequence reshuffling contracts,
parameter stability and sensitivity specifications, robustness envelopes,
bias guards, disabled execution enforcement, and Phase 150 handoff readiness.
Strictly non-signal, non-production, zero-live-trading, zero-execution layer.
"""

__version__ = "1.0.0"
__phase__ = 149
__target_final_phase__ = 160
__next_phase__ = 150

from advanced_monte_carlo_robustness.monte_carlo_config import (
    MonteCarloProfile,
    get_monte_carlo_profile,
    list_monte_carlo_profiles,
    validate_monte_carlo_profiles,
    get_default_monte_carlo_profile,
)
from advanced_monte_carlo_robustness.monte_carlo_pipeline import MonteCarloRobustnessPipeline
from advanced_monte_carlo_robustness.monte_carlo_health import build_monte_carlo_health_check, check_monte_carlo_health
from advanced_monte_carlo_robustness.monte_carlo_validation import build_monte_carlo_validation_report, validate_monte_carlo
from advanced_monte_carlo_robustness.monte_carlo_safety_boundary import build_monte_carlo_safety_boundary, enforce_monte_carlo_safety_boundary
from advanced_monte_carlo_robustness.phase_150_handoff import build_phase_150_backtest_governance_bias_control_handoff_report

__all__ = [
    "MonteCarloProfile",
    "get_monte_carlo_profile",
    "list_monte_carlo_profiles",
    "validate_monte_carlo_profiles",
    "get_default_monte_carlo_profile",
    "MonteCarloRobustnessPipeline",
    "build_monte_carlo_health_check",
    "check_monte_carlo_health",
    "build_monte_carlo_validation_report",
    "validate_monte_carlo",
    "build_monte_carlo_safety_boundary",
    "enforce_monte_carlo_safety_boundary",
    "build_phase_150_backtest_governance_bias_control_handoff_report",
]

