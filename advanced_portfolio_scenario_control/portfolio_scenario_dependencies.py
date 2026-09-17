# -*- coding: utf-8 -*-
"""Phase 156: Master Portfolio Scenario Dependencies."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_DEPENDENCIES = [
    {"dep_id": "DEP-156-001", "source_phase": 155, "source_module": "advanced_risk_reporting", "target_artifact": "risk_report_contracts", "status": "SATISFIED"},
    {"dep_id": "DEP-156-002", "source_phase": 154, "source_module": "advanced_portfolio_optimization", "target_artifact": "portfolio_optimization_contracts", "status": "SATISFIED"},
    {"dep_id": "DEP-156-003", "source_phase": 153, "source_module": "advanced_portfolio_construction", "target_artifact": "portfolio_construction_contracts", "status": "SATISFIED"},
    {"dep_id": "DEP-156-004", "source_phase": 152, "source_module": "advanced_backtest_acceptance", "target_artifact": "backtest_acceptance_manifest", "status": "SATISFIED"},
    {"dep_id": "DEP-156-005", "source_phase": 148, "source_module": "advanced_stress_testing", "target_artifact": "stress_testing_manifest", "status": "SATISFIED"},
    {"dep_id": "DEP-156-006", "source_phase": 149, "source_module": "advanced_monte_carlo_robustness", "target_artifact": "monte_carlo_manifest", "status": "SATISFIED"},
    {"dep_id": "DEP-156-007", "source_phase": 144, "source_module": "advanced_model_governance", "target_artifact": "governance_manifest", "status": "SATISFIED"},
    {"dep_id": "DEP-156-008", "source_phase": 135, "source_module": "advanced_regime_acceptance", "target_artifact": "regime_acceptance_manifest", "status": "SATISFIED"},
    {"dep_id": "DEP-156-009", "source_phase": 108, "source_module": "ml.feature_store", "target_artifact": "feature_store_client", "status": "SATISFIED"},
]


def build_portfolio_scenario_dependency_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    df = pd.DataFrame(DEFAULT_DEPENDENCIES)
    summary = {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
