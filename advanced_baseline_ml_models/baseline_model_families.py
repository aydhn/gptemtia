# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Families Registry.

Defines baseline model family specifications strictly at the metadata and contract level.
No machine learning algorithms are imported, instantiated, fit, or predicted.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

BASELINE_MODEL_FAMILIES_DATA = [
    {
        "family_id": "logistic_regression_baseline_contract",
        "family_name": "Logistic Regression Baseline Contract",
        "algorithm_category": "linear_model",
        "library_name": "scikit-learn",
        "description": "Linear classification baseline contract placeholder for feature baseline benchmarks.",
        "tags": ["linear", "classification", "baseline"],
    },
    {
        "family_id": "ridge_regression_baseline_contract",
        "family_name": "Ridge Regression Baseline Contract",
        "algorithm_category": "linear_model",
        "library_name": "scikit-learn",
        "description": "L2-regularized linear regression baseline contract placeholder.",
        "tags": ["linear", "regression", "regularized", "baseline"],
    },
    {
        "family_id": "random_forest_baseline_contract",
        "family_name": "Random Forest Baseline Contract",
        "algorithm_category": "tree_ensemble",
        "library_name": "scikit-learn",
        "description": "Bagged decision tree baseline contract placeholder for non-linear benchmark comparison.",
        "tags": ["tree", "ensemble", "bagging", "baseline"],
    },
    {
        "family_id": "gradient_boosting_baseline_contract",
        "family_name": "Gradient Boosting Baseline Contract",
        "algorithm_category": "tree_ensemble",
        "library_name": "scikit-learn",
        "description": "Sequential boosting decision tree baseline contract placeholder.",
        "tags": ["tree", "ensemble", "boosting", "baseline"],
    },
    {
        "family_id": "xgboost_baseline_contract",
        "family_name": "XGBoost Baseline Contract",
        "algorithm_category": "gradient_boosting",
        "library_name": "xgboost",
        "description": "Optimized distributed gradient boosting baseline contract placeholder.",
        "tags": ["xgboost", "tree", "gradient_boosting", "gpu_ready"],
    },
    {
        "family_id": "lightgbm_baseline_contract",
        "family_name": "LightGBM Baseline Contract",
        "algorithm_category": "gradient_boosting",
        "library_name": "lightgbm",
        "description": "Fast histogram-based gradient boosting baseline contract placeholder.",
        "tags": ["lightgbm", "tree", "gradient_boosting", "histogram"],
    },
    {
        "family_id": "catboost_baseline_contract",
        "family_name": "CatBoost Baseline Contract",
        "algorithm_category": "gradient_boosting",
        "library_name": "catboost",
        "description": "Categorical feature-aware gradient boosting baseline contract placeholder.",
        "tags": ["catboost", "tree", "categorical", "gpu_ready"],
    },
    {
        "family_id": "shallow_mlp_baseline_contract",
        "family_name": "Shallow MLP Baseline Contract",
        "algorithm_category": "neural_network",
        "library_name": "torch",
        "description": "1-2 layer shallow multi-layer perceptron neural baseline contract placeholder.",
        "tags": ["neural_network", "mlp", "pytorch", "gpu_ready"],
    },
    {
        "family_id": "sequence_model_baseline_contract",
        "family_name": "Sequence Model Baseline Contract",
        "algorithm_category": "sequence_model",
        "library_name": "torch",
        "description": "Simple recurrent/temporal convolution baseline contract placeholder.",
        "tags": ["sequence", "temporal", "pytorch", "gpu_ready"],
    },
    {
        "family_id": "unsupervised_model_placeholder_contract",
        "family_name": "Unsupervised Model Placeholder Contract",
        "algorithm_category": "unsupervised",
        "library_name": "scikit-learn",
        "description": "PCA / clustering / dimensionality reduction contract placeholder.",
        "tags": ["unsupervised", "clustering", "pca", "placeholder"],
    },
]


def build_baseline_model_family_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for baseline model family registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for item in BASELINE_MODEL_FAMILIES_DATA:
        rows.append({
            "family_id": item["family_id"],
            "family_name": item["family_name"],
            "algorithm_category": item["algorithm_category"],
            "library_name": item["library_name"],
            "description": item["description"],
            "is_contract_only": True,
            "real_training_allowed": False,
            "model_fit_allowed": False,
            "model_predict_allowed": False,
            "inference_allowed": False,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
            "official_approval": False,
            "tags": ", ".join(item["tags"]),
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_families(df)
    return df, summary


def summarize_baseline_model_families(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline model families."""
    return {
        "total_families": len(df),
        "algorithm_categories": sorted(df["algorithm_category"].unique().tolist()) if not df.empty else [],
        "libraries": sorted(df["library_name"].unique().tolist()) if not df.empty else [],
        "all_contract_only": bool(df["is_contract_only"].all()) if not df.empty else True,
        "zero_real_training": bool((~df["real_training_allowed"]).all()) if not df.empty else True,
        "zero_prediction": bool((~df["model_predict_allowed"]).all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
