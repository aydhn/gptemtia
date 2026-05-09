import pandas as pd
import numpy as np
from typing import Dict, Any, List, Optional

def calculate_probability_entropy(probabilities: Dict[str, float]) -> float:
    """Calculate normalized entropy of class probabilities. 1 = max uncertainty."""
    probs = list(probabilities.values())
    if not probs:
        return 1.0

    n_classes = len(probs)
    if n_classes <= 1:
        return 0.0

    probs = np.array(probs)
    # Filter out 0 to avoid log(0)
    probs = probs[probs > 0]

    entropy = -np.sum(probs * np.log(probs))
    max_entropy = np.log(n_classes)

    if max_entropy <= 0:
        return 0.0

    normalized = entropy / max_entropy
    return float(max(0.0, min(1.0, normalized)))

def calculate_margin_confidence(probabilities: Dict[str, float]) -> float:
    """Calculate confidence as margin between top 2 classes."""
    probs = sorted(probabilities.values(), reverse=True)
    if len(probs) < 2:
        return 1.0
    return float(max(0.0, min(1.0, probs[0] - probs[1])))

def calculate_uncertainty_from_confidence(confidence_score: Optional[float]) -> float:
    """Simple inverse fallback for uncertainty if entropy isn't available."""
    if confidence_score is None:
        return 1.0
    return 1.0 - confidence_score

def calculate_ensemble_disagreement(predictions: List[Dict[str, Any]]) -> float:
    """Calculate disagreement among ensemble models. 1 = total disagreement, 0 = unanimous."""
    if not predictions or len(predictions) <= 1:
        return 0.0

    directions = [p.get("predicted_direction", "unknown") for p in predictions]
    valid_directions = [d for d in directions if d not in ["unknown", "predicted_unknown"]]

    if not valid_directions:
        return 1.0

    # Simple measure: ratio of non-majority votes
    from collections import Counter
    counts = Counter(valid_directions)
    majority_count = counts.most_common(1)[0][1]

    disagreement = 1.0 - (majority_count / len(valid_directions))
    # Scale so max disagreement (e.g. 50/50) is near 1.0
    max_disagreement = 1.0 - (1.0 / len(counts)) if len(counts) > 1 else 0.0

    if max_disagreement <= 0:
        return 0.0

    return float(max(0.0, min(1.0, disagreement / max_disagreement)))

def build_uncertainty_report(prediction_df: pd.DataFrame) -> Dict[str, Any]:
    if prediction_df.empty:
        return {"calculated": False}

    if "uncertainty_score" in prediction_df.columns:
        return {
            "calculated": True,
            "mean_uncertainty": float(prediction_df["uncertainty_score"].mean()),
            "high_uncertainty_count": int((prediction_df["uncertainty_score"] > 0.6).sum())
        }
    return {"calculated": False}
