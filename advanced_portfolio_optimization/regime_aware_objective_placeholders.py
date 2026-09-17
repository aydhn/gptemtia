# -*- coding: utf-8 -*-
"""Phase 154: Regime-Aware Objective Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_regime_aware_objective_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build regime-aware objective placeholder registry."""
    records = [{
        "objective_name": "regime_aware_objective",
        "regime_state_ref": "regime_state_context_v135",
        "regime_covariance_ref": "regime_conditioned_covariance_stub",
        "is_placeholder": True,
        "actual_objective_calculated": None,
        "is_calculated": False,
        "actual_weights_generated": False,
        "status": "objective_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "objective_name": "regime_aware_objective",
        "is_placeholder": True,
        "is_calculated": False,
        "actual_weights_generated": False,
    }
    return df, summary
