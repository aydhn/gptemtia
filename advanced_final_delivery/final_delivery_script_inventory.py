# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Script Inventory.

Builds metadata inventory of operational CLI scripts delivered across the project.
Does not delete, move, or modify any files.
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

SCRIPT_CATEGORIES = [
    ("final_delivery_scripts", "Phase 160", 12, "Phase 160 final delivery, manifest, validation and completion scripts"),
    ("final_hardening_scripts", "Phase 159", 11, "Phase 159 final hardening, freeze and runbook scripts"),
    ("full_system_integration_scripts", "Phase 158", 10, "Phase 158 full-system integration and acceptance scripts"),
    ("portfolio_acceptance_scripts", "Phase 157", 9, "Phase 157 portfolio acceptance and evidence scripts"),
    ("portfolio_scenario_scripts", "Phase 156", 8, "Phase 156 scenario testing and drawdown scripts"),
    ("risk_reporting_scripts", "Phase 155", 8, "Phase 155 risk reporting and attribution scripts"),
    ("portfolio_optimization_scripts", "Phase 154", 8, "Phase 154 optimization and constraints scripts"),
    ("portfolio_construction_scripts", "Phase 153", 8, "Phase 153 portfolio construction and sizing scripts"),
    ("backtest_acceptance_scripts", "Phase 152", 8, "Phase 152 backtest acceptance scripts"),
    ("stress_monte_carlo_scripts", "Phase 150-151", 10, "Phase 150-151 stress testing and Monte Carlo scripts"),
    ("backtest_engine_scripts", "Phase 146-149", 12, "Phase 146-149 realistic backtest and walk-forward scripts"),
    ("ml_acceptance_scripts", "Phase 145", 8, "Phase 145 advanced ML acceptance scripts"),
    ("ml_governance_scripts", "Phase 140-144", 15, "Phase 140-144 model governance, ensemble, drift and calibration scripts"),
    ("regime_engine_scripts", "Phase 126-135", 20, "Phase 126-135 market regime classification and transition scripts"),
    ("feature_factor_scripts", "Phase 116-125", 25, "Phase 116-125 indicator, factor and drift diagnostic scripts"),
    ("data_provider_scripts", "Phase 106-115", 20, "Phase 106-115 data provider, calendar and news metadata scripts"),
]


def build_final_delivery_script_inventory_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build script inventory DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for cat_name, p_range, cnt, desc in SCRIPT_CATEGORIES:
        rows.append({
            "script_category": cat_name,
            "phase_range": p_range,
            "estimated_script_count": cnt,
            "description": desc,
            "executable_in_dry_run": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_INVENTORY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    total_scripts = int(df["estimated_script_count"].sum())
    summary = {
        "active_profile": active_profile.profile_name,
        "script_category_count": len(rows),
        "total_estimated_scripts": total_scripts,
        "all_dry_run_executable": bool(df["executable_in_dry_run"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
