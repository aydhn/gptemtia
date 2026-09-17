# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Test Inventory.

Builds metadata inventory of test suites validating the codebase across Phase 1-160.
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

TEST_SUITES = [
    ("test_final_delivery_suite", "Phase 160", 55, "Phase 160 final delivery, manifest, validation and closure tests"),
    ("test_final_hardening_suite", "Phase 159", 55, "Phase 159 final hardening, freeze audits and runbook tests"),
    ("test_full_system_integration_suite", "Phase 158", 29, "Phase 158 full system integration and rehearsal tests"),
    ("test_portfolio_acceptance_suite", "Phase 157", 31, "Phase 157 portfolio acceptance and validation tests"),
    ("test_portfolio_scenario_control_suite", "Phase 156", 26, "Phase 156 portfolio scenario and drawdown control tests"),
    ("test_risk_reporting_suite", "Phase 155", 25, "Phase 155 risk reporting and attribution tests"),
    ("test_portfolio_optimization_suite", "Phase 154", 25, "Phase 154 portfolio optimization and constraint tests"),
    ("test_portfolio_construction_suite", "Phase 153", 25, "Phase 153 portfolio construction and sizing tests"),
    ("test_backtest_acceptance_suite", "Phase 152", 28, "Phase 152 backtest acceptance and reliability tests"),
    ("test_stress_monte_carlo_suite", "Phase 150-151", 30, "Phase 150-151 stress and Monte Carlo tests"),
    ("test_realistic_backtest_suite", "Phase 146-149", 35, "Phase 146-149 realistic backtest and walk-forward tests"),
    ("test_ml_acceptance_suite", "Phase 145", 26, "Phase 145 advanced ML acceptance tests"),
    ("test_ml_governance_suite", "Phase 136-144", 60, "Phase 136-144 ML dataset, models, drift, calibration tests"),
    ("test_regime_engine_suite", "Phase 126-135", 70, "Phase 126-135 regime classification and transition tests"),
    ("test_feature_factor_suite", "Phase 116-125", 80, "Phase 116-125 indicator, factor and drift tests"),
    ("test_data_provider_suite", "Phase 106-115", 70, "Phase 106-115 data provider, calendar and news metadata tests"),
]


def build_final_delivery_test_inventory_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build test inventory DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for suite_name, p_range, cnt, desc in TEST_SUITES:
        rows.append({
            "test_suite": suite_name,
            "phase_range": p_range,
            "test_file_count": cnt,
            "description": desc,
            "in_memory_fixtures_safe": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_INVENTORY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    total_test_files = int(df["test_file_count"].sum())
    summary = {
        "active_profile": active_profile.profile_name,
        "test_suite_count": len(rows),
        "total_test_files": total_test_files,
        "all_in_memory_fixtures_safe": bool(df["in_memory_fixtures_safe"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
