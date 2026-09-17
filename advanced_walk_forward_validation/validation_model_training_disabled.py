# -*- coding: utf-8 -*-
"""Phase 147: Validation Model Training Disabled Report.

Documents and strictly enforces the disabled state of model training and fit operations.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_validation_model_training_disabled_report(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled model training."""
    rows = [
        {
            "execution_target": "model_fit_engine",
            "is_blocked": True,
            "reason": "Gercek model fit/train calismasi Faz 147'de kesinlikle engellenmistir.",
            "enforced": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_blocked_training": len(df),
        "all_blocked": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_validation_model_training_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate that request does not attempt model training."""
    req_str = request if isinstance(request, str) else str(request.get("command", ""))
    req_lower = req_str.lower()
    blocked_keywords = ["train", "fit", "fine_tune", "model_training"]
    is_blocked = any(k in req_lower for k in blocked_keywords)
    return {
        "request": req_str,
        "is_safe": not is_blocked,
        "is_blocked": is_blocked,
        "message": "Model egitim istegi engellendi." if is_blocked else "Talep guvenli.",
        "non_signal": True,
    }
