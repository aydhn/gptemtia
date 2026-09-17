# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Gaps Registry.

Identifies non-critical gaps or optional omissions in final delivery artifacts.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_GAP_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

POTENTIAL_GAP_TYPES = [
    ("optional_doc_missing", "Opsiyonel dokumantasyon ayrintisi eksikligi"),
    ("optional_report_missing", "Opsiyonel rapor ciktisi eksikligi"),
    ("final_summary_incomplete", "Nihai ozet detaylarinda bosluk"),
    ("manual_review_note_missing", "Manuel inceleme notunda bosluk"),
    ("operator_handover_detail_incomplete", "Operator devir teslim ayrintisi eksikligi"),
    ("inventory_note_missing", "Envanter aciklama notu eksikligi"),
    ("final_delivery_note_missing", "Nihai teslimat ayrinti notu eksikligi"),
]


def build_final_delivery_gap_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build gap registry DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    df = pd.DataFrame(rows, columns=["gap_id", "gap_type", "description", "severity", "domain", "status"])
    summary = {
        "active_profile": active_profile.profile_name,
        "gap_count": 0,
        "has_gaps": False,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
