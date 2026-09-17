# -*- coding: utf-8 -*-
"""Phase 158: System Component Dependencies.

Builds dependency graph metadata representing system-wide architectural flow:
DataLake -> FeatureStore -> Feature/Factor -> Regime -> ML Governance -> Backtest Acceptance -> Portfolio Acceptance -> Full-System Integration.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


DEPENDENCY_GRAPH = [
    ("DEP-001", "data_lake", "storage", "core_runtime", "runtime", "HARD", "VERIFIED"),
    ("DEP-002", "feature_store", "storage", "data_lake", "storage", "HARD", "VERIFIED"),
    ("DEP-003", "data_provider_contracts", "data", "data_lake", "storage", "HARD", "VERIFIED"),
    ("DEP-004", "macro_calendar_contracts", "data", "data_lake", "storage", "HARD", "VERIFIED"),
    ("DEP-005", "news_metadata_contracts", "data", "data_lake", "storage", "HARD", "VERIFIED"),
    ("DEP-006", "indicator_engine", "features", "data_lake", "storage", "HARD", "VERIFIED"),
    ("DEP-007", "feature_factor_engine", "features", "feature_store", "storage", "HARD", "VERIFIED"),
    ("DEP-008", "regime_engine", "regime", "feature_factor_engine", "features", "HARD", "VERIFIED"),
    ("DEP-009", "ml_dataset_registry", "ml", "regime_engine", "regime", "HARD", "VERIFIED"),
    ("DEP-010", "gpu_runtime_governance", "ml", "ml_dataset_registry", "ml", "SOFT", "VERIFIED"),
    ("DEP-011", "baseline_ml_models", "ml", "ml_dataset_registry", "ml", "HARD", "VERIFIED"),
    ("DEP-012", "ensemble_model_registry", "ml", "baseline_ml_models", "ml", "HARD", "VERIFIED"),
    ("DEP-013", "calibration_uncertainty", "ml", "ensemble_model_registry", "ml", "HARD", "VERIFIED"),
    ("DEP-014", "model_drift_monitoring", "ml", "calibration_uncertainty", "ml", "HARD", "VERIFIED"),
    ("DEP-015", "explainability_attribution", "ml", "model_drift_monitoring", "ml", "HARD", "VERIFIED"),
    ("DEP-016", "model_governance", "ml", "explainability_attribution", "ml", "HARD", "VERIFIED"),
    ("DEP-017", "ml_acceptance", "ml", "model_governance", "ml", "HARD", "VERIFIED"),
    ("DEP-018", "realistic_backtest", "backtest", "ml_acceptance", "ml", "HARD", "VERIFIED"),
    ("DEP-019", "walk_forward_oos", "backtest", "realistic_backtest", "backtest", "HARD", "VERIFIED"),
    ("DEP-020", "stress_testing", "backtest", "walk_forward_oos", "backtest", "HARD", "VERIFIED"),
    ("DEP-021", "monte_carlo_robustness", "backtest", "stress_testing", "backtest", "HARD", "VERIFIED"),
    ("DEP-022", "backtest_governance", "backtest", "monte_carlo_robustness", "backtest", "HARD", "VERIFIED"),
    ("DEP-023", "benchmark_evaluation", "backtest", "backtest_governance", "backtest", "HARD", "VERIFIED"),
    ("DEP-024", "backtest_acceptance", "backtest", "benchmark_evaluation", "backtest", "HARD", "VERIFIED"),
    ("DEP-025", "portfolio_construction", "portfolio", "backtest_acceptance", "backtest", "HARD", "VERIFIED"),
    ("DEP-026", "portfolio_optimization", "portfolio", "portfolio_construction", "portfolio", "HARD", "VERIFIED"),
    ("DEP-027", "risk_reporting", "portfolio", "portfolio_optimization", "portfolio", "HARD", "VERIFIED"),
    ("DEP-028", "portfolio_scenario_control", "portfolio", "risk_reporting", "portfolio", "HARD", "VERIFIED"),
    ("DEP-029", "portfolio_acceptance", "portfolio", "portfolio_scenario_control", "portfolio", "HARD", "VERIFIED"),
    ("DEP-030", "reporting_layer", "reporting", "portfolio_acceptance", "portfolio", "HARD", "VERIFIED"),
    ("DEP-031", "safety_boundaries", "governance", "reporting_layer", "reporting", "HARD", "VERIFIED"),
    ("DEP-032", "full_system_integration", "integration", "portfolio_acceptance", "portfolio", "HARD", "VERIFIED"),
]


def build_system_component_dependency_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system component dependency registry DataFrame and summary."""
    records = []
    for dep_id, src, src_lyr, tgt, tgt_lyr, dep_type, status in DEPENDENCY_GRAPH:
        records.append({
            "dependency_id": dep_id,
            "source_component": src,
            "source_layer": src_lyr,
            "target_component": tgt,
            "target_layer": tgt_lyr,
            "dependency_type": dep_type,
            "status": status,
            "contract_only": True,
            "non_production": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "active_profile": profile.profile_name,
        "total_dependencies": len(df),
        "hard_dependencies": int((df["dependency_type"] == "HARD").sum()),
        "soft_dependencies": int((df["dependency_type"] == "SOFT").sum()),
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
