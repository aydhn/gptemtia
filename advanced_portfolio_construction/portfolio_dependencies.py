# -*- coding: utf-8 -*-
"""Phase 153: Consolidated Portfolio Dependencies."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    DEPENDENCY_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)
from .portfolio_backtest_acceptance_dependencies import build_portfolio_backtest_acceptance_dependency_registry
from .portfolio_benchmark_evaluation_dependencies import build_portfolio_benchmark_evaluation_dependency_registry
from .portfolio_model_governance_dependencies import build_portfolio_model_governance_dependency_registry
from .portfolio_regime_dependencies import build_portfolio_regime_dependency_registry
from .portfolio_featurestore_dependencies import build_portfolio_featurestore_dependency_registry


def build_portfolio_dependency_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Consolidate all upstream dependency registries into a single master registry."""
    df_btest, _ = build_portfolio_backtest_acceptance_dependency_registry(profile)
    df_bench, _ = build_portfolio_benchmark_evaluation_dependency_registry(profile)
    df_gov, _ = build_portfolio_model_governance_dependency_registry(profile)
    df_regime, _ = build_portfolio_regime_dependency_registry(profile)
    df_fs, _ = build_portfolio_featurestore_dependency_registry(profile)

    combined_df = pd.concat([df_btest, df_bench, df_gov, df_regime, df_fs], ignore_index=True)

    summary = {
        "domain": DEPENDENCY_DOMAIN,
        "active_profile": profile.profile_name,
        "total_dependencies": len(combined_df),
        "satisfied_dependencies": int((combined_df["status"] == "SATISFIED").sum()),
        "all_satisfied": bool((combined_df["status"] == "SATISFIED").all()),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return combined_df, summary
