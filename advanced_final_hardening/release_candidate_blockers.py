# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate Blockers."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    BLOCKER_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

POTENTIAL_BLOCKERS = [
    ("BLK-01", "missing_final_hardening_contract", "Final hardening sözleşmesi eksikliği"),
    ("BLK-02", "missing_operator_runbook_contract", "Operatör runbook sözleşmesi eksikliği"),
    ("BLK-03", "missing_release_candidate_contract", "Release candidate sözleşmesi eksikliği"),
    ("BLK-04", "missing_configuration_freeze_contract", "Konfigürasyon dondurma eksikliği"),
    ("BLK-05", "missing_documentation_freeze_contract", "Dokümantasyon dondurma eksikliği"),
    ("BLK-06", "missing_safety_freeze_contract", "Güvenlik dondurma eksikliği"),
    ("BLK-07", "missing_validation_freeze_contract", "Doğrulama dondurma eksikliği"),
    ("BLK-08", "missing_dependency_freeze_contract", "Bağımlılık dondurma eksikliği"),
    ("BLK-09", "missing_manifest", "Manifest dosyası eksikliği"),
    ("BLK-10", "missing_validation_report", "Doğrulama raporu eksikliği"),
    ("BLK-11", "missing_safety_boundary", "Güvenlik sınırları raporu eksikliği"),
    ("BLK-12", "missing_disabled_execution_report", "Devre dışı çalıştırma raporu eksikliği"),
    ("BLK-13", "unsafe_execution_request_detected", "Güvensiz çalıştırma isteği algılandı"),
    ("BLK-14", "live_trading_request_detected", "Canlı işlem isteği algılandı"),
    ("BLK-15", "broker_execution_request_detected", "Broker bağlantı isteği algılandı"),
    ("BLK-16", "production_deployment_request_detected", "Canlı deployment isteği algılandı"),
    ("BLK-17", "release_deployment_request_detected", "Release deployment isteği algılandı"),
    ("BLK-18", "model_registry_write_request_detected", "Model registry yazma isteği algılandı"),
    ("BLK-19", "artifact_persistence_request_detected", "Artifact persist isteği algılandı"),
    ("BLK-20", "credential_output_detected", "Credential sızıntısı algılandı"),
    ("BLK-21", "source_overwrite_detected", "Kaynak veri ezme algılandı"),
    ("BLK-22", "destructive_action_detected", "Tahribatlı işlem algılandı"),
    ("BLK-23", "phase_160_handoff_missing", "Phase 160 devir raporu eksikliği"),
]


def build_release_candidate_blocker_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build blocker registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for b_id, name, desc in POTENTIAL_BLOCKERS:
        rows.append({
            "blocker_id": b_id,
            "blocker_name": name,
            "description": desc,
            "is_active": False,
            "remedy": "Ensure contract integrity, maintain strict local/offline flags.",
            "domain": BLOCKER_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "total_monitored_blockers": len(rows),
        "active_blockers_count": int(df["is_active"].sum()),
        "has_active_blockers": bool(df["is_active"].any()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
