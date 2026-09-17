# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration Domain Registry.

Defines the system-wide domain coverage across all architectural subsystems.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_labels import (
    FULL_SYSTEM_INTEGRATION_PROFILE_DOMAIN,
    FULL_SYSTEM_INTEGRATION_DOMAIN,
    FULL_SYSTEM_INTEGRATION_SCOPE_DOMAIN,
    SYSTEM_COMPONENT_DOMAIN,
    SYSTEM_DEPENDENCY_DOMAIN,
    SYSTEM_CHECKPOINT_DOMAIN,
    CONTRACT_INTEGRATION_DOMAIN,
    MANIFEST_INTEGRATION_DOMAIN,
    VALIDATION_EVIDENCE_DOMAIN,
    SAFETY_BOUNDARY_DOMAIN,
    NON_PRODUCTION_BOUNDARY_DOMAIN,
    DRY_RUN_BOUNDARY_DOMAIN,
    MANUAL_REVIEW_GATE_DOMAIN,
    ACCEPTANCE_REHEARSAL_DOMAIN,
    DATA_PIPELINE_INTEGRATION_DOMAIN,
    FEATURE_FACTOR_INTEGRATION_DOMAIN,
    REGIME_INTEGRATION_DOMAIN,
    ML_GOVERNANCE_INTEGRATION_DOMAIN,
    BACKTEST_ACCEPTANCE_INTEGRATION_DOMAIN,
    PORTFOLIO_ACCEPTANCE_INTEGRATION_DOMAIN,
    RISK_REPORTING_INTEGRATION_DOMAIN,
    SCENARIO_CONTROL_INTEGRATION_DOMAIN,
    REPORTING_INTEGRATION_DOMAIN,
    DISABLED_EXECUTION_DOMAIN,
    BLOCKER_DOMAIN,
    GAP_DOMAIN,
    WARNING_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_159_HANDOFF_DOMAIN,
)


def build_full_system_integration_domain_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build domain registry metadata."""
    domains = [
        {"domain_id": "DOM-158-001", "domain_name": FULL_SYSTEM_INTEGRATION_PROFILE_DOMAIN, "layer": "config", "scope": "system-wide"},
        {"domain_id": "DOM-158-002", "domain_name": FULL_SYSTEM_INTEGRATION_DOMAIN, "layer": "core", "scope": "system-wide"},
        {"domain_id": "DOM-158-003", "domain_name": FULL_SYSTEM_INTEGRATION_SCOPE_DOMAIN, "layer": "scope", "scope": "system-wide"},
        {"domain_id": "DOM-158-004", "domain_name": SYSTEM_COMPONENT_DOMAIN, "layer": "architecture", "scope": "components"},
        {"domain_id": "DOM-158-005", "domain_name": SYSTEM_DEPENDENCY_DOMAIN, "layer": "architecture", "scope": "graph"},
        {"domain_id": "DOM-158-006", "domain_name": SYSTEM_CHECKPOINT_DOMAIN, "layer": "governance", "scope": "checkpoints"},
        {"domain_id": "DOM-158-007", "domain_name": CONTRACT_INTEGRATION_DOMAIN, "layer": "contracts", "scope": "subsystems"},
        {"domain_id": "DOM-158-008", "domain_name": MANIFEST_INTEGRATION_DOMAIN, "layer": "manifests", "scope": "subsystems"},
        {"domain_id": "DOM-158-009", "domain_name": VALIDATION_EVIDENCE_DOMAIN, "layer": "validation", "scope": "evidence"},
        {"domain_id": "DOM-158-010", "domain_name": SAFETY_BOUNDARY_DOMAIN, "layer": "safety", "scope": "boundaries"},
        {"domain_id": "DOM-158-011", "domain_name": NON_PRODUCTION_BOUNDARY_DOMAIN, "layer": "safety", "scope": "non-production"},
        {"domain_id": "DOM-158-012", "domain_name": DRY_RUN_BOUNDARY_DOMAIN, "layer": "safety", "scope": "dry-run"},
        {"domain_id": "DOM-158-013", "domain_name": MANUAL_REVIEW_GATE_DOMAIN, "layer": "governance", "scope": "gates"},
        {"domain_id": "DOM-158-014", "domain_name": ACCEPTANCE_REHEARSAL_DOMAIN, "layer": "rehearsal", "scope": "acceptance"},
        {"domain_id": "DOM-158-015", "domain_name": DATA_PIPELINE_INTEGRATION_DOMAIN, "layer": "subsystem", "scope": "data"},
        {"domain_id": "DOM-158-016", "domain_name": FEATURE_FACTOR_INTEGRATION_DOMAIN, "layer": "subsystem", "scope": "features"},
        {"domain_id": "DOM-158-017", "domain_name": REGIME_INTEGRATION_DOMAIN, "layer": "subsystem", "scope": "regime"},
        {"domain_id": "DOM-158-018", "domain_name": ML_GOVERNANCE_INTEGRATION_DOMAIN, "layer": "subsystem", "scope": "ml"},
        {"domain_id": "DOM-158-019", "domain_name": BACKTEST_ACCEPTANCE_INTEGRATION_DOMAIN, "layer": "subsystem", "scope": "backtest"},
        {"domain_id": "DOM-158-020", "domain_name": PORTFOLIO_ACCEPTANCE_INTEGRATION_DOMAIN, "layer": "subsystem", "scope": "portfolio"},
        {"domain_id": "DOM-158-021", "domain_name": RISK_REPORTING_INTEGRATION_DOMAIN, "layer": "subsystem", "scope": "risk"},
        {"domain_id": "DOM-158-022", "domain_name": SCENARIO_CONTROL_INTEGRATION_DOMAIN, "layer": "subsystem", "scope": "scenario"},
        {"domain_id": "DOM-158-023", "domain_name": REPORTING_INTEGRATION_DOMAIN, "layer": "subsystem", "scope": "reporting"},
        {"domain_id": "DOM-158-024", "domain_name": DISABLED_EXECUTION_DOMAIN, "layer": "policy", "scope": "disabled"},
        {"domain_id": "DOM-158-025", "domain_name": BLOCKER_DOMAIN, "layer": "findings", "scope": "blockers"},
        {"domain_id": "DOM-158-026", "domain_name": GAP_DOMAIN, "layer": "findings", "scope": "gaps"},
        {"domain_id": "DOM-158-027", "domain_name": WARNING_DOMAIN, "layer": "findings", "scope": "warnings"},
        {"domain_id": "DOM-158-028", "domain_name": FINDING_DOMAIN, "layer": "findings", "scope": "findings"},
        {"domain_id": "DOM-158-029", "domain_name": READINESS_SCORE_DOMAIN, "layer": "scoring", "scope": "readiness"},
        {"domain_id": "DOM-158-030", "domain_name": MANIFEST_DOMAIN, "layer": "manifest", "scope": "phase-manifest"},
        {"domain_id": "DOM-158-031", "domain_name": HEALTH_DOMAIN, "layer": "health", "scope": "system-health"},
        {"domain_id": "DOM-158-032", "domain_name": VALIDATION_DOMAIN, "layer": "validation", "scope": "phase-validation"},
        {"domain_id": "DOM-158-033", "domain_name": SAFETY_DOMAIN, "layer": "safety", "scope": "phase-safety"},
        {"domain_id": "DOM-158-034", "domain_name": PHASE_159_HANDOFF_DOMAIN, "layer": "handoff", "scope": "phase-handoff"},
    ]
    df = pd.DataFrame(domains)
    summary = {
        "active_profile": profile.profile_name,
        "total_domains": len(df),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
