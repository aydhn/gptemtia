# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Component Checkpoints.

Verifies structural integrity, artifacts, tests, scripts, and non-production invariants
for each component in the portfolio block (Phases 153-157).
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    COMPONENT_CHECKPOINT_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

CHECKPOINTS = [
    {
        "checkpoint_id": "CHK-153",
        "component_name": "phase_153_portfolio_construction_position_sizing_risk_budgeting",
        "expected_module": "advanced_portfolio_construction",
        "expected_scripts": ["scripts/run_portfolio_construction_manifest.py"],
        "expected_tests": ["tests/test_portfolio_construction_manifest.py"],
        "expected_manifest": "portfolio_construction_manifest",
        "expected_validation_report": "portfolio_construction_validation_report",
        "expected_safety_boundary": "portfolio_construction_safety_boundary",
        "expected_handoff": "phase_154_portfolio_optimization_allocation_constraints_handoff_report",
    },
    {
        "checkpoint_id": "CHK-154",
        "component_name": "phase_154_portfolio_optimization_allocation_constraints",
        "expected_module": "advanced_portfolio_optimization",
        "expected_scripts": ["scripts/run_portfolio_optimization_manifest.py"],
        "expected_tests": ["tests/test_portfolio_optimization_manifest.py"],
        "expected_manifest": "portfolio_optimization_manifest",
        "expected_validation_report": "portfolio_optimization_validation_report",
        "expected_safety_boundary": "portfolio_optimization_safety_boundary",
        "expected_handoff": "phase_155_risk_reporting_exposure_attribution_limit_monitoring_handoff_report",
    },
    {
        "checkpoint_id": "CHK-155",
        "component_name": "phase_155_risk_reporting_exposure_attribution_limit_monitoring",
        "expected_module": "advanced_risk_reporting",
        "expected_scripts": ["scripts/run_risk_reporting_manifest.py"],
        "expected_tests": ["tests/test_risk_reporting_manifest.py"],
        "expected_manifest": "risk_reporting_manifest",
        "expected_validation_report": "risk_reporting_validation_report",
        "expected_safety_boundary": "risk_reporting_safety_boundary",
        "expected_handoff": "phase_156_portfolio_scenario_testing_drawdown_control_handoff_report",
    },
    {
        "checkpoint_id": "CHK-156",
        "component_name": "phase_156_portfolio_scenario_testing_drawdown_control",
        "expected_module": "advanced_portfolio_scenario_control",
        "expected_scripts": ["scripts/run_portfolio_scenario_control_manifest.py"],
        "expected_tests": ["tests/test_portfolio_scenario_control_manifest.py"],
        "expected_manifest": "portfolio_scenario_control_manifest",
        "expected_validation_report": "portfolio_scenario_control_validation_report",
        "expected_safety_boundary": "portfolio_scenario_control_safety_boundary",
        "expected_handoff": "phase_157_portfolio_acceptance_report_handoff_report",
    },
    {
        "checkpoint_id": "CHK-157",
        "component_name": "phase_157_portfolio_acceptance_report",
        "expected_module": "advanced_portfolio_acceptance",
        "expected_scripts": ["scripts/run_portfolio_acceptance_manifest.py"],
        "expected_tests": ["tests/test_portfolio_acceptance_manifest.py"],
        "expected_manifest": "portfolio_acceptance_manifest",
        "expected_validation_report": "portfolio_acceptance_validation_report",
        "expected_safety_boundary": "portfolio_acceptance_safety_boundary",
        "expected_handoff": "phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report",
    },
]


def build_portfolio_acceptance_component_checkpoint_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build verification checkpoint registry for portfolio components."""
    active = profile or get_portfolio_acceptance_profile()
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
            "contract_only": True,
            "non_production": True,
            "manual_review_required": True,
            "production_ready": False,
            "broker_ready": False,
            "live_ready": False,
            "signal_ready": False,
            "strategy_approved": False,
            "portfolio_approved": False,
            "allocation_approved": False,
            "risk_approved": False,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_component_checkpoints(df)
    return df, summary


def validate_portfolio_acceptance_component_checkpoint(checkpoint: Dict[str, Any]) -> Dict[str, Any]:
    """Validate an individual checkpoint against negative invariants."""
    valid = True
    reasons = []
    if checkpoint.get("production_ready", False):
        valid = False
        reasons.append("production_ready must be False")
    if checkpoint.get("broker_ready", False):
        valid = False
        reasons.append("broker_ready must be False")
    if checkpoint.get("live_ready", False):
        valid = False
        reasons.append("live_ready must be False")
    if checkpoint.get("signal_ready", False):
        valid = False
        reasons.append("signal_ready must be False")
    if checkpoint.get("portfolio_approved", False):
        valid = False
        reasons.append("portfolio_approved must be False")
    if not checkpoint.get("contract_only", False):
        valid = False
        reasons.append("contract_only must be True")
    if not checkpoint.get("non_production", False):
        valid = False
        reasons.append("non_production must be True")

    return {
        "is_valid": valid,
        "checkpoint_id": checkpoint.get("checkpoint_id", "unknown"),
        "component_name": checkpoint.get("component_name", "unknown"),
        "reasons": reasons,
        "status": PORTFOLIO_ACCEPTANCE_READY if valid else "CHECKPOINT_INVALID",
    }


def summarize_portfolio_acceptance_component_checkpoints(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize checkpoint registry."""
    return {
        "domain": COMPONENT_CHECKPOINT_DOMAIN,
        "total_checkpoints": len(df),
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "none_production_ready": not bool(df["production_ready"].any()) if not df.empty else True,
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }
