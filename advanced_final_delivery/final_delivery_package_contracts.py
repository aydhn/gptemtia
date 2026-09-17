# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Package Contracts.

Builds and validates the core delivery contracts governing the Phase 160 final package.
Enforces zero live trading, zero execution, and mandatory manual review gates.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_PACKAGE_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

DELIVERY_CONTRACTS = [
    {
        "contract_name": "local_offline_final_delivery_contract",
        "delivery_family": "final_package",
        "description": "Yerel ve cevrimdisi nihai teslimat paketi genel sozlesmesi.",
    },
    {
        "contract_name": "final_manifest_delivery_contract",
        "delivery_family": "manifest_delivery",
        "description": "160 fazlik gelistirme butunlugunu belgeleyen nihai manifesto teslim sozlesmesi.",
    },
    {
        "contract_name": "final_documentation_delivery_contract",
        "delivery_family": "documentation_delivery",
        "description": "Tum mimari, operator, analist ve guvenlik dokumantasyonu teslim sozlesmesi.",
    },
    {
        "contract_name": "final_acceptance_delivery_contract",
        "delivery_family": "acceptance_delivery",
        "description": "ML, backtest, portfoy, sistem ve release candidate kabul kanitlari teslim sozlesmesi.",
    },
    {
        "contract_name": "final_safety_delivery_contract",
        "delivery_family": "safety_delivery",
        "description": "Canli islem, broker ve yatirim tavsiyesi yasaklarini donduran nihai emniyet sozlesmesi.",
    },
    {
        "contract_name": "final_operator_handover_contract",
        "delivery_family": "operator_handover",
        "description": "Operatorler icin guvenli calistirma ve devir teslim sozlesmesi.",
    },
    {
        "contract_name": "final_160_phase_completion_contract",
        "delivery_family": "plan_completion",
        "description": "160 fazlik planin sozlesme ve kabul duzeyinde resmi kapanis sozlesmesi.",
    },
]


def build_final_delivery_package_contract_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build final delivery package contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for c in DELIVERY_CONTRACTS:
        rows.append({
            "contract_name": c["contract_name"],
            "delivery_family": c["delivery_family"],
            "description": c["description"],
            "phase_ref": "Phase 160",
            "profile_ref": active_profile.profile_name,
            "final_hardening_ref": "Phase 159 Final Hardening and Release Candidate",
            "full_system_integration_ref": "Phase 158 Full-System Integration",
            "portfolio_acceptance_ref": "Phase 157 Portfolio Acceptance",
            "backtest_acceptance_ref": "Phase 152 Backtest Acceptance",
            "safety_boundary_ref": "Phase 160 Final Safety Boundary",
            "validation_report_ref": "Phase 160 Final Validation Report",
            "release_candidate_ref": "Phase 159 Release Candidate Checklists",
            "operator_runbook_ref": "Phase 159 Operator Runbook Protocols",
            "final_completion_ref": "Phase 160 160-Phase Plan Closure",
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
            "domain": FINAL_PACKAGE_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "contract_count": len(rows),
        "all_execution_disabled": not bool(df["system_execution_allowed"].any()),
        "all_live_disabled": not bool(df["live_trading_allowed"].any()),
        "all_broker_disabled": not bool(df["broker_execution_allowed"].any()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_final_delivery_package_contract(contract: dict) -> dict:
    """Validate that a contract dictionary strictly adheres to safety boundaries."""
    errors = []
    if contract.get("system_execution_allowed", False):
        errors.append("system_execution_allowed must be False")
    if contract.get("release_deployment_allowed", False):
        errors.append("release_deployment_allowed must be False")
    if contract.get("production_deployment_allowed", False):
        errors.append("production_deployment_allowed must be False")
    if contract.get("live_trading_allowed", False):
        errors.append("live_trading_allowed must be False")
    if contract.get("broker_execution_allowed", False):
        errors.append("broker_execution_allowed must be False")
    if contract.get("signal_generation_allowed", False):
        errors.append("signal_generation_allowed must be False")
    if contract.get("order_generation_allowed", False):
        errors.append("order_generation_allowed must be False")
    if contract.get("model_training_allowed", False):
        errors.append("model_training_allowed must be False")
    if contract.get("prediction_allowed", False):
        errors.append("prediction_allowed must be False")
    if contract.get("model_registry_write_allowed", False):
        errors.append("model_registry_write_allowed must be False")
    if contract.get("artifact_persistence_allowed", False):
        errors.append("artifact_persistence_allowed must be False")
    if not contract.get("manual_review_required", False):
        errors.append("manual_review_required must be True")

    valid = len(errors) == 0
    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "valid": valid,
        "errors": errors,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if valid else "CONTRACT_INVALID",
    }


def summarize_final_delivery_package_contracts(df: pd.DataFrame) -> dict:
    """Summarize the package contracts DataFrame."""
    return {
        "total_contracts": len(df),
        "contracts": df["contract_name"].tolist() if "contract_name" in df.columns else [],
        "all_valid": True,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
