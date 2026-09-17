# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration Safety Boundary.

Defines NO-GO blocking conditions and SAFE-GO principles for full-system integration.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


def build_full_system_integration_no_go_conditions(
    profile: FullSystemIntegrationProfile,
) -> List[Dict[str, Any]]:
    """Return explicit NO-GO prohibited conditions."""
    return [
        {"no_go_id": "NGO-158-001", "action": "live_trading", "is_blocked": True, "reason": "Live trading prohibited."},
        {"no_go_id": "NGO-158-002", "action": "broker_execution", "is_blocked": True, "reason": "Broker API execution prohibited."},
        {"no_go_id": "NGO-158-003", "action": "investment_advice", "is_blocked": True, "reason": "Investment advice prohibited."},
        {"no_go_id": "NGO-158-004", "action": "signal_generation", "is_blocked": True, "reason": "Signal generation prohibited."},
        {"no_go_id": "NGO-158-005", "action": "system_execution", "is_blocked": True, "reason": "System execution prohibited."},
        {"no_go_id": "NGO-158-006", "action": "end_to_end_bot_run", "is_blocked": True, "reason": "End-to-end bot execution prohibited."},
        {"no_go_id": "NGO-158-007", "action": "order_generation", "is_blocked": True, "reason": "Order ticket generation prohibited."},
        {"no_go_id": "NGO-158-008", "action": "model_training", "is_blocked": True, "reason": "Model training prohibited."},
        {"no_go_id": "NGO-158-009", "action": "model_prediction", "is_blocked": True, "reason": "Model prediction prohibited."},
        {"no_go_id": "NGO-158-010", "action": "backtest_execution", "is_blocked": True, "reason": "Backtest execution prohibited."},
        {"no_go_id": "NGO-158-011", "action": "portfolio_execution", "is_blocked": True, "reason": "Portfolio execution prohibited."},
        {"no_go_id": "NGO-158-012", "action": "risk_execution", "is_blocked": True, "reason": "Risk calculation prohibited."},
        {"no_go_id": "NGO-158-013", "action": "scenario_execution", "is_blocked": True, "reason": "Scenario simulation prohibited."},
        {"no_go_id": "NGO-158-014", "action": "optimizer_execution", "is_blocked": True, "reason": "Optimizer execution prohibited."},
        {"no_go_id": "NGO-158-015", "action": "metric_calculation", "is_blocked": True, "reason": "Metric calculation prohibited."},
        {"no_go_id": "NGO-158-016", "action": "target_label_generation", "is_blocked": True, "reason": "Target label generation prohibited."},
        {"no_go_id": "NGO-158-017", "action": "model_registry_write", "is_blocked": True, "reason": "Model registry write prohibited."},
        {"no_go_id": "NGO-158-018", "action": "artifact_persistence", "is_blocked": True, "reason": "Binary artifact persistence prohibited."},
        {"no_go_id": "NGO-158-019", "action": "production_deployment", "is_blocked": True, "reason": "Production deployment prohibited."},
        {"no_go_id": "NGO-158-020", "action": "web_scraping", "is_blocked": True, "reason": "Web scraping prohibited."},
        {"no_go_id": "NGO-158-021", "action": "credential_output", "is_blocked": True, "reason": "Credential output prohibited."},
        {"no_go_id": "NGO-158-022", "action": "source_overwrite", "is_blocked": True, "reason": "Source overwrite prohibited."},
    ]


def build_full_system_integration_safe_go_conditions(
    profile: FullSystemIntegrationProfile,
) -> List[Dict[str, Any]]:
    """Return explicit SAFE-GO permissible actions."""
    return [
        {"safe_go_id": "SGO-158-001", "action": "local_offline_contract_generation", "is_allowed": True, "notes": "Contract generation is permitted."},
        {"safe_go_id": "SGO-158-002", "action": "component_dependency_checkpoint_registry", "is_allowed": True, "notes": "Registry generation is permitted."},
        {"safe_go_id": "SGO-158-003", "action": "manifest_validation_safety_evidence_summary", "is_allowed": True, "notes": "Summary evidence is permitted."},
        {"safe_go_id": "SGO-158-004", "action": "acceptance_rehearsal_checklist_generation", "is_allowed": True, "notes": "Checklist generation is permitted."},
        {"safe_go_id": "SGO-158-005", "action": "disabled_execution_reports_generation", "is_allowed": True, "notes": "Reports are permitted."},
        {"safe_go_id": "SGO-158-006", "action": "phase_159_handoff_preparation", "is_allowed": True, "notes": "Phase 159 handoff is permitted."},
    ]


def build_full_system_integration_safety_boundary(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build full safety boundary DataFrame and summary."""
    no_go = build_full_system_integration_no_go_conditions(profile)
    safe_go = build_full_system_integration_safe_go_conditions(profile)

    records = []
    for item in no_go:
        records.append({
            "rule_id": item["no_go_id"],
            "type": "NO-GO",
            "action": item["action"],
            "status": "BLOCKED",
            "enforced": True,
        })
    for item in safe_go:
        records.append({
            "rule_id": item["safe_go_id"],
            "type": "SAFE-GO",
            "action": item["action"],
            "status": "PERMITTED",
            "enforced": True,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "no_go_count": len(no_go),
        "safe_go_count": len(safe_go),
        "safety_status": "SAFETY_BOUNDARY_ENFORCED",
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
