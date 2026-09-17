# -*- coding: utf-8 -*-
"""Phase 154: Deployment Disabled Report & Policy."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_deployment_disabled_report(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build deployment disabled report table."""
    records = [{
        "component_name": "optimization_deployment",
        "is_disabled": True,
        "enforcement_mechanism": "runtime_policy_lock",
        "prohibited_actions": "deploy, publish, production_release",
        "status": "execution_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "deployment_disabled": True,
        "runtime_policy_lock_active": True,
    }
    return df, summary


def validate_no_optimization_deployment_request(request: Union[dict, str]) -> Dict:
    """Ensure no request invokes deployment."""
    text = str(request).lower()
    prohibited = ["deploy", "publish", "production_release", "deploy_portfolio"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Deployment is strictly blocked by Phase 154 policy" if blocked else "OK",
    }
