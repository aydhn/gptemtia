# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Component Checkpoints."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    COMPONENT_CHECKPOINT_DOMAIN,
    ACCEPTANCE_READY,
)

CHECKPOINTS: List[Dict[str, Any]] = [
    {
        "checkpoint_id": "CHK-CMP-146",
        "component_name": "phase_146_realistic_backtest_transaction_cost_slippage",
        "expected_module": "advanced_realistic_backtest",
        "expected_scripts": ["run_realistic_backtest_contracts.py"],
        "expected_tests": ["test_advanced_realistic_backtest.py"],
        "expected_manifest": "realistic_backtest_manifest",
        "expected_validation_report": "realistic_backtest_validation_report",
        "expected_safety_boundary": "realistic_backtest_safety_boundary",
        "expected_handoff": "phase_147_handoff",
    },
    {
        "checkpoint_id": "CHK-CMP-147",
        "component_name": "phase_147_walk_forward_oos_benchmarking",
        "expected_module": "advanced_walk_forward_validation",
        "expected_scripts": ["run_walk_forward_contracts.py"],
        "expected_tests": ["test_advanced_walk_forward_validation.py"],
        "expected_manifest": "walk_forward_manifest",
        "expected_validation_report": "walk_forward_validation_report",
        "expected_safety_boundary": "walk_forward_safety_boundary",
        "expected_handoff": "phase_148_handoff",
    },
    {
        "checkpoint_id": "CHK-CMP-148",
        "component_name": "phase_148_stress_testing_scenario_simulation",
        "expected_module": "advanced_stress_testing",
        "expected_scripts": ["run_stress_testing_contracts.py"],
        "expected_tests": ["test_advanced_stress_testing.py"],
        "expected_manifest": "stress_testing_manifest",
        "expected_validation_report": "stress_testing_validation_report",
        "expected_safety_boundary": "stress_testing_safety_boundary",
        "expected_handoff": "phase_149_handoff",
    },
    {
        "checkpoint_id": "CHK-CMP-149",
        "component_name": "phase_149_monte_carlo_robustness_parameter_stability",
        "expected_module": "advanced_monte_carlo_robustness",
        "expected_scripts": ["run_monte_carlo_contracts.py"],
        "expected_tests": ["test_advanced_monte_carlo_robustness.py"],
        "expected_manifest": "monte_carlo_manifest",
        "expected_validation_report": "monte_carlo_validation_report",
        "expected_safety_boundary": "monte_carlo_safety_boundary",
        "expected_handoff": "phase_150_handoff",
    },
    {
        "checkpoint_id": "CHK-CMP-150",
        "component_name": "phase_150_backtest_governance_bias_control",
        "expected_module": "advanced_backtest_governance",
        "expected_scripts": ["run_backtest_governance_manifest.py"],
        "expected_tests": ["test_advanced_backtest_governance.py"],
        "expected_manifest": "backtest_governance_manifest",
        "expected_validation_report": "backtest_governance_validation_report",
        "expected_safety_boundary": "backtest_governance_safety_boundary",
        "expected_handoff": "phase_151_handoff",
    },
    {
        "checkpoint_id": "CHK-CMP-151",
        "component_name": "phase_151_benchmark_comparison_strategy_evaluation",
        "expected_module": "advanced_benchmark_evaluation",
        "expected_scripts": ["run_benchmark_evaluation_manifest.py"],
        "expected_tests": ["test_advanced_benchmark_evaluation.py"],
        "expected_manifest": "benchmark_evaluation_manifest",
        "expected_validation_report": "benchmark_evaluation_validation_report",
        "expected_safety_boundary": "benchmark_evaluation_safety_boundary",
        "expected_handoff": "phase_152_handoff",
    },
    {
        "checkpoint_id": "CHK-CMP-152",
        "component_name": "phase_152_backtest_acceptance_report",
        "expected_module": "advanced_backtest_acceptance",
        "expected_scripts": ["run_backtest_acceptance_manifest.py"],
        "expected_tests": ["test_backtest_acceptance_manifest.py"],
        "expected_manifest": "backtest_acceptance_manifest",
        "expected_validation_report": "backtest_acceptance_validation_report",
        "expected_safety_boundary": "backtest_acceptance_safety_boundary",
        "expected_handoff": "phase_153_handoff",
    },
]


def build_backtest_acceptance_component_checkpoint_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for component acceptance checkpoints."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for chk in CHECKPOINTS:
        records.append({
            "checkpoint_id": chk["checkpoint_id"],
            "component_name": chk["component_name"],
            "expected_module": chk["expected_module"],
            "expected_scripts": ",".join(chk["expected_scripts"]),
            "expected_tests": ",".join(chk["expected_tests"]),
            "expected_manifest": chk["expected_manifest"],
            "expected_validation_report": chk["expected_validation_report"],
            "expected_safety_boundary": chk["expected_safety_boundary"],
            "expected_handoff": chk["expected_handoff"],
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "contract_only": True,
            "non_production": True,
            "manual_review_required": True,
            "production_ready": False,
            "broker_ready": False,
            "live_ready": False,
            "signal_ready": False,
            "strategy_approved": False,
            "status": ACCEPTANCE_READY,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": COMPONENT_CHECKPOINT_DOMAIN,
        "active_profile": active.profile_name,
        "total_checkpoints": len(records),
        "all_contract_only": True,
        "all_non_production": True,
        "manual_review_required": True,
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def validate_backtest_acceptance_component_checkpoint(checkpoint: Dict[str, Any]) -> Dict[str, Any]:
    """Validate an individual checkpoint against required fields and safety rules."""
    required_keys = [
        "component_name", "expected_module", "expected_manifest",
        "expected_validation_report", "expected_safety_boundary", "expected_handoff"
    ]
    missing = [k for k in required_keys if k not in checkpoint or not checkpoint[k]]
    is_valid = len(missing) == 0

    return {
        "checkpoint_id": checkpoint.get("checkpoint_id", "UNKNOWN"),
        "component_name": checkpoint.get("component_name", "UNKNOWN"),
        "is_valid": is_valid,
        "missing_keys": missing,
        "contract_only": checkpoint.get("contract_only", True),
        "non_production": checkpoint.get("non_production", True),
        "production_ready": False,
        "broker_ready": False,
        "live_ready": False,
        "signal_ready": False,
        "strategy_approved": False,
    }


def summarize_backtest_acceptance_component_checkpoints(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the component checkpoint DataFrame."""
    return {
        "checkpoint_count": len(df),
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty and "contract_only" in df.columns else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty and "non_production" in df.columns else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty and "manual_review_required" in df.columns else True,
        "non_signal": True,
    }
