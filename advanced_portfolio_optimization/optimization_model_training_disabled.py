# -*- coding: utf-8 -*-
"""Phase 154: Model Training Disabled Report & Policy."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_model_training_disabled_report(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build model training disabled report table."""
    records = [{
        "component_name": "optimization_model_training",
        "is_disabled": True,
        "enforcement_mechanism": "runtime_policy_lock",
        "prohibited_actions": "fit, train, backward, gradient_step",
        "status": "execution_blocked_no_model_training",
    }]
    df = pd.DataFrame(records)
    summary = {
        "model_training_disabled": True,
        "runtime_policy_lock_active": True,
    }
    return df, summary


def validate_no_optimization_model_training_request(request: Union[dict, str]) -> Dict:
    """Ensure no request invokes model training."""
    text = str(request).lower()
    prohibited = ["fit", "train", "backward", "gradient_step"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Model training is strictly blocked by Phase 154 policy" if blocked else "OK",
    }
