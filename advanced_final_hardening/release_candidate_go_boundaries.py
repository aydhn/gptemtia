# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate GO Boundaries.

Defines the safe GO pathways permitted for advancing to Phase 160 under local,
offline, and research-only constraints.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    RELEASE_CANDIDATE_BOUNDARY_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

RC_GO_ACTIONS = [
    ("proceed_to_phase_160_final_delivery_contract", "Phase 160 Final Delivery sözleşmesine güvenli devir"),
    ("proceed_to_final_delivery_report_generation", "Nihai teslim raporlarının çevrimdışı derlenmesi"),
    ("proceed_to_final_local_offline_package_summary", "Yerel çevrimdışı paket özetinin oluşturulması"),
    ("proceed_to_final_manual_review_summary", "İnsan onay kapılarının özetlenmesi ve kayıt altına alınması"),
    ("proceed_to_final_no_live_no_broker_safety_summary", "Canlı işlem ve broker yokluğu güvenlik teyidi"),
]


def build_release_candidate_go_boundary_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build release candidate GO boundary registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for action, desc in RC_GO_ACTIONS:
        rows.append({
            "boundary_id": f"RC-GO-{action}",
            "boundary_type": "go",
            "action_name": action,
            "policy": "PERMITTED_LOCAL_RESEARCH_ACTION",
            "reason": desc,
            "domain": RELEASE_CANDIDATE_BOUNDARY_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "go_boundary_count": len(rows),
        "all_safe_go": True,
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
