# -*- coding: utf-8 -*-
"""Phase 159: Operator Runbook Contracts.

Defines operator runbook contracts governing safe local operation, startup/shutdown,
health inspection, validation audits, and recovery procedures.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    OPERATOR_RUNBOOK_DOMAIN,
    OPERATOR_RUNBOOK_CONTRACT_READY,
)

OPERATOR_RUNBOOKS = [
    ("operator_startup_runbook_contract", "startup", "Yerel ve çevrimdışı sistem ön kontrol ve başlatma sözleşmesi"),
    ("operator_shutdown_runbook_contract", "shutdown", "Güvenli sistem sonlandırma ve oturum kapatma prosedürü"),
    ("operator_config_check_runbook_contract", "configuration", "Konfigürasyon bütünlüğü ve ortam değişkenleri denetimi"),
    ("operator_data_check_runbook_contract", "data_integrity", "DataLake ve FeatureStore veri bütünlüğü kontrolü"),
    ("operator_report_check_runbook_contract", "reporting", "Raporlama ve çıktı dosyaları doğrulama prosedürü"),
    ("operator_health_check_runbook_contract", "health", "Tüm faz bileşenleri sağlık kontrolü prosedürü"),
    ("operator_validation_runbook_contract", "validation", "Kabul kriterleri ve sözleşme kuralları doğrulama prosedürü"),
    ("operator_troubleshooting_runbook_contract", "troubleshooting", "Hata teşhisi, anomali inceleme ve problem giderme kılavuzu"),
    ("operator_recovery_runbook_contract", "recovery", "Güvenli, tahribatsız geri yükleme ve kurtarma prosedürü"),
    ("operator_safe_usage_runbook_contract", "safe_usage", "Canlı işlem yasağı ve güvenli araştırma kullanım sınırları kılavuzu"),
]


def build_operator_runbook_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build the operator runbook contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for rb_name, cat, desc in OPERATOR_RUNBOOKS:
        rows.append({
            "runbook_name": rb_name,
            "category": cat,
            "description": desc,
            "execution_instructions_allowed": False,
            "live_bot_execution_allowed": False,
            "broker_execution_allowed": False,
            "manual_review_required": True,
            "domain": OPERATOR_RUNBOOK_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": OPERATOR_RUNBOOK_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "runbook_count": len(rows),
        "current_phase": active_profile.current_phase,
        "all_execution_instructions_blocked": bool((~df["execution_instructions_allowed"]).all()),
        "all_live_bot_blocked": bool((~df["live_bot_execution_allowed"]).all()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "status": OPERATOR_RUNBOOK_CONTRACT_READY,
    }
    return df, summary


def validate_operator_runbook_contract(contract: dict) -> dict:
    """Validate that an operator runbook contract contains no execution instructions."""
    violations = []
    if contract.get("execution_instructions_allowed", False):
        violations.append("execution_instructions_allowed must be False")
    if contract.get("live_bot_execution_allowed", False):
        violations.append("live_bot_execution_allowed must be False")
    if contract.get("broker_execution_allowed", False):
        violations.append("broker_execution_allowed must be False")

    valid = len(violations) == 0
    return {
        "valid": valid,
        "runbook_name": contract.get("runbook_name", "UNKNOWN"),
        "violations": violations,
        "status": OPERATOR_RUNBOOK_CONTRACT_READY if valid else "VIOLATION_DETECTED",
    }
