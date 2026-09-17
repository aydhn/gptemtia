# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Deployment Disabled Report."""

from typing import Any, Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
    DISABLED_EXEC_DEPLOYMENT,
    PORTFOLIO_CONTRACT_READY,
)


def build_portfolio_deployment_disabled_report(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict, Any]:
    """Build DataFrame report certifying deployment is disabled for portfolio construction."""
    rows = [
        {
            "operation": "portfolio_deployment",
            "is_disabled": True,
            "policy_code": DISABLED_EXEC_DEPLOYMENT,
            "reason": "Phase 153 is local/offline contract design; production deployment and orchestration triggers are disabled.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
        "operation": "portfolio_deployment",
        "is_disabled": True,
        "policy_code": DISABLED_EXEC_DEPLOYMENT,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
