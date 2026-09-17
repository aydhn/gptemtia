# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Meta-Model Placeholders Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

META_MODEL_PLACEHOLDERS = [
    {
        "placeholder_id": "linear_meta_model_placeholder",
        "meta_model_type": "linear_regression",
        "description": "Linear meta-learner contract placeholder (model training blocked).",
    },
    {
        "placeholder_id": "ridge_meta_model_placeholder",
        "meta_model_type": "ridge_regression",
        "description": "L2-regularized linear meta-learner contract placeholder (model training blocked).",
    },
    {
        "placeholder_id": "gradient_boosting_meta_model_placeholder",
        "meta_model_type": "gradient_boosting",
        "description": "Tree-based secondary meta-learner contract placeholder (model training blocked).",
    },
]


def build_ensemble_meta_model_placeholder_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build meta-model placeholder registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for mp in META_MODEL_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_id": mp["placeholder_id"],
                "meta_model_type": mp["meta_model_type"],
                "description": mp["description"],
                "training_blocked": True,
                "meta_model_trained": False,
                "meta_model_fitted": False,
                "non_signal": True,
                "source_preserved": True,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ensemble_meta_model_placeholders(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_ensemble_meta_model_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize meta-model placeholders DataFrame."""
    if df.empty:
        return {
            "total_meta_model_placeholders": 0,
            "all_training_blocked": True,
            "zero_models_trained": True,
            "non_signal": True,
        }
    return {
        "total_meta_model_placeholders": len(df),
        "all_training_blocked": bool(df["training_blocked"].all()),
        "zero_models_trained": not bool(df["meta_model_trained"].any()),
        "zero_models_fitted": not bool(df["meta_model_fitted"].any()),
        "non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_ensemble_meta_model_placeholders(placeholders: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate ensemble meta-model placeholders."""
    if isinstance(placeholders, tuple):
        df = placeholders[0]
    elif isinstance(placeholders, pd.DataFrame):
        df = placeholders
    elif isinstance(placeholders, dict):
        return all(not p.get("meta_model_trained", False) for p in placeholders.values())
    else:
        return False
    if df.empty:
        return False
    if df["meta_model_trained"].any() or df["meta_model_fitted"].any():
        return False
    if not df["non_signal"].all():
        return False
    return True


build_ensemble_meta_model_placeholders = build_ensemble_meta_model_placeholder_registry

