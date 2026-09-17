# -*- coding: utf-8 -*-
"""Phase 155: Master Risk Reporting Dependencies Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


DEFAULT_DEPENDENCIES = [
    {"source_phase": 154, "source_component": "advanced_portfolio_optimization", "dependency_name": "portfolio_optimization_contracts", "status": "AVAILABLE_CONTRACT_ONLY"},
    {"source_phase": 153, "source_component": "advanced_portfolio_construction", "dependency_name": "portfolio_construction_contracts", "status": "AVAILABLE_CONTRACT_ONLY"},
    {"source_phase": 152, "source_component": "advanced_backtest_acceptance", "dependency_name": "backtest_acceptance_report", "status": "AVAILABLE_CONTRACT_ONLY"},
    {"source_phase": 151, "source_component": "advanced_benchmark_evaluation", "dependency_name": "benchmark_evaluation_contracts", "status": "AVAILABLE_CONTRACT_ONLY"},
    {"source_phase": 150, "source_component": "advanced_backtest_governance", "dependency_name": "backtest_governance_registry", "status": "AVAILABLE_CONTRACT_ONLY"},
    {"source_phase": 149, "source_component": "advanced_monte_carlo_robustness", "dependency_name": "monte_carlo_robustness_contracts", "status": "AVAILABLE_CONTRACT_ONLY"},
    {"source_phase": 148, "source_component": "advanced_stress_testing", "dependency_name": "stress_testing_contracts", "status": "AVAILABLE_CONTRACT_ONLY"},
    {"source_phase": 147, "source_component": "advanced_walk_forward_validation", "dependency_name": "walk_forward_contracts", "status": "AVAILABLE_CONTRACT_ONLY"},
    {"source_phase": 146, "source_component": "advanced_realistic_backtest", "dependency_name": "realistic_backtest_contracts", "status": "AVAILABLE_CONTRACT_ONLY"},
    {"source_phase": 145, "source_component": "advanced_ml_acceptance", "dependency_name": "ml_acceptance_report", "status": "AVAILABLE_CONTRACT_ONLY"},
    {"source_phase": 144, "source_component": "advanced_model_governance", "dependency_name": "model_cards_and_audit", "status": "AVAILABLE_CONTRACT_ONLY"},
    {"source_phase": 135, "source_component": "advanced_regime_acceptance", "dependency_name": "regime_classification_catalog", "status": "AVAILABLE_METADATA_ONLY"},
    {"source_phase": 134, "source_component": "advanced_feature_store_integration", "dependency_name": "featurestore_metadata", "status": "AVAILABLE_METADATA_ONLY"},
]


def build_risk_reporting_dependency_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary of upstream dependencies."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for d in DEFAULT_DEPENDENCIES:
        item = dict(d)
        item["current_phase"] = profile.current_phase
        item["target_final_phase"] = profile.target_final_phase
        item["next_phase"] = profile.next_phase
        rows.append(item)

    df = pd.DataFrame(rows)
    summary = {
        "dependency_count": len(df),
        "total_dependencies": len(df),
        "all_available": True,
        "is_safe": True,
    }
    return df, summary
