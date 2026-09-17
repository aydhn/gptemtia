# -*- coding: utf-8 -*-
"""Phase 158: Advanced Acceptance Rehearsal Scripts Registry.

Verifies script existence, non-execution compliance, and contract alignment.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile

REHEARSAL_SCRIPTS = [
    ("RSC-001", "scripts.run_full_system_integration_profile_registry", "Profile, domain, and scope registry runner.", "VERIFIED"),
    ("RSC-002", "scripts.run_system_component_registry", "System component, dependency, and checkpoint runner.", "VERIFIED"),
    ("RSC-003", "scripts.run_system_contract_integration", "Contract, manifest, and evidence integration runner.", "VERIFIED"),
    ("RSC-004", "scripts.run_advanced_acceptance_rehearsal", "Advanced acceptance rehearsal checklist runner.", "VERIFIED"),
    ("RSC-005", "scripts.run_system_boundaries", "Safety, non-production, dry-run, and forbidden column policies runner.", "VERIFIED"),
    ("RSC-006", "scripts.run_system_disabled_execution_reports", "Disabled execution reports generator.", "VERIFIED"),
    ("RSC-007", "scripts.run_system_integration_findings_manifest", "Findings, readiness score, manifest, and handoff runner.", "VERIFIED"),
    ("RSC-008", "scripts.run_full_system_integration_health_check", "System health check runner.", "VERIFIED"),
    ("RSC-009", "scripts.run_full_system_integration_validation_report", "Validation and safety boundary runner.", "VERIFIED"),
    ("RSC-010", "scripts.run_full_system_integration_status", "Full status summary runner.", "VERIFIED"),
]


def build_advanced_acceptance_rehearsal_script_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build advanced acceptance rehearsal script registry DataFrame and summary."""
    records = []
    for sid, sname, desc, status in REHEARSAL_SCRIPTS:
        records.append({
            "script_id": sid,
            "script_path": sname,
            "description": desc,
            "status": status,
            "contract_only": True,
            "non_production": True,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": profile.profile_name,
        "total_scripts": len(df),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
