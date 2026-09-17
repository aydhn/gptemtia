# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Model Training Disabled Report.

Documents and validates that machine learning training and model fitting are disabled.
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
    EXECUTION_BLOCKED_NO_MODEL_TRAINING,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def build_final_delivery_model_training_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build model training disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "model_fit", "disabled": True, "reason": "Model fitting strictly disabled"},
        {"action": "hyperparameter_tuning", "disabled": True, "reason": "Automated hyperparameter search disabled"},
        {"action": "neural_net_train", "disabled": True, "reason": "Deep learning backpropagation disabled"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "model_training_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_BLOCKED_NO_MODEL_TRAINING,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_no_final_delivery_model_training_request(request: Union[dict, str]) -> dict:
    """Validate request does not request model training."""
    text = " ".join(str(v) for v in request.values()) if isinstance(request, dict) else str(request)
    blocked = bool(re.search(r"\b(train_model|fit_model|run_training|retrain_model)\b", text.lower()))
    return {
        "is_safe": not blocked,
        "training_blocked": blocked,
        "message": "Model training blocked by policy" if blocked else "Request verified no model training",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if not blocked else EXECUTION_BLOCKED_NO_MODEL_TRAINING,
    }
