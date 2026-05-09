import pandas as pd
import numpy as np
from typing import Optional, Dict, Any

def calibrate_classification_probabilities(prob_df: pd.DataFrame, method: str = "identity") -> pd.DataFrame:
    """Calibrate probabilities. Currently identity, can be expanded to isotonic or sigmoid."""
    return prob_df.copy()

def normalize_classification_confidence(probabilities: Dict[str, float]) -> float:
    """Normalize confidence from a dictionary of probabilities. Returns max prob."""
    if not probabilities:
        return 0.5
    return float(max(probabilities.values()))

def normalize_regression_score(predicted_value: Optional[float], reference_volatility: Optional[float] = None) -> Optional[float]:
    """Map a regression value to a [0, 1] score. E.g. using reference volatility."""
    if predicted_value is None:
        return None

    # If we have a volatility reference, we can scale by it.
    if reference_volatility and reference_volatility > 0:
        z = predicted_value / reference_volatility
        # Map z-score loosely to 0-1 (sigmoid like)
        return 1 / (1 + np.exp(-z))

    # Fallback bounds if no reference
    # Assuming typical return values -0.05 to +0.05 mapping to 0 to 1
    clamped = max(-0.05, min(0.05, predicted_value))
    return (clamped + 0.05) / 0.10

def calculate_calibrated_prediction_score(row: pd.Series, task_type: str) -> Optional[float]:
    if "classification" in task_type.lower():
        # Look for probability column
        if "class_probability_up" in row and "class_probability_down" in row:
            # Score could be up prob
            return float(row.get("class_probability_up", 0.5))
        return float(row.get("confidence_score", 0.5))
    else:
        val = row.get("predicted_value")
        # without volatility reference, just use fallback
        return normalize_regression_score(val)

def build_calibration_report(prediction_df: pd.DataFrame) -> Dict[str, Any]:
    if prediction_df.empty:
        return {"calibrated": False}

    if "calibrated_score" in prediction_df.columns:
        return {
            "calibrated": True,
            "mean_score": float(prediction_df["calibrated_score"].mean()),
            "std_score": float(prediction_df["calibrated_score"].std())
        }
    return {"calibrated": False}
