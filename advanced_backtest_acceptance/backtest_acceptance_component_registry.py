# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Component Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    COMPONENT_REGISTRY_DOMAIN,
    ACCEPTANCE_READY,
)

COMPONENTS: List[Dict[str, Any]] = [
    {
        "component_id": "CMP-146",
        "component_name": "phase_146_realistic_backtest_transaction_cost_slippage",
        "phase_ref": "Phase 146",
        "primary_module": "advanced_realistic_backtest",
        "description": "Realistic Backtest, Transaction Cost and Slippage Modeling contract layer.",
    },
    {
        "component_id": "CMP-147",
        "component_name": "phase_147_walk_forward_oos_benchmarking",
        "phase_ref": "Phase 147",
        "primary_module": "advanced_walk_forward_validation",
        "description": "Walk-Forward Validation and Out-of-Sample Benchmarking contract layer.",
    },
    {
        "component_id": "CMP-148",
        "component_name": "phase_148_stress_testing_scenario_simulation",
        "phase_ref": "Phase 148",
        "primary_module": "advanced_stress_testing",
        "description": "Stress Testing and Scenario Simulation contract layer.",
    },
    {
        "component_id": "CMP-149",
        "component_name": "phase_149_monte_carlo_robustness_parameter_stability",
        "phase_ref": "Phase 149",
        "primary_module": "advanced_monte_carlo_robustness",
        "description": "Monte Carlo Robustness and Parameter Stability contract layer.",
    },
    {
        "component_id": "CMP-150",
        "component_name": "phase_150_backtest_governance_bias_control",
        "phase_ref": "Phase 150",
        "primary_module": "advanced_backtest_governance",
        "description": "Backtest Governance and Bias Control contract layer.",
    },
    {
        "component_id": "CMP-151",
        "component_name": "phase_151_benchmark_comparison_strategy_evaluation",
        "phase_ref": "Phase 151",
        "primary_module": "advanced_benchmark_evaluation",
        "description": "Benchmark Comparison and Strategy Evaluation Reports contract layer.",
    },
    {
        "component_id": "CMP-152",
        "component_name": "phase_152_backtest_acceptance_report",
        "phase_ref": "Phase 152",
        "primary_module": "advanced_backtest_acceptance",
        "description": "Backtest Acceptance Report, Consolidated Acceptance Layer and Phase 153 Handoff.",
    },
]


def build_backtest_acceptance_component_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Backtest block components."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for c in COMPONENTS:
        records.append({
            "component_id": c["component_id"],
            "component_name": c["component_name"],
            "phase_ref": c["phase_ref"],
            "primary_module": c["primary_module"],
            "description": c["description"],
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "contract_only": True,
            "non_production": True,
            "production_ready": False,
            "broker_ready": False,
            "signal_ready": False,
            "strategy_approved": False,
            "status": ACCEPTANCE_READY,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": COMPONENT_REGISTRY_DOMAIN,
        "active_profile": active.profile_name,
        "total_components": len(records),
        "all_contract_only": True,
        "all_non_production": True,
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_backtest_acceptance_components(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the component DataFrame."""
    return {
        "component_count": len(df),
        "phases_covered": list(df["phase_ref"].unique()) if not df.empty else [],
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty and "contract_only" in df.columns else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty and "non_production" in df.columns else True,
        "non_signal": True,
    }
