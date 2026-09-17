# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration Scope Registry.

Defines the operational scope, permissible actions, and explicit boundaries.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


def build_full_system_integration_scope_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build scope registry metadata."""
    scope_items = [
        {"scope_id": "SCP-158-001", "scope_item": "full_system_integration_contract", "is_allowed": True, "category": "permitted"},
        {"scope_id": "SCP-158-002", "scope_item": "system_wide_dependency_graph", "is_allowed": True, "category": "permitted"},
        {"scope_id": "SCP-158-003", "scope_item": "system_wide_dry_run_rehearsal_plan", "is_allowed": True, "category": "permitted"},
        {"scope_id": "SCP-158-004", "scope_item": "advanced_acceptance_rehearsal_checklist", "is_allowed": True, "category": "permitted"},
        {"scope_id": "SCP-158-005", "scope_item": "component_completeness_verification", "is_allowed": True, "category": "permitted"},
        {"scope_id": "SCP-158-006", "scope_item": "manifest_presence_verification", "is_allowed": True, "category": "permitted"},
        {"scope_id": "SCP-158-007", "scope_item": "safety_boundary_verification", "is_allowed": True, "category": "permitted"},
        {"scope_id": "SCP-158-008", "scope_item": "phase_159_handoff_preparation", "is_allowed": True, "category": "permitted"},
        {"scope_id": "SCP-158-009", "scope_item": "live_order_execution", "is_allowed": False, "category": "prohibited"},
        {"scope_id": "SCP-158-010", "scope_item": "broker_api_integration", "is_allowed": False, "category": "prohibited"},
        {"scope_id": "SCP-158-011", "scope_item": "trading_signal_generation", "is_allowed": False, "category": "prohibited"},
        {"scope_id": "SCP-158-012", "scope_item": "investment_advice_generation", "is_allowed": False, "category": "prohibited"},
        {"scope_id": "SCP-158-013", "scope_item": "real_system_execution", "is_allowed": False, "category": "prohibited"},
        {"scope_id": "SCP-158-014", "scope_item": "end_to_end_bot_run", "is_allowed": False, "category": "prohibited"},
        {"scope_id": "SCP-158-015", "scope_item": "model_fit_train_predict", "is_allowed": False, "category": "prohibited"},
        {"scope_id": "SCP-158-016", "scope_item": "backtest_and_optimizer_run", "is_allowed": False, "category": "prohibited"},
        {"scope_id": "SCP-158-017", "scope_item": "portfolio_construction_and_risk_execution", "is_allowed": False, "category": "prohibited"},
        {"scope_id": "SCP-158-018", "scope_item": "production_deployment_and_approval", "is_allowed": False, "category": "prohibited"},
        {"scope_id": "SCP-158-019", "scope_item": "web_scraping_and_credential_output", "is_allowed": False, "category": "prohibited"},
        {"scope_id": "SCP-158-020", "scope_item": "source_overwrite_and_destructive_cleaning", "is_allowed": False, "category": "prohibited"},
    ]
    df = pd.DataFrame(scope_items)
    summary = {
        "active_profile": profile.profile_name,
        "total_scope_items": len(df),
        "permitted_count": int((df["is_allowed"] == True).sum()),
        "prohibited_count": int((df["is_allowed"] == False).sum()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
