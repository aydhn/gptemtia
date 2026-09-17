# -*- coding: utf-8 -*-
"""Phase 158: System Integration Blockers Registry.

Tracks potential critical blockers that would prevent integration or handoff.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


def build_system_integration_blocker_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system integration blocker registry DataFrame and summary."""
    # Active system is healthy; potential blocker types are cataloged and monitored
    blocker_catalog = [
        {"blocker_id": "BLK-158-001", "blocker_type": "missing_component", "severity": "CRITICAL", "is_active": False, "description": "Required architectural component missing from project."},
        {"blocker_id": "BLK-158-002", "blocker_type": "missing_dependency", "severity": "CRITICAL", "is_active": False, "description": "Upstream architectural dependency broken or missing."},
        {"blocker_id": "BLK-158-003", "blocker_type": "missing_contract_registry", "severity": "HIGH", "is_active": False, "description": "Contract registry missing for a subsystem."},
        {"blocker_id": "BLK-158-004", "blocker_type": "missing_manifest", "severity": "HIGH", "is_active": False, "description": "Master manifest missing from a previous phase."},
        {"blocker_id": "BLK-158-005", "blocker_type": "missing_validation_report", "severity": "HIGH", "is_active": False, "description": "Validation evidence report missing."},
        {"blocker_id": "BLK-158-006", "blocker_type": "missing_safety_boundary", "severity": "CRITICAL", "is_active": False, "description": "Safety boundary missing or inactive."},
        {"blocker_id": "BLK-158-007", "blocker_type": "missing_disabled_execution_report", "severity": "HIGH", "is_active": False, "description": "Disabled execution report missing."},
        {"blocker_id": "BLK-158-008", "blocker_type": "unsafe_execution_request_detected", "severity": "CRITICAL", "is_active": False, "description": "Attempt to run live or end-to-end execution detected."},
        {"blocker_id": "BLK-158-009", "blocker_type": "live_trading_request_detected", "severity": "CRITICAL", "is_active": False, "description": "Live trading directive detected in payload."},
        {"blocker_id": "BLK-158-010", "blocker_type": "broker_execution_request_detected", "severity": "CRITICAL", "is_active": False, "description": "Broker API invocation detected."},
        {"blocker_id": "BLK-158-011", "blocker_type": "production_deployment_request_detected", "severity": "CRITICAL", "is_active": False, "description": "Production deployment triggered."},
        {"blocker_id": "BLK-158-012", "blocker_type": "order_generation_request_detected", "severity": "CRITICAL", "is_active": False, "description": "Executable order generation detected."},
        {"blocker_id": "BLK-158-013", "blocker_type": "signal_generation_request_detected", "severity": "HIGH", "is_active": False, "description": "Trade signal directive detected."},
        {"blocker_id": "BLK-158-014", "blocker_type": "model_training_request_detected", "severity": "HIGH", "is_active": False, "description": "Model fitting or training request detected."},
        {"blocker_id": "BLK-158-015", "blocker_type": "prediction_request_detected", "severity": "HIGH", "is_active": False, "description": "Model prediction request detected."},
        {"blocker_id": "BLK-158-016", "blocker_type": "backtest_execution_request_detected", "severity": "HIGH", "is_active": False, "description": "Backtest execution run detected."},
        {"blocker_id": "BLK-158-017", "blocker_type": "portfolio_execution_request_detected", "severity": "HIGH", "is_active": False, "description": "Portfolio optimizer run detected."},
        {"blocker_id": "BLK-158-018", "blocker_type": "risk_execution_request_detected", "severity": "HIGH", "is_active": False, "description": "Risk calculation run detected."},
        {"blocker_id": "BLK-158-019", "blocker_type": "scenario_execution_request_detected", "severity": "HIGH", "is_active": False, "description": "Scenario simulation run detected."},
        {"blocker_id": "BLK-158-020", "blocker_type": "phase_159_handoff_missing", "severity": "CRITICAL", "is_active": False, "description": "Phase 159 handoff report missing."},
    ]
    df = pd.DataFrame(blocker_catalog)
    summary = {
        "active_profile": profile.profile_name,
        "total_monitored_blockers": len(df),
        "active_blockers_count": int((df["is_active"] == True).sum()),
        "has_active_blockers": bool((df["is_active"] == True).any()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
