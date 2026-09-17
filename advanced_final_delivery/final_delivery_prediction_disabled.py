# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Prediction Disabled Report.

Documents and validates that prediction generation and inference are disabled.
"""

from typing import Dict, Tuple, Union
import re
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_DISABLED_EXECUTION_DOMAIN,
    EXECUTION_BLOCKED_NO_PREDICTION,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def build_final_delivery_prediction_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build prediction disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "model_inference", "disabled": True, "reason": "Model inference strictly disabled"},
        {"action": "forward_return_predict", "disabled": True, "reason": "Future return prediction disabled"},
        {"action": "probabilistic_forecasting", "disabled": True, "reason": "Forecasting strictly disabled"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "prediction_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_BLOCKED_NO_PREDICTION,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_no_final_delivery_prediction_request(request: Union[dict, str]) -> dict:
    """Validate request does not request prediction generation."""
    text = " ".join(str(v) for v in request.values()) if isinstance(request, dict) else str(request)
    blocked = bool(re.search(r"\b(predict_future|generate_prediction|run_inference|predict_return)\b", text.lower()))
    return {
        "is_safe": not blocked,
        "prediction_blocked": blocked,
        "message": "Prediction blocked by policy" if blocked else "Request verified no prediction",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if not blocked else EXECUTION_BLOCKED_NO_PREDICTION,
    }
