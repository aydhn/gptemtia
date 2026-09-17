# -*- coding: utf-8 -*-
"""Phase 159: Final System Component Inventory.

Consolidates all system components developed across Phases 1 through 159.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    INVENTORY_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

SYSTEM_COMPONENTS = [
    ("advanced_final_hardening", "Phase 159", "Final Hardening, Operator Runbook ve Release Candidate"),
    ("advanced_full_system_integration", "Phase 158", "Full-System Integration and Advanced Acceptance Rehearsal"),
    ("advanced_portfolio_acceptance", "Phase 157", "Portfolio Acceptance Report and Production Readiness Rehearsal"),
    ("advanced_portfolio_scenario_control", "Phase 156", "Portfolio Scenario and Shock Governance"),
    ("advanced_risk_reporting", "Phase 154", "Advanced Risk Reporting and Capital Allocation Constraints"),
    ("advanced_portfolio_optimization", "Phase 153", "Portfolio Optimization and Weight Constraint Governance"),
    ("advanced_portfolio_construction", "Phase 152", "Multi-Asset Portfolio Construction and Regime Rebalancing"),
    ("advanced_backtest_acceptance", "Phase 151", "Advanced Backtest Acceptance and Rejection Governance"),
    ("advanced_benchmark_evaluation", "Phase 150", "Benchmark Evaluation and Relative Performance Assessment"),
    ("advanced_backtest_governance", "Phase 149", "Backtest Governance and Strategy Limitation Contracts"),
    ("advanced_monte_carlo_robustness", "Phase 148", "Monte Carlo Simulation and Parameter Perturbation"),
    ("advanced_stress_testing", "Phase 147", "Stress Testing Scenarios and Extreme Drawdown Bounds"),
    ("advanced_walk_forward_validation", "Phase 146", "Walk-Forward Out-of-Sample Validation Protocols"),
    ("advanced_ml_acceptance", "Phase 145", "ML Model Acceptance and Production Deployment Blockers"),
    ("advanced_model_governance", "Phase 144", "Model Audit, Versioning and Lifecycle Registry"),
    ("data_lake", "Phases 1-159", "Yerel dosya tabanlı veri gölü katmanı"),
    ("feature_store", "Phases 1-159", "Özellik ambarı ve veri okuma katmanı"),
]


def build_final_system_component_inventory_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build system component inventory registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for comp_name, phase, desc in SYSTEM_COMPONENTS:
        rows.append({
            "item_id": f"CMP-{comp_name}",
            "inventory_type": "system_component",
            "item_name": comp_name,
            "associated_phase": phase,
            "description": desc,
            "metadata_only": True,
            "domain": INVENTORY_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "component_count": len(rows),
        "all_metadata_only": bool(df["metadata_only"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
