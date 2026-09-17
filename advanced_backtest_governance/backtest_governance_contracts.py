# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Contracts.

Defines the central contracts linking Phase 146-149 capabilities under
strict offline governance and zero-execution policy.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    GOVERNANCE_CONTRACT_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

CONTRACT_DEFINITIONS: List[Dict[str, Any]] = [
    {
        "contract_name": "realistic_backtest_governance_contract",
        "governance_family": "execution_realism_governance",
        "phase_146_ref": "PHASE_146_REALISTIC_BACKTEST_CONTRACTS",
        "phase_147_ref": "PHASE_147_LINKAGE_READY",
        "phase_148_ref": "PHASE_148_LINKAGE_READY",
        "phase_149_ref": "PHASE_149_LINKAGE_READY",
        "no_lookahead_guard_ref": "GUARD_NO_LOOKAHEAD_EXECUTION",
        "bias_control_ref": "BIAS_CONTROL_TRANSACTION_REALISM",
        "result_claim_boundary_ref": "BOUNDARY_RESULT_CLAIM_BLOCKED",
        "metric_claim_boundary_ref": "BOUNDARY_METRIC_CLAIM_BLOCKED",
    },
    {
        "contract_name": "walk_forward_governance_contract",
        "governance_family": "validation_split_governance",
        "phase_146_ref": "PHASE_146_ENGINE_CONTRACTS",
        "phase_147_ref": "PHASE_147_WALK_FORWARD_CONTRACTS",
        "phase_148_ref": "PHASE_148_LINKAGE_READY",
        "phase_149_ref": "PHASE_149_LINKAGE_READY",
        "no_lookahead_guard_ref": "GUARD_PURGE_AND_EMBARGO",
        "bias_control_ref": "BIAS_CONTROL_OVERFITTING_SPLIT",
        "result_claim_boundary_ref": "BOUNDARY_RESULT_CLAIM_BLOCKED",
        "metric_claim_boundary_ref": "BOUNDARY_METRIC_CLAIM_BLOCKED",
    },
    {
        "contract_name": "oos_benchmark_governance_contract",
        "governance_family": "oos_governance",
        "phase_146_ref": "PHASE_146_REALISTIC_ENGINE",
        "phase_147_ref": "PHASE_147_OOS_BENCHMARK_CONTRACTS",
        "phase_148_ref": "PHASE_148_LINKAGE_READY",
        "phase_149_ref": "PHASE_149_LINKAGE_READY",
        "no_lookahead_guard_ref": "GUARD_OOS_QUARANTINE",
        "bias_control_ref": "BIAS_CONTROL_BENCHMARK_SELECTION",
        "result_claim_boundary_ref": "BOUNDARY_RESULT_CLAIM_BLOCKED",
        "metric_claim_boundary_ref": "BOUNDARY_METRIC_CLAIM_BLOCKED",
    },
    {
        "contract_name": "stress_testing_governance_contract",
        "governance_family": "stress_scenario_governance",
        "phase_146_ref": "PHASE_146_REALISTIC_ENGINE",
        "phase_147_ref": "PHASE_147_VALIDATION_CONTRACTS",
        "phase_148_ref": "PHASE_148_STRESS_TESTING_CONTRACTS",
        "phase_149_ref": "PHASE_149_LINKAGE_READY",
        "no_lookahead_guard_ref": "GUARD_SCENARIO_LEAKAGE",
        "bias_control_ref": "BIAS_CONTROL_REGIME_COVERAGE",
        "result_claim_boundary_ref": "BOUNDARY_RESULT_CLAIM_BLOCKED",
        "metric_claim_boundary_ref": "BOUNDARY_METRIC_CLAIM_BLOCKED",
    },
    {
        "contract_name": "monte_carlo_governance_contract",
        "governance_family": "robustness_governance",
        "phase_146_ref": "PHASE_146_REALISTIC_ENGINE",
        "phase_147_ref": "PHASE_147_VALIDATION_CONTRACTS",
        "phase_148_ref": "PHASE_148_STRESS_CONTRACTS",
        "phase_149_ref": "PHASE_149_MONTE_CARLO_CONTRACTS",
        "no_lookahead_guard_ref": "GUARD_RESAMPLING_LEAKAGE",
        "bias_control_ref": "BIAS_CONTROL_MULTIPLE_TESTING",
        "result_claim_boundary_ref": "BOUNDARY_RESULT_CLAIM_BLOCKED",
        "metric_claim_boundary_ref": "BOUNDARY_METRIC_CLAIM_BLOCKED",
    },
    {
        "contract_name": "result_reporting_governance_contract",
        "governance_family": "reporting_claim_governance",
        "phase_146_ref": "PHASE_146_REPORTING_SPEC",
        "phase_147_ref": "PHASE_147_REPORTING_SPEC",
        "phase_148_ref": "PHASE_148_REPORTING_SPEC",
        "phase_149_ref": "PHASE_149_REPORTING_SPEC",
        "no_lookahead_guard_ref": "GUARD_REPORTING_BIAS",
        "bias_control_ref": "BIAS_CONTROL_REPORTING_DISCLOSURE",
        "result_claim_boundary_ref": "BOUNDARY_RESULT_CLAIM_BLOCKED",
        "metric_claim_boundary_ref": "BOUNDARY_METRIC_CLAIM_BLOCKED",
    },
    {
        "contract_name": "bias_control_governance_contract",
        "governance_family": "bias_audit_governance",
        "phase_146_ref": "PHASE_146_GUARD_SPECS",
        "phase_147_ref": "PHASE_147_GUARD_SPECS",
        "phase_148_ref": "PHASE_148_GUARD_SPECS",
        "phase_149_ref": "PHASE_149_GUARD_SPECS",
        "no_lookahead_guard_ref": "GUARD_COMPREHENSIVE_BIAS",
        "bias_control_ref": "BIAS_CONTROL_MASTER_REGISTRY",
        "result_claim_boundary_ref": "BOUNDARY_RESULT_CLAIM_BLOCKED",
        "metric_claim_boundary_ref": "BOUNDARY_METRIC_CLAIM_BLOCKED",
    },
]


