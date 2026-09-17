# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate Contracts.

Defines the Release Candidate contract layer ensuring all pre-release criteria
are strictly bounded to local, offline, and non-production verification.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    RELEASE_CANDIDATE_DOMAIN,
    RELEASE_CANDIDATE_CONTRACT_READY,
)

RC_CONTRACTS = [
    ("release_candidate_core_contract", "core", "Temel Release Candidate yerel araştırma sözleşmesi"),
    ("release_candidate_safety_boundary_contract", "safety", "Release Candidate güvenlik sınırları ve canlı işlem yasağı sözleşmesi"),
    ("release_candidate_freeze_contract", "freeze", "Kod, konfigürasyon ve dokümantasyon dondurma teyit sözleşmesi"),
    ("release_candidate_verification_contract", "verification", "Doğrulama ve test provası sözleşmesi"),
    ("release_candidate_handoff_contract", "handoff", "Phase 160 nihai bot teslimatına güvenli devir sözleşmesi"),
]


def build_release_candidate_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build the release candidate contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for rc_id, cat, desc in RC_CONTRACTS:
        rows.append({
            "candidate_id": rc_id,
            "candidate_name": rc_id.replace("_", " ").title(),
            "category": cat,
            "description": desc,
            "version_tag": "RC-PHASE-159",
            "domain": RELEASE_CANDIDATE_DOMAIN,
            "production_ready": False,
            "broker_ready": False,
            "live_trading_ready": False,
            "deployment_ready": False,
            "signal_ready": False,
            "official_approval": False,
            "manual_review_required": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "target_final_phase": active_profile.target_final_phase,
            "status": RELEASE_CANDIDATE_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "candidate_contract_count": len(rows),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "all_production_ready_false": bool((~df["production_ready"]).all()),
        "all_broker_ready_false": bool((~df["broker_ready"]).all()),
        "all_live_ready_false": bool((~df["live_trading_ready"]).all()),
        "all_official_approval_false": bool((~df["official_approval"]).all()),
        "status": RELEASE_CANDIDATE_CONTRACT_READY,
    }
    return df, summary


def validate_release_candidate_contract(contract: dict) -> dict:
    """Validate that a release candidate contract makes no unauthorized production or broker claims."""
    violations = []
    if contract.get("production_ready", False):
        violations.append("production_ready must be False")
    if contract.get("broker_ready", False):
        violations.append("broker_ready must be False")
    if contract.get("live_trading_ready", False):
        violations.append("live_trading_ready must be False")
    if contract.get("official_approval", False):
        violations.append("official_approval must be False")

    valid = len(violations) == 0
    return {
        "valid": valid,
        "candidate_id": contract.get("candidate_id", "UNKNOWN"),
        "violations": violations,
        "status": RELEASE_CANDIDATE_CONTRACT_READY if valid else "VIOLATION_DETECTED",
    }
