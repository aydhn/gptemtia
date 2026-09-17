# -*- coding: utf-8 -*-
"""Phase 158: System Component Registry.

Registers all core architectural components from Phase 1 to Phase 157.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemComponentItem

COMPONENTS_DATA = [
    ("CMP-001", "core_runtime", "runtime", "main", "ready"),
    ("CMP-002", "config_paths_settings", "foundation", "config", "ready"),
    ("CMP-003", "data_lake", "storage", "data.storage.data_lake", "ready"),
    ("CMP-004", "feature_store", "storage", "ml.feature_store", "ready"),
    ("CMP-005", "data_provider_contracts", "data", "advanced_data_providers", "ready"),
    ("CMP-006", "macro_calendar_contracts", "data", "advanced_economic_calendar", "ready"),
    ("CMP-007", "news_metadata_contracts", "data", "advanced_news_sentiment_metadata", "ready"),
    ("CMP-008", "indicator_engine", "features", "indicators", "ready"),
    ("CMP-009", "feature_factor_engine", "features", "advanced_feature_factor_acceptance", "ready"),
    ("CMP-010", "regime_engine", "regime", "advanced_regime_acceptance", "ready"),
    ("CMP-011", "ml_dataset_registry", "ml", "advanced_ml_dataset_registry", "ready"),
    ("CMP-012", "gpu_runtime_governance", "ml", "advanced_gpu_ml_runtime", "ready"),
    ("CMP-013", "baseline_ml_models", "ml", "advanced_baseline_ml_models", "ready"),
    ("CMP-014", "ensemble_model_registry", "ml", "advanced_ensemble_model_registry", "ready"),
    ("CMP-015", "calibration_uncertainty", "ml", "advanced_calibration_uncertainty", "ready"),
    ("CMP-016", "model_drift_monitoring", "ml", "advanced_model_drift_monitoring", "ready"),
    ("CMP-017", "explainability_attribution", "ml", "advanced_explainability_attribution", "ready"),
    ("CMP-018", "model_governance", "ml", "advanced_model_governance", "ready"),
    ("CMP-019", "ml_acceptance", "ml", "advanced_ml_acceptance", "ready"),
    ("CMP-020", "realistic_backtest", "backtest", "advanced_realistic_backtest", "ready"),
    ("CMP-021", "walk_forward_oos", "backtest", "advanced_walk_forward_validation", "ready"),
    ("CMP-022", "stress_testing", "backtest", "advanced_stress_testing", "ready"),
    ("CMP-023", "monte_carlo_robustness", "backtest", "advanced_monte_carlo_robustness", "ready"),
    ("CMP-024", "backtest_governance", "backtest", "advanced_backtest_governance", "ready"),
    ("CMP-025", "benchmark_evaluation", "backtest", "advanced_benchmark_evaluation", "ready"),
    ("CMP-026", "backtest_acceptance", "backtest", "advanced_backtest_acceptance", "ready"),
    ("CMP-027", "portfolio_construction", "portfolio", "advanced_portfolio_construction", "ready"),
    ("CMP-028", "portfolio_optimization", "portfolio", "advanced_portfolio_optimization", "ready"),
    ("CMP-029", "risk_reporting", "portfolio", "advanced_risk_reporting", "ready"),
    ("CMP-030", "portfolio_scenario_control", "portfolio", "advanced_portfolio_scenario_control", "ready"),
    ("CMP-031", "portfolio_acceptance", "portfolio", "advanced_portfolio_acceptance", "ready"),
    ("CMP-032", "reporting_layer", "reporting", "reports", "ready"),
    ("CMP-033", "telegram_interface_placeholder", "interface", "interfaces.telegram_placeholder", "ready"),
    ("CMP-034", "local_paper_trading_placeholder", "interface", "interfaces.paper_placeholder", "ready"),
    ("CMP-035", "operator_docs", "documentation", "docs", "ready"),
    ("CMP-036", "safety_boundaries", "governance", "safety", "ready"),
]


def build_system_component_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system component registry DataFrame and summary."""
    items = []
    for cid, cname, layer, mod, status in COMPONENTS_DATA:
        item = SystemComponentItem(
            component_id=cid,
            component_name=cname,
            layer_name=layer,
            module_name=mod,
            status=status,
            contract_only=True,
            non_production=True,
            dry_run=True,
            local_only=True,
            production_ready=False,
            broker_ready=False,
            live_ready=False,
            signal_ready=False,
            system_executed=False,
        )
        items.append(item.__dict__)

    df = pd.DataFrame(items)
    summary = summarize_system_components(df, profile)
    return df, summary


def summarize_system_components(
    df: pd.DataFrame, profile: FullSystemIntegrationProfile | None = None
) -> Dict[str, Any]:
    """Summarize system components DataFrame."""
    return {
        "total_components": len(df),
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "all_production_ready_false": not bool(df["production_ready"].any()) if not df.empty else True,
        "all_broker_ready_false": not bool(df["broker_ready"].any()) if not df.empty else True,
        "all_live_ready_false": not bool(df["live_ready"].any()) if not df.empty else True,
        "all_system_executed_false": not bool(df["system_executed"].any()) if not df.empty else True,
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
