# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Model family placeholder registry.

No model import, fit, train, predict, transform, or clustering execution.
Pure metadata placeholders for future Phase 138+ model family integration.
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)

MODEL_FAMILIES = [
    {
        "model_family_key": "logistic_regression_placeholder",
        "category": "linear_baseline",
        "description": "Linear logistic regression baseline placeholder for tabular regime features",
        "target_phase": 138,
        "is_executable_in_phase_137": False,
        "model_training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "model_family_key": "random_forest_placeholder",
        "category": "tree_ensemble_baseline",
        "description": "Random Forest non-linear ensemble baseline placeholder",
        "target_phase": 138,
        "is_executable_in_phase_137": False,
        "model_training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "model_family_key": "gradient_boosting_placeholder",
        "category": "gradient_boosting_baseline",
        "description": "Standard gradient boosting decision tree baseline placeholder",
        "target_phase": 138,
        "is_executable_in_phase_137": False,
        "model_training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "model_family_key": "xgboost_placeholder",
        "category": "gpu_accelerated_tree",
        "description": "XGBoost GPU/CPU tree boosting placeholder for Phase 138/139",
        "target_phase": 139,
        "is_executable_in_phase_137": False,
        "model_training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "model_family_key": "lightgbm_placeholder",
        "category": "fast_histogram_tree",
        "description": "LightGBM histogram-based tree boosting placeholder",
        "target_phase": 139,
        "is_executable_in_phase_137": False,
        "model_training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "model_family_key": "catboost_placeholder",
        "category": "categorical_tree",
        "description": "CatBoost robust categorical boosting placeholder",
        "target_phase": 139,
        "is_executable_in_phase_137": False,
        "model_training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "model_family_key": "shallow_neural_network_placeholder",
        "category": "neural_baseline",
        "description": "Shallow MLP / Feedforward neural net placeholder for tabular feature fusion",
        "target_phase": 139,
        "is_executable_in_phase_137": False,
        "model_training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "model_family_key": "sequence_model_placeholder",
        "category": "temporal_sequence",
        "description": "Temporal sequence model placeholder (LSTM/GRU/Temporal Convolution)",
        "target_phase": 139,
        "is_executable_in_phase_137": False,
        "model_training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "model_family_key": "unsupervised_model_placeholder",
        "category": "representation_learning",
        "description": "Unsupervised manifold / dimensionality reduction placeholder (PCA/UMAP)",
        "target_phase": 140,
        "is_executable_in_phase_137": False,
        "model_training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "model_family_key": "ensemble_placeholder",
        "category": "meta_ensemble",
        "description": "Stacking / Blending meta-model candidate placeholder for Phase 140",
        "target_phase": 140,
        "is_executable_in_phase_137": False,
        "model_training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
]


def build_ml_model_family_placeholder_registry(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for ML model family placeholders."""
    p = profile or get_default_advanced_ml_dataset_profile()
    df = pd.DataFrame(MODEL_FAMILIES)
    summary = summarize_ml_model_family_placeholders(df)
    return df, summary


def summarize_ml_model_family_placeholders(df: pd.DataFrame) -> Dict:
    """Summarize model family placeholders."""
    return {
        "total_model_families": len(df),
        "all_executable_blocked": bool((df["is_executable_in_phase_137"] == False).all()),
        "training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    }