def validate_backtest_governance_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that a single backtest governance contract respects safety invariants."""
    is_valid = True
    reasons: List[str] = []

    if contract.get("backtest_execution_allowed", True) is not False:
        is_valid = False
        reasons.append("backtest_execution_allowed must be strictly False")
    if contract.get("benchmark_execution_allowed", True) is not False:
        is_valid = False
        reasons.append("benchmark_execution_allowed must be strictly False")
    if contract.get("metric_calculation_allowed", True) is not False:
        is_valid = False
        reasons.append("metric_calculation_allowed must be strictly False")
    if contract.get("optimizer_execution_allowed", True) is not False:
        is_valid = False
        reasons.append("optimizer_execution_allowed must be strictly False")
    if contract.get("result_claim_allowed", True) is not False:
        is_valid = False
        reasons.append("result_claim_allowed must be strictly False")
    if contract.get("performance_claim_allowed", True) is not False:
        is_valid = False
        reasons.append("performance_claim_allowed must be strictly False")
    if contract.get("live_trading_allowed", True) is not False:
        is_valid = False
        reasons.append("live_trading_allowed must be strictly False")
    if contract.get("broker_execution_allowed", True) is not False:
        is_valid = False
        reasons.append("broker_execution_allowed must be strictly False")
    if contract.get("signal_generation_allowed", True) is not False:
        is_valid = False
        reasons.append("signal_generation_allowed must be strictly False")
    if contract.get("manual_review_required", False) is not True:
        is_valid = False
        reasons.append("manual_review_required must be True")

    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": is_valid,
        "reasons": reasons,
        "non_signal": True,
    }


def summarize_backtest_governance_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the registered backtest governance contracts."""
    all_exec_blocked = bool(
        (df["backtest_execution_allowed"] == False).all()
        and (df["benchmark_execution_allowed"] == False).all()
        and (df["metric_calculation_allowed"] == False).all()
        and (df["optimizer_execution_allowed"] == False).all()
        and (df["result_claim_allowed"] == False).all()
        and (df["performance_claim_allowed"] == False).all()
        and (df["live_trading_allowed"] == False).all()
        and (df["broker_execution_allowed"] == False).all()
        and (df["signal_generation_allowed"] == False).all()
    ) if not df.empty else True

    return {
        "domain": GOVERNANCE_CONTRACT_DOMAIN,
        "total_contracts": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "all_contracts_valid": all_exec_blocked,
        "all_executions_blocked": all_exec_blocked,
        "all_manual_review_required": bool((df["manual_review_required"] == True).all()) if not df.empty else True,
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
        "all_local_only": bool((df["local_only"] == True).all()) if not df.empty else True,
        "non_signal": True,
    }


def build_backtest_governance_contract_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for backtest governance contracts."""
    rows: List[Dict[str, Any]] = []
    for c in CONTRACT_DEFINITIONS:
        row = {
            "contract_name": c["contract_name"],
            "governance_family": c["governance_family"],
            "phase_146_ref": c["phase_146_ref"],
            "phase_147_ref": c["phase_147_ref"],
            "phase_148_ref": c["phase_148_ref"],
            "phase_149_ref": c["phase_149_ref"],
            "no_lookahead_guard_ref": c["no_lookahead_guard_ref"],
            "bias_control_ref": c["bias_control_ref"],
            "result_claim_boundary_ref": c["result_claim_boundary_ref"],
            "metric_claim_boundary_ref": c["metric_claim_boundary_ref"],
            "backtest_execution_allowed": False,
            "benchmark_execution_allowed": False,
            "metric_calculation_allowed": False,
            "optimizer_execution_allowed": False,
            "result_claim_allowed": False,
            "performance_claim_allowed": False,
            "live_trading_allowed": False,
            "broker_execution_allowed": False,
            "signal_generation_allowed": False,
            "manual_review_required": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "phase": profile.current_phase,
        }
        val = validate_backtest_governance_contract(row)
        row["is_valid"] = val["is_valid"]
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_backtest_governance_contracts(df)
    return df, summary
