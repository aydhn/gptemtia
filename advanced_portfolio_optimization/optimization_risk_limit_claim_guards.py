# -*- coding: utf-8 -*-
"""Phase 154: Risk Limit Claim Guards."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_risk_limit_claim_guard_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build risk limit claim guard registry."""
    records = [{
        "guard_name": "optimization_risk_limit_claim_guard",
        "description": "Gercek risk limiti veya maruziyet tahsisi iddialarini engelleme",
        "is_active": True,
        "action_on_violation": "BLOCK",
    }]
    df = pd.DataFrame(records)
    summary = {
        "guard_name": "optimization_risk_limit_claim_guard",
        "is_active": True,
    }
    return df, summary


def validate_optimization_risk_limit_claim_request(request: Union[dict, str]) -> Dict:
    """Detect and block prohibited risk limit claims."""
    text = str(request).lower()
    prohibited = ["actual_risk_limit", "broker_margin_limit", "live_exposure_limit"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Risk limit claims strictly blocked" if blocked else "OK",
    }
