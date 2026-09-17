# -*- coding: utf-8 -*-
"""Phase 154: Prediction Disabled Report & Policy."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_prediction_disabled_report(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build prediction disabled report table."""
    records = [{
        "component_name": "optimization_prediction",
        "is_disabled": True,
        "enforcement_mechanism": "runtime_policy_lock",
        "prohibited_actions": "predict, inference, forecast",
        "status": "execution_blocked_no_prediction",
    }]
    df = pd.DataFrame(records)
    summary = {
        "prediction_disabled": True,
        "runtime_policy_lock_active": True,
    }
    return df, summary


def validate_no_optimization_prediction_request(request: Union[dict, str]) -> Dict:
    """Ensure no request invokes model prediction."""
    text = str(request).lower()
    prohibited = ["predict", "inference", "forecast", "target_label"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Prediction is strictly blocked by Phase 154 policy" if blocked else "OK",
    }
