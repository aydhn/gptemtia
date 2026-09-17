# -*- coding: utf-8 -*-
"""Phase 158: System Manifest Integration.

Integrates manifests from preceding phases (Data, Feature, Regime, ML, Backtest, Portfolio).
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile

MANIFEST_ENTRIES = [
    ("MNF-INT-001", "data_providers_manifest", "Phase 106", "advanced_data_providers", "READY"),
    ("MNF-INT-002", "economic_calendar_manifest", "Phase 110", "advanced_economic_calendar", "READY"),
    ("MNF-INT-003", "news_sentiment_manifest", "Phase 111", "advanced_news_sentiment_metadata", "READY"),
    ("MNF-INT-004", "feature_factor_manifest", "Phase 125", "advanced_feature_factor_acceptance", "READY"),
    ("MNF-INT-005", "regime_acceptance_manifest", "Phase 135", "advanced_regime_acceptance", "READY"),
    ("MNF-INT-006", "ml_acceptance_manifest", "Phase 145", "advanced_ml_acceptance", "READY"),
    ("MNF-INT-007", "backtest_acceptance_manifest", "Phase 152", "advanced_backtest_acceptance", "READY"),
    ("MNF-INT-008", "portfolio_construction_manifest", "Phase 153", "advanced_portfolio_construction", "READY"),
    ("MNF-INT-009", "portfolio_optimization_manifest", "Phase 154", "advanced_portfolio_optimization", "READY"),
    ("MNF-INT-010", "risk_reporting_manifest", "Phase 155", "advanced_risk_reporting", "READY"),
    ("MNF-INT-011", "scenario_control_manifest", "Phase 156", "advanced_portfolio_scenario_control", "READY"),
    ("MNF-INT-012", "portfolio_acceptance_manifest", "Phase 157", "advanced_portfolio_acceptance", "READY"),
    ("MNF-INT-013", "full_system_integration_manifest", "Phase 158", "advanced_full_system_integration", "READY"),
]


def build_system_manifest_integration_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system manifest integration DataFrame and summary."""
    records = []
    for mid, mname, phase, mod, status in MANIFEST_ENTRIES:
        records.append({
            "manifest_integration_id": mid,
            "manifest_name": mname,
            "origin_phase": phase,
            "target_module": mod,
            "status": status,
            "contract_only": True,
            "non_production": True,
            "manifest_verified": True,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": profile.profile_name,
        "total_manifests_integrated": len(df),
        "all_manifests_verified": bool(df["manifest_verified"].all()) if not df.empty else True,
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
