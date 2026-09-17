# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Go Boundaries.

Defines safe-go actions permitted during the local/offline Phase 160 final delivery process.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_BOUNDARY_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

SAFE_GO_ACTIONS = [
    ("generate_final_delivery_report", "Nihai teslimat raporu ve sozlesmelerini yerel/cevrimdisi uretme"),
    ("generate_final_manifest", "160 fazi kapsayan nihai sistem manifestosu uretme"),
    ("generate_final_safety_summary", "Tum emniyet ve sifir-canli sinirlarini belgeleyen ozet uretme"),
    ("generate_final_operator_handover", "Operator kullanim ve devir teslim raporu olusturma"),
    ("generate_final_manual_review_summary", "Manuel inceleme kapilari ve insan onayi listesini olusturma"),
    ("mark_phase_160_contract_completed", "160 fazlik plani sozlesme, yonetisim ve kabul duzeyinde kapatma"),
]


def build_final_delivery_go_boundary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build go boundary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for a_name, desc in SAFE_GO_ACTIONS:
        rows.append({
            "action_name": a_name,
            "description": desc,
            "is_safe_go": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_BOUNDARY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "safe_go_action_count": len(rows),
        "all_safe_go": bool(df["is_safe_go"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
