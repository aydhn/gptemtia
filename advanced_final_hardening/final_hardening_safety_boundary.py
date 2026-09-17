# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Safety Boundary.

Defines the system-level safety boundary, NO-GO conditions, and safe GO conditions.
"""

from typing import Dict, List, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    SAFETY_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

FINAL_HARDENING_NO_GO_CONDITIONS: List[str] = [
    "live_trading_execution",
    "broker_integration_connection",
    "real_order_generation",
    "signal_generation_output",
    "directional_trade_claim",
    "investment_advice_dissemination",
    "system_execution_initiation",
    "end_to_end_run_initiation",
    "release_deployment_initiation",
    "production_deployment_initiation",
    "production_approval_claim",
    "broker_ready_approval_claim",
    "live_ready_approval_claim",
    "official_approval_claim",
    "model_training_fit",
    "model_predict_inference",
    "target_label_generation",
    "backtest_execution",
    "benchmark_execution",
    "portfolio_execution",
    "risk_execution",
    "scenario_execution",
    "optimizer_execution",
    "metric_calculation",
    "model_registry_write",
    "artifact_persistence",
    "model_deployment",
    "web_scraping",
    "credential_output",
    "source_overwrite",
    "file_deletion",
    "destructive_cleaning",
]

FINAL_HARDENING_SAFE_GO_CONDITIONS: List[str] = [
    "local_offline_final_hardening_contract_generation",
    "operator_runbook_contract_generation",
    "release_candidate_checklist_generation",
    "freeze_audit_inventory_registry_generation",
    "no_go_go_boundary_generation",
    "release_candidate_manifest_generation",
    "phase_160_final_delivery_handoff_generation",
]


def build_final_hardening_no_go_conditions(
    profile: FinalHardeningProfile | None = None,
) -> List[str]:
    """Return all active NO-GO conditions."""
    return list(FINAL_HARDENING_NO_GO_CONDITIONS)


def build_final_hardening_safe_go_conditions(
    profile: FinalHardeningProfile | None = None,
) -> List[str]:
    """Return all active safe GO conditions."""
    return list(FINAL_HARDENING_SAFE_GO_CONDITIONS)


def build_final_hardening_safety_boundary(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build safety boundary DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for cond in FINAL_HARDENING_NO_GO_CONDITIONS:
        rows.append({
            "boundary_id": f"NO-GO-{cond}",
            "condition_type": "NO-GO",
            "name": cond,
            "policy": "BLOCKED",
            "enforced": True,
            "domain": SAFETY_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    for cond in FINAL_HARDENING_SAFE_GO_CONDITIONS:
        rows.append({
            "boundary_id": f"SAFE-GO-{cond}",
            "condition_type": "SAFE-GO",
            "name": cond,
            "policy": "PERMITTED_OFFLINE_RESEARCH",
            "enforced": True,
            "domain": SAFETY_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "total_rules": len(rows),
        "no_go_count": len(FINAL_HARDENING_NO_GO_CONDITIONS),
        "safe_go_count": len(FINAL_HARDENING_SAFE_GO_CONDITIONS),
        "safety_status": "SAFETY_BOUNDARY_ENFORCED",
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
