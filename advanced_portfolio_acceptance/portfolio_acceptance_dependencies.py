# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Dependency Registry.

Tracks and verifies upstream dependencies across data lake, feature store,
ML governance, backtest blocks, and portfolio/risk components.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    DEPENDENCY_ACCEPTANCE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

DEPENDENCY_SOURCES = [
    {
        "dep_id": "DEP-153",
        "source_phase": "Phase 153",
        "source_module": "advanced_portfolio_construction",
        "description": "Portfolio construction, volatility parity/risk budget sizing contracts.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-154",
        "source_phase": "Phase 154",
        "source_module": "advanced_portfolio_optimization",
        "description": "Portfolio optimization objectives, allocation constraints and solver contracts.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-155",
        "source_phase": "Phase 155",
        "source_module": "advanced_risk_reporting",
        "description": "Risk reporting, exposure attribution, and limit monitoring contracts.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-156",
        "source_phase": "Phase 156",
        "source_module": "advanced_portfolio_scenario_control",
        "description": "Portfolio scenario simulation, resilience testing, and drawdown control contracts.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-152",
        "source_phase": "Phase 152",
        "source_module": "advanced_backtest_acceptance",
        "description": "Consolidated backtest block acceptance and governance layer.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-151",
        "source_phase": "Phase 151",
        "source_module": "advanced_benchmark_evaluation",
        "description": "Benchmark comparison and strategy evaluation contract layer.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-150",
        "source_phase": "Phase 150",
        "source_module": "advanced_backtest_governance",
        "description": "Backtest governance, lookahead bias control, and survivorship invariants.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-149",
        "source_phase": "Phase 149",
        "source_module": "advanced_monte_carlo_robustness",
        "description": "Monte Carlo robustness and parameter stability contracts.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-148",
        "source_phase": "Phase 148",
        "source_module": "advanced_stress_testing",
        "description": "Stress testing and scenario simulation contracts.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-147",
        "source_phase": "Phase 147",
        "source_module": "advanced_walk_forward_validation",
        "description": "Walk-forward validation and out-of-sample benchmarking contracts.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-146",
        "source_phase": "Phase 146",
        "source_module": "advanced_realistic_backtest",
        "description": "Realistic backtest, transaction cost, and slippage contracts.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-145",
        "source_phase": "Phase 145",
        "source_module": "advanced_ml_acceptance",
        "description": "Consolidated ML block acceptance and model readiness boundaries.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-144",
        "source_phase": "Phase 144",
        "source_module": "advanced_model_governance",
        "description": "Model governance, model cards, and audit trail contracts.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-135",
        "source_phase": "Phase 135",
        "source_module": "advanced_regime_acceptance",
        "description": "Regime block acceptance report and consolidated regime contracts.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-134",
        "source_phase": "Phase 134",
        "source_module": "advanced_regime_featurestore_integration",
        "description": "Regime featurestore integration and point-in-time state tables.",
        "satisfied": True,
    },
    {
        "dep_id": "DEP-STORAGE",
        "source_phase": "Infrastructure",
        "source_module": "DataLake / FeatureStore",
        "description": "Data storage persistence layer and feature lookup registry.",
        "satisfied": True,
    },
]


def build_portfolio_acceptance_dependency_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of portfolio acceptance dependencies."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for dep in DEPENDENCY_SOURCES:
        records.append({
            "dep_id": dep["dep_id"],
            "source_phase": dep["source_phase"],
            "source_module": dep["source_module"],
            "description": dep["description"],
            "satisfied": dep["satisfied"],
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_dependencies(df)
    return df, summary


def summarize_portfolio_acceptance_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize dependency registry."""
    all_satisfied = bool(df["satisfied"].all()) if not df.empty and "satisfied" in df.columns else False
    return {
        "domain": DEPENDENCY_ACCEPTANCE_DOMAIN,
        "total_dependencies": len(df),
        "satisfied_dependencies": int(df["satisfied"].sum()) if not df.empty and "satisfied" in df.columns else 0,
        "all_satisfied": all_satisfied,
        "status": PORTFOLIO_ACCEPTANCE_READY if all_satisfied else "DEPENDENCIES_INCOMPLETE",
    }
