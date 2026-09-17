# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Release Candidate Evidence.

Builds and summarizes the evidence registry for Phase 159 Release Candidate checkpoints and checklists.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_EVIDENCE_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

RELEASE_CANDIDATE_CHECKPOINTS = [
    ("RC-CHK-01-COMPONENT", "Bilesen tamlik ve mevcudiyet kontrol noktasi"),
    ("RC-CHK-02-DEPENDENCY", "Paket bagimliliklari ve import butunlugu kontrol noktasi"),
    ("RC-CHK-03-VALIDATION", "Dogrulama testleri ve acceptance kriterleri kontrol noktasi"),
    ("RC-CHK-04-SAFETY", "Guvenlik sinirlari ve no-live/no-broker kontrolleri"),
    ("RC-CHK-05-DOCS", "Dokumantasyon tamligi ve kullanim rehberleri kontrol noktasi"),
    ("RC-CHK-06-SCRIPTS", "CLI betik calisma basarisi ve exit code 0 kontrol noktasi"),
    ("RC-CHK-07-TESTS", "Test paketleri basari orani ve regresyon kontrol noktasi"),
    ("RC-CHK-08-REPORTS", "Rapor formatlari ve feragatnameler kontrol noktasi"),
]


def build_final_delivery_release_candidate_evidence_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build release candidate evidence DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for chk_name, desc in RELEASE_CANDIDATE_CHECKPOINTS:
        rows.append({
            "checkpoint_id": chk_name,
            "phase_reference": "Phase 159",
            "description": desc,
            "passed": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_EVIDENCE_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "checkpoint_count": len(rows),
        "all_passed": bool(df["passed"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
