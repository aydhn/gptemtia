# -*- coding: utf-8 -*-
"""Phase 158: Model Training Disabled Report.

Certifies and enforces that model training and fitting are disabled.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_model_training_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build model training disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="MTD-001",
            execution_type="model_training",
            is_disabled=True,
            blocking_reason="Fitting ML models is forbidden in Phase 158.",
        ),
        SystemDisabledExecutionItem(
            item_id="MTD-002",
            execution_type="target_label_generation",
            is_disabled=True,
            blocking_reason="Generating target labels or supervised targets is forbidden.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_model_training",
        "non_signal": True,
    }
    return df, summary


def validate_no_model_training_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming payload does not request model training."""
    text = str(request).lower()
    forbidden_tokens = ["train", "fit", "target", "label"]
    found = [t for t in forbidden_tokens if t in text]
    return {
        "is_safe": len(found) == 0,
        "forbidden_tokens_detected": found,
        "blocked_by_policy": len(found) > 0,
        "non_signal": True,
    }
