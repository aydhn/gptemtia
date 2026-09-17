# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate Script Checkpoints."""

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

SCRIPT_CHECKPOINTS = [
    ("chk_run_profiles", "scripts", "scripts/run_final_hardening_profile_registry.py", "AVAILABLE"),
    ("chk_run_contracts", "scripts", "scripts/run_final_hardening_contracts.py", "AVAILABLE"),
    ("chk_run_runbooks", "scripts", "scripts/run_operator_runbook_contracts.py", "AVAILABLE"),
    ("chk_run_checklists", "scripts", "scripts/run_release_candidate_checklists.py", "AVAILABLE"),
    ("chk_run_health", "scripts", "scripts/run_final_hardening_health_check.py", "AVAILABLE"),
    ("chk_run_status", "scripts", "scripts/run_release_candidate_status.py", "AVAILABLE"),
]


def build_release_candidate_script_checkpoint_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build script checkpoint registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for chk_name, family, artifact, status_val in SCRIPT_CHECKPOINTS:
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
        "all_available": True,
        "current_phase": active_profile.current_phase,
        "status": RELEASE_CANDIDATE_CONTRACT_READY,
    }
    return df, summary
