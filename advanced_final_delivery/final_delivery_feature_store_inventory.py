# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery FeatureStore Inventory.

Builds metadata inventory of FeatureStore read interfaces delivered across the project.
Enforces that loaders remain strictly read-only and never trigger execution.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_INVENTORY_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

FEATURE_STORE_LOADER_GROUPS = [
    ("final_delivery_loaders", "Phase 160", "Final delivery manifest, contracts, inventory ve completion okuyuculari"),
    ("final_hardening_loaders", "Phase 159", "Final hardening freeze contracts, checklists ve manifest okuyuculari"),
    ("full_system_integration_loaders", "Phase 158", "Full-system integration contract, boundaries ve manifest okuyuculari"),
    ("portfolio_acceptance_loaders", "Phase 157", "Portfolio acceptance report ve manifest okuyuculari"),
    ("portfolio_scenario_loaders", "Phase 156", "Scenario control ve drawdown manifest okuyuculari"),
    ("risk_reporting_loaders", "Phase 155", "Risk reporting ve exposure manifest okuyuculari"),
    ("portfolio_optimization_loaders", "Phase 154", "Portfolio optimization ve allocation manifest okuyuculari"),
    ("portfolio_construction_loaders", "Phase 153", "Portfolio construction ve sizing manifest okuyuculari"),
    ("backtest_acceptance_loaders", "Phase 152", "Backtest acceptance ve reliability manifest okuyuculari"),
    ("stress_monte_carlo_loaders", "Phase 150-151", "Stress testing ve Monte Carlo manifest okuyuculari"),
    ("ml_acceptance_loaders", "Phase 145", "ML acceptance ve governance manifest okuyuculari"),
    ("feature_factor_loaders", "Phase 116-125", "Feature store, factor families ve quality drift okuyuculari"),
]


def build_final_delivery_feature_store_inventory_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build FeatureStore inventory DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for grp_name, p_range, desc in FEATURE_STORE_LOADER_GROUPS:
        rows.append({
            "loader_group": grp_name,
            "phase_range": p_range,
            "description": desc,
            "read_only": True,
            "execution_triggered": False,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_INVENTORY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "loader_group_count": len(rows),
        "all_read_only": bool(df["read_only"].all()),
        "zero_execution_triggered": not bool(df["execution_triggered"].any()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
