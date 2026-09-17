# -*- coding: utf-8 -*-
"""Phase 147: Validation Prediction Disabled Report.

Documents and strictly enforces the disabled state of prediction and inference operations.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_validation_prediction_disabled_report(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled prediction generation."""
    rows = [
        {
            "execution_target": "model_inference_engine",
            "is_blocked": True,
            "reason": "Gercek model predict/inference cikarimi Faz 147'de kesinlikle engellenmistir.",
            "enforced": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_blocked_predictions": len(df),
        "all_blocked": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_validation_prediction_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate that request does not attempt prediction generation."""
    req_str = request if isinstance(request, str) else str(request.get("command", ""))
    req_lower = req_str.lower()
    blocked_keywords = ["predict", "inference", "generate_prediction", "target_label"]
    is_blocked = any(k in req_lower for k in blocked_keywords)
    return {
        "request": req_str,
        "is_safe": not is_blocked,
        "is_blocked": is_blocked,
        "message": "Tahmin/cikarim istegi engellendi." if is_blocked else "Talep guvenli.",
        "non_signal": True,
    }
