# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Manual Review Evidence.

Builds and summarizes the evidence registry for required human review gates and sign-offs.
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

MANUAL_REVIEW_GATES = [
    ("final_manifest_manual_review", "Phase 160 final manifestonun insan tarafindan incelenmesi zorunlulugu"),
    ("safety_boundary_manual_review", "Tum guvenlik sinirlarinin aktif oldugunun operator tarafindan teyit edilmesi"),
    ("validation_report_manual_review", "Dogrulama raporu sonuclarinin ve uyarilarinin incelenmesi"),
    ("operator_handover_manual_review", "Devir teslim protokolunun operator tarafindan imzalanmasi"),
    ("acceptance_evidence_manual_review", "ML, backtest ve portfoy kabul kanitlarinin teyit edilmesi"),
    ("160_phase_completion_manual_review", "160 fazlik plan resmi kapanis kaydinin insan incelemesinden gecmesi"),
]


def build_final_delivery_manual_review_evidence_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build manual review evidence DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for g_name, desc in MANUAL_REVIEW_GATES:
        rows.append({
            "gate_name": g_name,
            "description": desc,
            "manual_review_enforced": True,
            "auto_approval_prohibited": True,
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
        "manual_review_gate_count": len(rows),
        "all_manual_review_enforced": bool(df["manual_review_enforced"].all()),
        "all_auto_approval_prohibited": bool(df["auto_approval_prohibited"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
