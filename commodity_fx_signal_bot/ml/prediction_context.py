import pandas as pd
from typing import Tuple, Dict, Any, Optional

def build_model_context_features(prediction_df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Convert prediction pool dataframe to a context feature frame."""
    if prediction_df.empty:
        return pd.DataFrame(), {"status": "empty"}

    df = prediction_df.copy()

    # We want to create features per model or aggregated.
    # For context, let's just create features based on the best/latest candidate per timestamp
    # or aggregate if multiple models.

    # Sort by confidence so drop_duplicates keeps the highest confidence
    df = df.sort_values("confidence_score", ascending=False)
    df = df.drop_duplicates(subset=["timestamp"], keep="first").copy()
    df = df.set_index("timestamp")

    context_df = pd.DataFrame(index=df.index)

    # Map direction to code
    dir_map = {
        "predicted_up": 1,
        "predicted_down": -1,
        "predicted_flat": 0,
        "predicted_unknown": float('nan')
    }

    context_df["ml_predicted_direction_code"] = df["predicted_direction"].map(dir_map)
    context_df["ml_prediction_score"] = df["prediction_score"]
    context_df["ml_calibrated_score"] = df["calibrated_score"]
    context_df["ml_confidence_score"] = df["confidence_score"]
    context_df["ml_uncertainty_score"] = df["uncertainty_score"]

    context_df["ml_model_quality_score"] = df["model_quality_score"]
    context_df["ml_dataset_quality_score"] = df["dataset_quality_score"]
    context_df["ml_leakage_risk_score"] = df["leakage_risk_score"]

    context_df["ml_context_supportive"] = (df["prediction_context_label"] == "ml_context_supportive").astype(int)
    context_df["ml_context_conflicting"] = (df["prediction_context_label"] == "ml_context_conflicting").astype(int)
    context_df["ml_context_uncertain"] = (df["prediction_context_label"] == "ml_context_uncertain").astype(int)

    return context_df, {"status": "success", "rows": len(context_df)}

def build_ensemble_context_features(ensemble_df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if ensemble_df.empty:
        return pd.DataFrame(), {"status": "empty"}

    df = ensemble_df.copy()
    context_df = pd.DataFrame(index=df.index)

    dir_map = {
        "predicted_up": 1,
        "predicted_down": -1,
        "predicted_flat": 0,
        "predicted_unknown": float('nan')
    }

    if "ensemble_predicted_direction" in df.columns:
        context_df["ml_ensemble_direction_code"] = df["ensemble_predicted_direction"].map(dir_map)

    context_df["ml_ensemble_score"] = df.get("ensemble_prediction_score", float('nan'))
    context_df["ml_ensemble_confidence"] = df.get("ensemble_confidence_score", float('nan'))
    context_df["ml_ensemble_uncertainty"] = df.get("ensemble_uncertainty_score", float('nan'))
    context_df["ml_ensemble_disagreement"] = df.get("ensemble_disagreement_score", float('nan'))

    if "ensemble_context_label" in df.columns:
        context_df["ml_ensemble_supportive"] = (df["ensemble_context_label"] == "ml_context_supportive").astype(int)
        context_df["ml_ensemble_conflicting"] = (df["ensemble_context_label"] == "ml_context_conflicting").astype(int)
        context_df["ml_ensemble_uncertain"] = (df["ensemble_context_label"] == "ml_context_uncertain").astype(int)

    return context_df, {"status": "success", "rows": len(context_df)}

def merge_model_context_with_existing_features(
    model_context_df: pd.DataFrame,
    existing_context_df: Optional[pd.DataFrame] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if existing_context_df is None or existing_context_df.empty:
        return model_context_df.copy(), {"status": "merged_new"}

    if model_context_df.empty:
        return existing_context_df.copy(), {"status": "merged_existing"}

    merged = existing_context_df.join(model_context_df, how="left")
    return merged, {"status": "merged_both"}
