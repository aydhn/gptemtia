# -*- coding: utf-8 -*-
"""Phase 138 Baseline Evaluation Placeholders Registry.

Defines evaluation protocol placeholders for dry-run contract, leakage,
lookahead, and governance checks without generating performance ratings.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

EVALUATION_PLACEHOLDERS_DATA = [
    {
        "evaluation_placeholder_id": "dry_run_contract_validation_placeholder",
        "evaluation_scope": "contract_integrity",
        "description": "Validates that all training plans run in contract-only mode",
    },
    {
        "evaluation_placeholder_id": "input_contract_validation_placeholder",
        "evaluation_scope": "input_data_integrity",
        "description": "Validates feature store and dataset contract references",
    },
    {
        "evaluation_placeholder_id": "no_leakage_validation_placeholder",
        "evaluation_scope": "leakage_prevention",
        "description": "Validates split barriers and purged window boundaries",
    },
    {
        "evaluation_placeholder_id": "no_lookahead_validation_placeholder",
        "evaluation_scope": "temporal_integrity",
        "description": "Validates absence of forward-looking timestamps and future return columns",
    },
    {
        "evaluation_placeholder_id": "metadata_only_news_validation_placeholder",
        "evaluation_scope": "content_compliance",
        "description": "Validates news streams contain only approved metadata tags",
    },
    {
        "evaluation_placeholder_id": "artifact_absence_validation_placeholder",
        "evaluation_scope": "artifact_governance",
        "description": "Validates that no binary model files or pickles are saved to disk",
    },
    {
        "evaluation_placeholder_id": "phase_139_gpu_resource_validation_placeholder",
        "evaluation_scope": "future_readiness",
        "description": "Validates GPU device and memory constraints for Phase 139 handoff",
    },
]


def build_baseline_evaluation_placeholder_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build evaluation placeholders DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for item in EVALUATION_PLACEHOLDERS_DATA:
        rows.append({
            "evaluation_placeholder_id": item["evaluation_placeholder_id"],
            "evaluation_scope": item["evaluation_scope"],
            "description": item["description"],
            "is_executed": False,
            "performance_claim_allowed": False,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_evaluation_placeholders(df)
    return df, summary


def summarize_baseline_evaluation_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize evaluation placeholders."""
    return {
        "total_evaluation_placeholders": len(df),
        "all_unexecuted": bool((~df["is_executed"]).all()) if not df.empty else True,
        "performance_claims_prohibited": bool((~df["performance_claim_allowed"]).all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
