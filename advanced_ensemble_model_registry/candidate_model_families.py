# -*- coding: utf-8 -*-
"""Phase 140: Candidate Model Families Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

CANDIDATE_MODEL_FAMILIES: List[Dict[str, Any]] = [
    {
        "family_id": "logistic_regression_candidate_contract",
        "family_name": "Logistic Regression Candidate",
        "family_category": "linear",
        "description": "Linear logistic regression candidate model contract placeholder.",
        "baseline_contract_ref": "baseline_logistic_regression_contract",
        "dataset_contract_ref": "dataset_contract_v137",
    },
    {
        "family_id": "ridge_regression_candidate_contract",
        "family_name": "Ridge Regression Candidate",
        "family_category": "linear",
        "description": "L2-regularized linear candidate model contract placeholder.",
        "baseline_contract_ref": "baseline_ridge_regression_contract",
        "dataset_contract_ref": "dataset_contract_v137",
    },
    {
        "family_id": "random_forest_candidate_contract",
        "family_name": "Random Forest Candidate",
        "family_category": "tree",
        "description": "Bagged decision tree candidate model contract placeholder.",
        "baseline_contract_ref": "baseline_random_forest_contract",
        "dataset_contract_ref": "dataset_contract_v137",
    },
    {
        "family_id": "gradient_boosting_candidate_contract",
        "family_name": "Gradient Boosting Candidate",
        "family_category": "boosting",
        "description": "Sequential gradient boosted tree candidate model contract placeholder.",
        "baseline_contract_ref": "baseline_gradient_boosting_contract",
        "dataset_contract_ref": "dataset_contract_v137",
    },
    {
        "family_id": "xgboost_candidate_contract",
        "family_name": "XGBoost Candidate",
        "family_category": "boosting",
        "description": "Extreme gradient boosting candidate contract placeholder.",
        "baseline_contract_ref": "baseline_xgboost_contract",
        "dataset_contract_ref": "dataset_contract_v137",
    },
    {
        "family_id": "lightgbm_candidate_contract",
        "family_name": "LightGBM Candidate",
        "family_category": "boosting",
        "description": "Histogram-based gradient boosting candidate contract placeholder.",
        "baseline_contract_ref": "baseline_lightgbm_contract",
        "dataset_contract_ref": "dataset_contract_v137",
    },
    {
        "family_id": "catboost_candidate_contract",
        "family_name": "CatBoost Candidate",
        "family_category": "boosting",
        "description": "Categorical feature-aware gradient boosting candidate contract placeholder.",
        "baseline_contract_ref": "baseline_catboost_contract",
        "dataset_contract_ref": "dataset_contract_v137",
    },
    {
        "family_id": "shallow_mlp_candidate_contract",
        "family_name": "Shallow MLP Candidate",
        "family_category": "neural",
        "description": "Multi-layer perceptron candidate model contract placeholder.",
        "baseline_contract_ref": "baseline_shallow_mlp_contract",
        "dataset_contract_ref": "dataset_contract_v137",
    },
    {
        "family_id": "sequence_model_candidate_contract",
        "family_name": "Sequence Model Candidate",
        "family_category": "sequence",
        "description": "Sequential/temporal candidate model contract placeholder.",
        "baseline_contract_ref": "baseline_sequence_model_contract",
        "dataset_contract_ref": "dataset_contract_v137",
    },
    {
        "family_id": "unsupervised_candidate_placeholder_contract",
        "family_name": "Unsupervised Candidate Placeholder",
        "family_category": "unsupervised_placeholder",
        "description": "Non-executing unsupervised candidate placeholder contract.",
        "baseline_contract_ref": "baseline_unsupervised_contract",
        "dataset_contract_ref": "dataset_contract_v137",
    },
]


def build_candidate_model_family_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build candidate model family registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for item in CANDIDATE_MODEL_FAMILIES:
        rows.append(
            {
                "family_id": item["family_id"],
                "family_name": item["family_name"],
                "family_category": item["family_category"],
                "description": item["description"],
                "baseline_contract_ref": item["baseline_contract_ref"],
                "dataset_contract_ref": item["dataset_contract_ref"],
                "is_placeholder": True,
                "model_instantiated": False,
                "model_fit_executed": False,
                "model_predict_executed": False,
                "real_training_allowed": False,
                "non_signal": True,
                "production_ready": False,
                "broker_ready": False,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_candidate_model_families(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_candidate_model_families(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize candidate model families DataFrame."""
    if df.empty:
        return {
            "total_families": 0,
            "all_placeholders": True,
            "zero_models_instantiated": True,
            "zero_training_executed": True,
            "non_signal": True,
        }
    return {
        "total_families": len(df),
        "all_placeholders": bool(df["is_placeholder"].all()),
        "zero_models_instantiated": not bool(df["model_instantiated"].any()),
        "zero_training_executed": not bool(df["model_fit_executed"].any()),
        "zero_predict_executed": not bool(df["model_predict_executed"].any()),
        "non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_candidate_model_families(df: pd.DataFrame, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate candidate model families DataFrame."""
    if df.empty:
        return False
    if not df["non_signal"].all():
        return False
    if df["model_fit_executed"].any() or df["model_predict_executed"].any() or df["model_instantiated"].any():
        return False
    return True


build_candidate_model_families = build_candidate_model_family_registry

