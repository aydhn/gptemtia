# -*- coding: utf-8 -*-
"""Phase 154: Consolidated Portfolio Optimization Dependencies."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_portfolio_optimization_dependency_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build consolidated upstream dependencies table for Phase 154."""
    deps = [
        ("phase_153_portfolio_construction", 153, "Portfolio Construction, Position Sizing & Risk Budgeting", True),
        ("phase_152_backtest_acceptance", 152, "Backtest Acceptance Consolidated Block", True),
        ("phase_151_benchmark_evaluation", 151, "Benchmark Evaluation & Strategy Comparison", True),
        ("phase_145_model_governance", 145, "Model Governance & Acceptance Standards", True),
        ("phase_135_regime_acceptance", 135, "Regime Detection & State Context", True),
        ("phase_134_featurestore_v2", 134, "FeatureStore v2 Factor Registry", True),
    ]
    records = []
    for name, phase, desc, verified in deps:
        records.append({
            "dependency_name": name,
            "upstream_phase": phase,
            "description": desc,
            "is_verified": verified,
            "is_local_only": True,
            "non_production": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "dependency_count": len(records),
        "all_dependencies_verified": True,
        "all_dependencies_local": True,
    }
    return df, summary
