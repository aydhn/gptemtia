# -*- coding: utf-8 -*-
"""Phase 138 Baseline Metric Placeholders Registry.

Defines metric placeholders strictly without calculating values or claiming
model performance.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

METRIC_PLACEHOLDERS_DATA = [
    {
        "metric_placeholder_id": "classification_metric_placeholder",
        "metric_category": "classification",
        "description": "Placeholder for binary/multiclass classification accuracy, F1, and log-loss without compute",
    },
    {
        "metric_placeholder_id": "regression_metric_placeholder",
        "metric_category": "regression",
        "description": "Placeholder for MSE, MAE, RMSE metrics without compute",
    },
    {
        "metric_placeholder_id": "ranking_metric_placeholder",
        "metric_category": "ranking",
        "description": "Placeholder for NDCG, spearman rank correlation without compute",
    },
    {
        "metric_placeholder_id": "calibration_metric_placeholder",
        "metric_category": "calibration",
        "description": "Placeholder for Brier score and expected calibration error (ECE) without compute",
    },
    {
        "metric_placeholder_id": "drift_metric_placeholder",
        "metric_category": "drift",
        "description": "Placeholder for prediction drift and population stability index (PSI) without compute",
    },
    {
        "metric_placeholder_id": "explainability_metric_placeholder",
        "metric_category": "explainability",
        "description": "Placeholder for SHAP / feature attribution metrics without compute",
    },
    {
        "metric_placeholder_id": "latency_metric_placeholder",
        "metric_category": "system",
        "description": "Placeholder for inference latency and batch throughput timing without compute",
    },
    {
        "metric_placeholder_id": "resource_usage_metric_placeholder",
        "metric_category": "system",
        "description": "Placeholder for GPU memory and CPU utilization profiling without compute",
    },
]


def build_baseline_metric_placeholder_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build metric placeholders DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for item in METRIC_PLACEHOLDERS_DATA:
        rows.append({
            "metric_placeholder_id": item["metric_placeholder_id"],
            "metric_category": item["metric_category"],
            "description": item["description"],
            "is_calculated": False,
            "calculated_value": None,
            "performance_claim_allowed": False,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_metric_placeholders(df)
    return df, summary


def summarize_baseline_metric_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize metric placeholders."""
    return {
        "total_placeholders": len(df),
        "all_uncalculated": bool((~df["is_calculated"]).all()) if not df.empty else True,
        "performance_claims_prohibited": bool((~df["performance_claim_allowed"]).all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
