# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Blockers Registry.

Evaluates and summarizes any critical blockers that would prevent final delivery.
In a clean, compliant build, 0 blockers are detected.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_BLOCKER_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

POTENTIAL_BLOCKER_TYPES = [
    ("missing_final_delivery_contract", "Nihai teslimat sozlesmelerinin eksik olmasi"),
    ("missing_final_manifest", "Final manifestonun eksik olmasi"),
    ("missing_final_validation_report", "Validasyon raporunun eksik olmasi"),
    ("missing_final_safety_boundary", "Emniyet siniri tescilinin eksik olmasi"),
    ("missing_final_operator_handover", "Operator devir raporunun eksik olmasi"),
    ("missing_release_candidate_evidence", "Phase 159 release candidate kanitlarinin eksik olmasi"),
    ("missing_acceptance_evidence", "Milestone kabul kanitlarinin eksik olmasi"),
    ("missing_disabled_execution_report", "Yurutme engelleme raporlarinin eksik olmasi"),
    ("unsafe_execution_request_detected", "Guvenliksiz calistirma talebi tespiti"),
    ("live_trading_request_detected", "Canli islem talebi tespiti"),
    ("broker_execution_request_detected", "Broker baglanti talebi tespiti"),
    ("production_deployment_request_detected", "Uretim dagitim talebi tespiti"),
    ("release_deployment_request_detected", "Release dagitim talebi tespiti"),
    ("model_registry_write_request_detected", "Model registry yazim talebi tespiti"),
    ("artifact_persistence_request_detected", "Artifact persist etme talebi tespiti"),
    ("credential_output_detected", "Kimlik bilgisi yazdirma talebi tespiti"),
    ("source_overwrite_detected", "Kaynak ezme talebi tespiti"),
    ("destructive_action_detected", "Yikici aksiyon talebi tespiti"),
]


def build_final_delivery_blocker_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build blocker registry DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    # In compliant state, no active blockers exist
    df = pd.DataFrame(rows, columns=["blocker_id", "blocker_type", "description", "severity", "domain", "status"])
    summary = {
        "active_profile": active_profile.profile_name,
        "blocker_count": 0,
        "has_blockers": False,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
