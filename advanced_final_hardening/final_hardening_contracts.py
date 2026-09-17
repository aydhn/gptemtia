# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Contracts.

Defines the core hardening contracts binding all subsystem validations, safety boundaries,
and freeze checkpoints before Phase 160.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    FINAL_HARDENING_CONTRACT_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

HARDENING_CONTRACTS = [
    ("local_final_hardening_contract", "local_offline_hardening", "Yerel ve çevrimdışı çalışma ortamı kesin sınır sözleşmesi"),
    ("system_boundary_hardening_contract", "system_safety_hardening", "Sistem sınırları ve yetkisiz çalıştırma engelleme sözleşmesi"),
    ("configuration_hardening_contract", "configuration_hardening", "Tüm konfigürasyon ve ayarların denetlenmesi ve dondurulması sözleşmesi"),
    ("documentation_hardening_contract", "documentation_hardening", "Operatör, analist ve mimari dokümantasyon bütünlüğü sözleşmesi"),
    ("validation_hardening_contract", "validation_hardening", "Sistem kuralları ve test kabul kriterleri doğrulama sözleşmesi"),
    ("release_candidate_hardening_contract", "release_candidate_hardening", "Release candidate hazır oluş ve kontrol noktaları sözleşmesi"),
    ("operator_runbook_hardening_contract", "operator_runbook_hardening", "Operatör çalıştırma, durdurma ve teşhis protokolleri sözleşmesi"),
    ("no_go_protocol_hardening_contract", "safety_hardening", "Kritik NO-GO sınırları ve engelleme kuralları sözleşmesi"),
    ("final_delivery_handoff_hardening_contract", "handoff_hardening", "Phase 160 Full Advanced Bot Final Delivery devir sözleşmesi"),
]


def build_final_hardening_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build the final hardening contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for c_name, family, desc in HARDENING_CONTRACTS:
        rows.append({
            "contract_name": c_name,
            "hardening_family": family,
            "description": desc,
            "full_system_integration_ref": "PHASE_158_FULL_SYSTEM_INTEGRATION",
            "portfolio_acceptance_ref": "PHASE_157_PORTFOLIO_ACCEPTANCE",
            "backtest_acceptance_ref": "PHASE_151_BACKTEST_ACCEPTANCE",
            "safety_boundary_ref": "PHASE_159_SAFETY_BOUNDARY",
            "validation_report_ref": "PHASE_159_VALIDATION_REPORT",
            "manifest_ref": "PHASE_159_RELEASE_CANDIDATE_MANIFEST",
            "operator_runbook_ref": "PHASE_159_OPERATOR_RUNBOOK",
            "release_candidate_ref": "PHASE_159_RELEASE_CANDIDATE",
            "phase_160_handoff_ref": "PHASE_160_FULL_ADVANCED_BOT_FINAL_DELIVERY",
            "domain": FINAL_HARDENING_CONTRACT_DOMAIN,
            "system_execution_allowed": False,
            "release_deployment_allowed": False,
            "production_deployment_allowed": False,
            "live_trading_allowed": False,
            "broker_execution_allowed": False,
            "signal_generation_allowed": False,
            "order_generation_allowed": False,
            "model_training_allowed": False,
            "prediction_allowed": False,
            "model_registry_write_allowed": False,
            "artifact_persistence_allowed": False,
            "manual_review_required": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "contract_count": len(rows),
        "current_phase": active_profile.current_phase,
        "all_execution_blocked": bool((~df["system_execution_allowed"]).all()),
        "all_live_trading_blocked": bool((~df["live_trading_allowed"]).all()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary


def validate_final_hardening_contract(contract: dict) -> dict:
    """Validate that an individual final hardening contract conforms to safety boundaries."""
    violations = []
    if contract.get("system_execution_allowed", False):
        violations.append("system_execution_allowed must be False")
    if contract.get("release_deployment_allowed", False):
        violations.append("release_deployment_allowed must be False")
    if contract.get("production_deployment_allowed", False):
        violations.append("production_deployment_allowed must be False")
    if contract.get("live_trading_allowed", False):
        violations.append("live_trading_allowed must be False")
    if contract.get("broker_execution_allowed", False):
        violations.append("broker_execution_allowed must be False")
    if contract.get("signal_generation_allowed", False):
        violations.append("signal_generation_allowed must be False")

    valid = len(violations) == 0
    return {
        "valid": valid,
        "contract_name": contract.get("contract_name", "UNKNOWN"),
        "violations": violations,
        "status": FINAL_HARDENING_CONTRACT_READY if valid else "VIOLATION_DETECTED",
    }


def summarize_final_hardening_contracts(df: pd.DataFrame) -> dict:
    """Summarize the DataFrame of final hardening contracts."""
    return {
        "total_contracts": len(df),
        "unique_families": int(df["hardening_family"].nunique()) if not df.empty else 0,
        "all_safe": bool((~df["live_trading_allowed"]).all() and (~df["system_execution_allowed"]).all()) if not df.empty else True,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
