# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
ML metric placeholder registry.

No metric calculation, no prediction, no target or label evaluation.
Pure metadata placeholders for future evaluation phases.
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)

METRIC_PLACEHOLDERS = [
    {
        "metric_family_key": "classification_metric_placeholder",
        "metric_group": "classification",
        "metrics": ["log_loss", "brier_score", "roc_auc", "f1_macro"],
        "description": "Classification evaluation metric placeholders for categorical regime target",
        "target_phase": 138,
        "calculation_allowed": False,
        "target_label_required": False,
        "prediction_required": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "metric_family_key": "regression_metric_placeholder",
        "metric_group": "regression",
        "metrics": ["mse", "mae", "directional_accuracy_placeholder"],
        "description": "Regression evaluation metric placeholders for continuous factor changes",
        "target_phase": 138,
        "calculation_allowed": False,
        "target_label_required": False,
        "prediction_required": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "metric_family_key": "calibration_metric_placeholder",
        "metric_group": "probability_calibration",
        "metrics": ["expected_calibration_error", "maximum_calibration_error"],
        "description": "Probability calibration diagnostic placeholders for Phase 141",
        "target_phase": 141,
        "calculation_allowed": False,
        "target_label_required": False,
        "prediction_required": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "metric_family_key": "ranking_metric_placeholder",
        "metric_group": "ranking_fidelity",
        "metrics": ["spearman_rank_correlation", "ndcg"],
        "description": "Cross-sectional ranking fidelity metric placeholders",
        "target_phase": 140,
        "calculation_allowed": False,
        "target_label_required": False,
        "prediction_required": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "metric_family_key": "drift_metric_placeholder",
        "metric_group": "model_drift",
        "metrics": ["prediction_drift_psi", "concept_drift_ks"],
        "description": "Model and concept drift metric placeholders for Phase 142",
        "target_phase": 142,
        "calculation_allowed": False,
        "target_label_required": False,
        "prediction_required": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "metric_family_key": "explainability_metric_placeholder",
        "metric_group": "attribution",
        "metrics": ["shap_attribution_placeholder", "permutation_importance_placeholder"],
        "description": "Feature attribution and explainability metric placeholders for Phase 143",
        "target_phase": 143,
        "calculation_allowed": False,
        "target_label_required": False,
        "prediction_required": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "metric_family_key": "robustness_metric_placeholder",
        "metric_group": "stress_testing",
        "metrics": ["subperiod_stability", "worst_regime_decay"],
        "description": "Subperiod stability and regime transition robustness placeholders",
        "target_phase": 144,
        "calculation_allowed": False,
        "target_label_required": False,
        "prediction_required": False,
        "non_signal": True,
        "manual_review_required": True,
    },
]


def build_ml_metric_placeholder_registry(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for ML metric placeholders."""
    p = profile or get_default_advanced_ml_dataset_profile()
    df = pd.DataFrame(METRIC_PLACEHOLDERS)
    summary = summarize_ml_metric_placeholders(df)
    return df, summary


def summarize_ml_metric_placeholders(df: pd.DataFrame) -> Dict:
    """Summarize metric placeholders."""
    return {
        "total_metric_families": len(df),
        "calculation_allowed": False,
        "target_label_required": False,
        "prediction_required": False,
        "non_signal": True,
        "manual_review_required": True,
    }
