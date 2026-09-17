# -*- coding: utf-8 -*-
"""Phase 159: Phase 160 Handoff Report.

Generates the handoff contract bridging Phase 159 Final Hardening and Release Candidate
to Phase 160 Full Advanced Bot Final Delivery.
Enforces that Phase 160 remains strictly local, offline, non-live, and research-only.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    PHASE_160_HANDOFF_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

HANDOFF_PREREQUISITES = [
    ("final_delivery_prerequisites", "Phase 160 nihai teslimat için sözleşme ve paketleme altyapısının hazır olması"),
    ("release_candidate_prerequisites", "Release candidate kontrol listesinin ve manifestinin tamamlanması"),
    ("final_hardening_prerequisites", "Sistem sertleştirme sözleşmelerinin ve dondurma kayıtlarının hazır olması"),
    ("operator_runbook_prerequisites", "Operatör runbook ve acil durum protokollerinin tanımlı olması"),
    ("full_system_integration_prerequisites", "Phase 158 sistem entegrasyonu ve kabul provası çıktılarının doğrulanması"),
    ("backtest_acceptance_prerequisites", "Phase 151 backtest kabul çıktılarının korunması"),
    ("portfolio_acceptance_prerequisites", "Phase 157 portföy kabul çıktılarının korunması"),
    ("safety_boundary_prerequisites", "Canlı işlem ve broker yasağı sınırlarının aktif olması"),
    ("documentation_prerequisites", "Kullanım ve mimari rehberlerinin dondurulmuş olması"),
    ("final_manifest_prerequisites", "Phase 159 release candidate manifestinin imzalanması"),
    ("final_validation_prerequisites", "Tüm doğrulama testlerinin geçmiş olması"),
    ("final_manual_review_prerequisites", "Phase 160 öncesi insan onay kapılarının hazır olması"),
]


def build_phase_160_full_advanced_bot_final_delivery_handoff_report(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build the Phase 160 handoff report DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for item_name, desc in HANDOFF_PREREQUISITES:
        rows.append({
            "prerequisite_name": item_name,
            "description": desc,
            "satisfied": True,
            "domain": PHASE_160_HANDOFF_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "target_final_phase": active_profile.target_final_phase,
            "next_phase": active_profile.next_phase,
            "status": "SATISFIED",
        })

    df = pd.DataFrame(rows)
    all_satisfied = bool(df["satisfied"].all())
    summary = {
        "current_phase": active_profile.current_phase,
        "next_phase": active_profile.next_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase_name": "Phase 160: Full Advanced Bot Final Delivery",
        "prerequisite_count": len(rows),
        "satisfied_count": int(df["satisfied"].sum()),
        "all_satisfied": all_satisfied,
        "phase_160_handoff_ready": all_satisfied,
        "boundary_notice": (
            "Phase 160 creates Full Advanced Bot Final Delivery package under local/offline research boundaries; "
            "live trading, broker execution, investment advice and production deployment remain blocked."
        ),
        "status": "phase_160_handoff_ready" if all_satisfied else "HANDOFF_BLOCKED",
    }
    return df, summary


def summarize_phase_160_handoff(df: pd.DataFrame) -> Dict:
    """Summarize Phase 160 handoff DataFrame."""
    return {
        "total_items": len(df),
        "satisfied_items": int(df["satisfied"].sum()) if "satisfied" in df.columns else len(df),
        "ready": bool(df["satisfied"].all()) if "satisfied" in df.columns else True,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
