# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery No-Prediction Boundaries.

Prohibits model inference, forward returns, target labels, and speculative predictions.
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

NO_PREDICTION_RULES = [
    ("zero_model_inference", "Gercek makine ogrenmesi cikarimi veya tahmini yapilamaz"),
    ("zero_forward_returns", "Gelecege yonelik getiri veya fiyat tahmini hesaplanamaz"),
    ("zero_target_labels", "Egitim etiketi veya hedef degisken olusturulamaz"),
]


def build_final_delivery_no_prediction_boundary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build no prediction boundary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for r_name, desc in NO_PREDICTION_RULES:
        rows.append({
            "rule_name": r_name,
            "description": desc,
            "enforced": True,
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
        "rule_count": len(rows),
        "all_enforced": bool(df["enforced"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
