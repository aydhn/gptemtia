# -*- coding: utf-8 -*-
"""Phase 138 Dry-Run Training Harness Interface Specifications.

Defines permitted and strictly prohibited interfaces for baseline model trainers.
Permitted: validation, safety checks, simulation without fit, review reporting.
Prohibited: fit, train, predict, inference, transform, save_model, write_model_registry, etc.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

PERMITTED_INTERFACES = [
    {"method_name": "validate_contracts", "is_permitted": True, "category": "validation", "description": "Validates model and harness contracts"},
    {"method_name": "validate_inputs", "is_permitted": True, "category": "validation", "description": "Validates feature store and dataset inputs"},
    {"method_name": "check_safety_policies", "is_permitted": True, "category": "safety", "description": "Enforces zero-training and guard policies"},
    {"method_name": "simulate_training_plan_without_fit", "is_permitted": True, "category": "simulation", "description": "Dry-run plan validation without fitting models"},
    {"method_name": "return_blocked_execution_status", "is_permitted": True, "category": "execution", "description": "Returns safe blocked execution status dict"},
    {"method_name": "build_manual_review_report", "is_permitted": True, "category": "reporting", "description": "Generates inspection queue report"},
]

PROHIBITED_INTERFACES = [
    {"method_name": "fit", "is_permitted": False, "category": "execution", "description": "Forbidden model fitting"},
    {"method_name": "train", "is_permitted": False, "category": "execution", "description": "Forbidden model training"},
    {"method_name": "predict", "is_permitted": False, "category": "execution", "description": "Forbidden model prediction"},
    {"method_name": "inference", "is_permitted": False, "category": "execution", "description": "Forbidden forward pass inference"},
    {"method_name": "transform", "is_permitted": False, "category": "execution", "description": "Forbidden state transform"},
    {"method_name": "save_model", "is_permitted": False, "category": "persistence", "description": "Forbidden artifact dump"},
    {"method_name": "write_model_registry", "is_permitted": False, "category": "governance", "description": "Forbidden model registry write"},
    {"method_name": "run_backtest", "is_permitted": False, "category": "strategy", "description": "Forbidden backtest run"},
    {"method_name": "generate_signal", "is_permitted": False, "category": "strategy", "description": "Forbidden signal generation"},
]


def build_dry_run_training_harness_interface_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build interface specifications registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for item in PERMITTED_INTERFACES + PROHIBITED_INTERFACES:
        rows.append({
            "method_name": item["method_name"],
            "is_permitted": item["is_permitted"],
            "category": item["category"],
            "description": item["description"],
            "enforced_by_policy": True,
            "non_signal": True,
        })

    df = pd.DataFrame(rows)
    summary = summarize_dry_run_training_harness_interfaces(df)
    return df, summary


def validate_interface_permission(method_name: str) -> Dict[str, Any]:
    """Validate whether an interface method is permitted in Phase 138."""
    permitted_names = {item["method_name"] for item in PERMITTED_INTERFACES}
    prohibited_names = {item["method_name"] for item in PROHIBITED_INTERFACES}

    if method_name in prohibited_names:
        return {
            "method_name": method_name,
            "permitted": False,
            "status": "INTERFACE_METHOD_PROHIBITED",
            "reason": f"Method '{method_name}' is strictly prohibited in Phase 138 dry-run harness.",
            "non_signal": True,
        }
    if method_name in permitted_names:
        return {
            "method_name": method_name,
            "permitted": True,
            "status": "INTERFACE_METHOD_PERMITTED",
            "non_signal": True,
        }
    return {
        "method_name": method_name,
        "permitted": False,
        "status": "INTERFACE_METHOD_UNKNOWN",
        "reason": f"Method '{method_name}' is not recognized in interface specifications.",
        "non_signal": True,
    }


def summarize_dry_run_training_harness_interfaces(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize interface specifications."""
    permitted_count = int(df["is_permitted"].sum()) if not df.empty else 0
    prohibited_count = int((~df["is_permitted"]).sum()) if not df.empty else 0
    return {
        "total_interfaces": len(df),
        "permitted_count": permitted_count,
        "prohibited_count": prohibited_count,
        "fit_prohibited": "fit" in df[~df["is_permitted"]]["method_name"].values if not df.empty else True,
        "train_prohibited": "train" in df[~df["is_permitted"]]["method_name"].values if not df.empty else True,
        "predict_prohibited": "predict" in df[~df["is_permitted"]]["method_name"].values if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
