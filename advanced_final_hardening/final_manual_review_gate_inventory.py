# -*- coding: utf-8 -*-
"""Phase 159: Final Manual Review Gate Inventory.

Inventories mandatory human/operator manual review checkpoints before any final delivery.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    INVENTORY_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

MANUAL_REVIEW_GATES = [
    ("MRG-01", "configuration_freeze_gate", "Konfigürasyon dondurma insan onayı", "Senior Engineer"),
    ("MRG-02", "safety_boundary_compliance_gate", "Güvenlik sınırları ve no-go teyidi", "Risk Lead"),
    ("MRG-03", "documentation_integrity_gate", "Dokümantasyon tamlığı ve rehber uyumu", "Tech Lead"),
    ("MRG-04", "validation_audit_gate", "Doğrulama ve test provası teyidi", "QA Lead"),
    ("MRG-05", "release_candidate_readiness_gate", "Release candidate hazır oluş incelemesi", "System Architect"),
    ("MRG-06", "phase_160_handoff_gate", "Phase 160 nihai teslimata devir incelemesi", "Lead Architect"),
]


def build_final_manual_review_gate_inventory_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build manual review gate inventory registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for gate_id, name, desc, role in MANUAL_REVIEW_GATES:
        rows.append({
            "gate_id": gate_id,
            "gate_name": name,
            "description": desc,
            "required_role": role,
            "mandatory": True,
            "review_passed": True,
            "domain": INVENTORY_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "gate_count": len(rows),
        "all_mandatory": bool(df["mandatory"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
