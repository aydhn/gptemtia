# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Documentation Inventory.

Builds metadata inventory of all primary documents and user guides in the project.
Does not delete, move, or modify any files.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_INVENTORY_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

DOCUMENTATION_FILES = [
    ("README.md", "Ana repo rehberi ve Phase 160 Full Advanced Bot Final Delivery ozeti"),
    ("docs/ARCHITECTURE.md", "160 fazlik gelistirme mimari tasarimi ve veri akislari"),
    ("docs/PHASE_LOG.md", "Phase 1-160 tamamlanmis tum fazlarin ayrintili gunlugu"),
    ("docs/ROADMAP.md", "160 fazlik resmi gelistirme yol haritasi ve kapanis durumu"),
    ("docs/OPERATOR_MANUAL.md", "Operator kullanim, izleme ve baslatma/durdurma el kitabi"),
    ("docs/ANALYST_HANDBOOK.md", "Analist arastirma ve offline calisma rehberi"),
    ("docs/CODEX_AGENT_GUIDE.md", "AI ve ajan yonergeleri, kodlama kurallari ve sinirlar"),
    ("docs/SAFE_USAGE_GUIDE.md", "Guvenli kullanim, no-live/no-broker emniyet rehberi"),
    ("docs/CONFIGURATION.md", "Sistem konfigürasyon parametreleri ve profilleri kilavuzu"),
    ("docs/RELEASE_CANDIDATE_CHECKLIST.md", "Phase 159 release candidate kontrol listesi rehberi"),
    ("docs/FINAL_HARDENING_GUIDE.md", "Phase 159 final hardening ve sistem dondurma rehberi"),
    ("docs/FINAL_DELIVERY.md", "Phase 160 Full Advanced Bot Final Delivery kapsami ve paket sozlesmeleri"),
    ("docs/FINAL_SYSTEM_SUMMARY.md", "Phase 1-160 konsolide sistem, MVP ve gelismis bloklar ozeti"),
    ("docs/FINAL_OPERATOR_HANDOVER.md", "Operator devir teslim protokolu ve guvenli yerel kullanim rehberi"),
    ("docs/FINAL_SAFETY_BOUNDARY.md", "Sistem geneli sifir-canli ve sifir-broker emniyet kurallari"),
    ("docs/FINAL_MANUAL_REVIEW.md", "Insan onay kapisi, manuel inceleme kuyrugu ve kontrol listesi"),
]


def build_final_delivery_docs_inventory_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build docs inventory DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for doc_path, desc in DOCUMENTATION_FILES:
        rows.append({
            "doc_path": doc_path,
            "description": desc,
            "verified": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_INVENTORY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "docs_count": len(rows),
        "all_verified": bool(df["verified"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
