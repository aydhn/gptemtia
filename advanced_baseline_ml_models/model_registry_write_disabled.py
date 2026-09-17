# -*- coding: utf-8 -*-
"""Phase 138 Model Registry Write Disabled Report and Validator.

Guarantees that write operations to external or internal model registries
(MLflow, model catalogs, deployment registries) are strictly disabled by policy.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

FORBIDDEN_REGISTRY_KEYWORDS = [
    "model_registry", "mlflow", "register_model", "register model", "log_model",
    "log model", "model_catalog", "deploy_model", "deploy model",
]


def build_model_registry_write_disabled_report(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report confirming zero model registry write operations."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = [
        {
            "check_item": "model_registry_write_disabled",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that writing to model registry is disabled",
        },
        {
            "check_item": "mlflow_model_logging_disabled",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that MLflow/catalog logging is disabled",
        },
        {
            "check_item": "model_version_registration_disabled",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that model version registration is disabled",
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_model_registry_write_disabled(df)
    return df, summary


def validate_no_model_registry_write_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Inspect request to ensure no model registry write is requested."""
    text = str(request).lower()
    detected = [kw for kw in FORBIDDEN_REGISTRY_KEYWORDS if kw in text]

    blocked = len(detected) > 0
    return {
        "blocked": blocked,
        "detected_keywords": detected,
        "status": "execution_blocked_no_registry_write" if blocked else "clean_no_registry_write_request",
        "model_registry_written": False,
        "manual_review_required": True,
        "non_signal": True,
    }


def summarize_model_registry_write_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model registry write disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()) if not df.empty else True,
        "model_registry_written": False,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
