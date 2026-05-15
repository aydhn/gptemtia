from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any
import hashlib
import pandas as pd
from ml.prediction_config import MLPredictionProfile

@dataclass
class MLPredictionCandidate:
    symbol: str
    timeframe: str
    timestamp: str
    prediction_id: str
    model_id: str
    model_family: str
    task_type: str
    target_column: str
    prediction_label: str
    predicted_direction: str
    prediction_context_label: str
    raw_prediction: Any
    predicted_value: Optional[float]
    prediction_score: Optional[float]
    calibrated_score: Optional[float]
    confidence_score: float
    uncertainty_score: float
    model_quality_score: float
    dataset_quality_score: float
    leakage_risk_score: float
    schema_compatible: bool
    passed_prediction_filters: bool
    warnings: List[str]
    notes: str = ""

def build_prediction_id(symbol: str, timeframe: str, timestamp: str, model_id: str, target_column: str) -> str:
    """Generate a deterministic ID for a prediction."""
    key = f"{symbol}_{timeframe}_{timestamp}_{model_id}_{target_column}"
    return hashlib.md5(key.encode()).hexdigest()

def prediction_candidate_to_dict(candidate: MLPredictionCandidate) -> Dict[str, Any]:
    return asdict(candidate)

def build_prediction_candidate_from_row(row: pd.Series, audit: Dict[str, Any], profile: MLPredictionProfile) -> MLPredictionCandidate:
    """Build a prediction candidate object from an inference output row and audit dict."""
    symbol = row.get("symbol", "UNKNOWN")
    timeframe = row.get("timeframe", "UNKNOWN")
    # if timestamp is index, it won't be in row if we iterate normally, but let's assume it's passed or extracted
    timestamp = str(row.name) if hasattr(row, "name") and not isinstance(row.name, int) else str(row.get("timestamp", ""))

    model_id = str(row.get("model_id", ""))
    target_column = str(row.get("target_column", ""))

    pred_id = build_prediction_id(symbol, timeframe, timestamp, model_id, target_column)

    confidence = float(row.get("confidence_score", 0.0))
    uncertainty = float(row.get("uncertainty_score", 1.0))

    # Evaluate labels
    if not audit.get("passed", False):
        pred_label = "prediction_candidate_rejected"
        passed = False
    elif confidence < profile.min_confidence_score:
        pred_label = "prediction_candidate_low_confidence"
        passed = False
    elif uncertainty > profile.uncertainty_warning_threshold:
        pred_label = "prediction_candidate_high_uncertainty"
        passed = profile.allow_warning_models
    else:
        pred_label = "prediction_candidate_ready"
        passed = True

    warnings = list(row.get("warnings", []))
    if not passed:
        warnings.append(f"Candidate failed filters. Label: {pred_label}")

    return MLPredictionCandidate(
        symbol=symbol,
        timeframe=timeframe,
        timestamp=timestamp,
        prediction_id=pred_id,
        model_id=model_id,
        model_family=str(row.get("model_family", "")),
        task_type=str(row.get("task_type", "")),
        target_column=target_column,
        prediction_label=pred_label,
        predicted_direction=str(row.get("predicted_direction", "predicted_unknown")),
        prediction_context_label=str(row.get("prediction_context_label", "ml_context_unavailable")),
        raw_prediction=row.get("raw_prediction"),
        predicted_value=row.get("predicted_value"),
        prediction_score=row.get("prediction_score"),
        calibrated_score=row.get("calibrated_score"),
        confidence_score=confidence,
        uncertainty_score=uncertainty,
        model_quality_score=float(audit.get("model_quality_score", 0.0)),
        dataset_quality_score=float(audit.get("dataset_quality_score", 0.0)),
        leakage_risk_score=float(audit.get("leakage_risk_score", 1.0)),
        schema_compatible=bool(audit.get("schema_compatible", False)),
        passed_prediction_filters=passed,
        warnings=warnings,
        notes=""
    )
