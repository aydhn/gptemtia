# -*- coding: utf-8 -*-
"""Phase 158: Model Prediction Disabled Report.

Certifies and enforces that model inference and predictions are disabled.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_model_prediction_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build model prediction disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="MPD-001",
            execution_type="model_prediction",
            is_disabled=True,
            blocking_reason="Generating inference outputs or predictions is forbidden.",
        ),
        SystemDisabledExecutionItem(
            item_id="MPD-002",
            execution_type="directional_forecasting",
            is_disabled=True,
            blocking_reason="Directional forecast generation is forbidden.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_prediction",
        "non_signal": True,
    }
    return df, summary


def validate_no_model_prediction_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming payload does not request model predictions."""
    text = str(request).lower()
    forbidden_tokens = ["predict", "inference", "prediction"]
    found = [t for t in forbidden_tokens if t in text]
    return {
        "is_safe": len(found) == 0,
        "forbidden_tokens_detected": found,
        "blocked_by_policy": len(found) > 0,
        "non_signal": True,
    }
