# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Output Contracts Registry.

Defines the output boundary: strictly prohibited from outputting predictions,
class labels, regression estimates, probabilities, or trade signals.
Permits only dry-run status, contract validation results, and review notifications.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_families import BASELINE_MODEL_FAMILIES_DATA


def build_baseline_model_output_contract_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build output contract registry DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for fam in BASELINE_MODEL_FAMILIES_DATA:
        rows.append({
            "output_contract_id": f"output_contract_{fam['family_id']}",
            "model_contract_ref": f"contract_{fam['family_id']}",
            "allowed_outputs": "dry_run_status, blocked_reason, contract_validation_status, manual_review_required",
            "prediction_output_allowed": False,
            "probability_output_allowed": False,
            "class_label_allowed": False,
            "regression_output_allowed": False,
            "trade_signal_allowed": False,
            "performance_metric_allowed": False,
            "contains_target_or_prediction": False,
            "contains_trading_recommendation": False,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_output_contracts(df)
    return df, summary


def summarize_baseline_model_output_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline model output contracts."""
    return {
        "total_output_contracts": len(df),
        "all_predictions_prohibited": bool((~df["prediction_output_allowed"]).all()) if not df.empty else True,
        "all_probabilities_prohibited": bool((~df["probability_output_allowed"]).all()) if not df.empty else True,
        "all_class_labels_prohibited": bool((~df["class_label_allowed"]).all()) if not df.empty else True,
        "all_regression_prohibited": bool((~df["regression_output_allowed"]).all()) if not df.empty else True,
        "all_trade_signals_prohibited": bool((~df["trade_signal_allowed"]).all()) if not df.empty else True,
        "all_metrics_prohibited": bool((~df["performance_metric_allowed"]).all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
