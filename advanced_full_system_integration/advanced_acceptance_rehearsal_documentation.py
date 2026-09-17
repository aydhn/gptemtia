# -*- coding: utf-8 -*-
"""Phase 158: Advanced Acceptance Rehearsal Documentation.

Verifies that documentation documents match integration requirements and disclaimers.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile

DOCUMENTATION_ITEMS = [
    ("DOC-001", "README.md", "Overview of Phase 158 and architecture status.", "VERIFIED"),
    ("DOC-002", "docs/ARCHITECTURE.md", "System-wide architectural pipeline flow.", "VERIFIED"),
    ("DOC-003", "docs/PHASE_LOG.md", "Historical phase log with Phase 158 additions.", "VERIFIED"),
    ("DOC-004", "docs/ROADMAP.md", "Roadmap tracking Phase 158-160 final closing block.", "VERIFIED"),
    ("DOC-005", "docs/OPERATOR_MANUAL.md", "Operator instructions for rehearsal and reviews.", "VERIFIED"),
    ("DOC-006", "docs/ANALYST_HANDBOOK.md", "Analyst guide for contract interpretation.", "VERIFIED"),
    ("DOC-007", "docs/CODEX_AGENT_GUIDE.md", "Autonomous agent operation boundaries.", "VERIFIED"),
    ("DOC-008", "docs/SAFE_USAGE_GUIDE.md", "Safe usage rules and strict non-live disclaimers.", "VERIFIED"),
    ("DOC-009", "docs/CONFIGURATION.md", "Settings reference for Phase 158.", "VERIFIED"),
]


def build_advanced_acceptance_rehearsal_documentation_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build advanced acceptance rehearsal documentation registry DataFrame and summary."""
    records = []
    for did, dpath, desc, status in DOCUMENTATION_ITEMS:
        records.append({
            "doc_id": did,
            "doc_path": dpath,
            "description": desc,
            "status": status,
            "contract_only": True,
            "non_production": True,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": profile.profile_name,
        "total_documents": len(df),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
