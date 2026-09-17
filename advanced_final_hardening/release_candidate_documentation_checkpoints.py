# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate Documentation Checkpoints."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    RELEASE_CANDIDATE_CHECKPOINT_DOMAIN,
    RELEASE_CANDIDATE_CONTRACT_READY,
)

DOC_CHECKPOINTS = [
    ("chk_readme", "documentation", "README.md", "VERIFIED"),
    ("chk_architecture", "documentation", "docs/ARCHITECTURE.md", "VERIFIED"),
    ("chk_roadmap", "documentation", "docs/ROADMAP.md", "VERIFIED"),
    ("chk_operator_manual", "documentation", "docs/OPERATOR_MANUAL.md", "VERIFIED"),
    ("chk_safe_usage_guide", "documentation", "docs/SAFE_USAGE_GUIDE.md", "VERIFIED"),
    ("chk_rc_checklist", "documentation", "docs/RELEASE_CANDIDATE_CHECKLIST.md", "VERIFIED"),
    ("chk_final_hardening_guide", "documentation", "docs/FINAL_HARDENING_GUIDE.md", "VERIFIED"),
]


def build_release_candidate_documentation_checkpoint_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build documentation checkpoint registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for chk_name, family, artifact, status_val in DOC_CHECKPOINTS:
        rows.append({
            "checkpoint_name": chk_name,
            "checkpoint_family": family,
            "expected_artifact": artifact,
            "expected_status": status_val,
            "validation_ref": "PHASE_159_VALIDATION",
            "safety_ref": "PHASE_159_SAFETY_BOUNDARY",
            "runbook_ref": "PHASE_159_OPERATOR_RUNBOOK",
            "manual_review_required": True,
            "production_ready": False,
            "broker_ready": False,
            "live_ready": False,
            "deployment_ready": False,
            "signal_ready": False,
            "domain": RELEASE_CANDIDATE_CHECKPOINT_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": RELEASE_CANDIDATE_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "checkpoint_count": len(rows),
        "all_verified": True,
        "current_phase": active_profile.current_phase,
        "status": RELEASE_CANDIDATE_CONTRACT_READY,
    }
    return df, summary
