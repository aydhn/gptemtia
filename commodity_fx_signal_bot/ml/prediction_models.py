from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any

@dataclass
class ModelPredictionOutput:
    model_id: str
    model_family: str
    task_type: str
    target_column: str
    timestamp: str
    raw_prediction: Any
    prediction_score: Optional[float]
    predicted_label: Optional[str]
    predicted_value: Optional[float]
    class_probabilities: Dict[str, float]
    confidence_score: float
    uncertainty_score: float
    warnings: List[str]

@dataclass
class PredictionAudit:
    model_id: str
    dataset_id: str
    leakage_audit_passed: bool
    dataset_quality_passed: bool
    model_quality_passed: bool
    schema_compatible: bool
    inference_rows: int
    warning_count: int
    passed: bool
    warnings: List[str]

def model_prediction_output_to_dict(output: ModelPredictionOutput) -> Dict[str, Any]:
    return asdict(output)

def prediction_audit_to_dict(audit: PredictionAudit) -> Dict[str, Any]:
    return asdict(audit)

def normalize_prediction_score(value: Optional[float], task_type: str) -> Optional[float]:
    """Normalize a raw prediction score to [0, 1] if possible."""
    if value is None:
        return None
    if task_type == "classification_prediction":
        # Usually already [0, 1] if it's a probability
        return max(0.0, min(1.0, value))
    elif task_type == "regression_prediction":
        # Simple sigmoid or bounds could be used, but without knowing the distribution it's tricky.
        # For this bot, if it's a probability proxy, bound it.
        # If it's pure forward return, it needs reference volatility calibration (handled in ScoreCalibration).
        return max(0.0, min(1.0, value))
    return None

def infer_predicted_direction_from_class(label: Optional[str]) -> str:
    """Map a raw class label to a predicted direction."""
    if label is None:
        return "predicted_unknown"
    label_lower = str(label).lower()
    if "up" in label_lower or "positive" in label_lower or label_lower in ["1", "1.0"]:
        return "predicted_up"
    elif "down" in label_lower or "negative" in label_lower or label_lower in ["-1", "-1.0"]:
        return "predicted_down"
    elif "flat" in label_lower or "neutral" in label_lower or label_lower in ["0", "0.0"]:
        return "predicted_flat"
    return "predicted_unknown"

def infer_prediction_context_label(predicted_direction: str, confidence_score: float, uncertainty_score: float) -> str:
    """Map confidence/uncertainty to a context label."""
    if predicted_direction == "predicted_unknown":
        return "ml_context_unavailable"
    if uncertainty_score > 0.60:
        return "ml_context_uncertain"
    if confidence_score > 0.60:
        return "ml_context_supportive"
    elif confidence_score > 0.40:
        return "ml_context_neutral"
    else:
        return "ml_context_conflicting" # Low confidence could mean conflict or weak signal
