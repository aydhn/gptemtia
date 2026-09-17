# -*- coding: utf-8 -*-
"""Phase 153: Risk Budget Execution Disabled Report."""

from typing import Any, Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
    DISABLED_EXEC_RISK_BUDGETING,
    PORTFOLIO_CONTRACT_READY,
)


def build_risk_budget_execution_disabled_report(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict, Any]:
    """Build DataFrame report certifying risk budget execution is disabled."""
    rows = [
        {
            "operation": "risk_budget_execution",
            "is_disabled": True,
            "policy_code": DISABLED_EXEC_RISK_BUDGETING,
            "reason": "Phase 153 sets up placeholders and governance contracts; live risk budget enforcement is disabled.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
        "operation": "risk_budget_execution",
        "is_disabled": True,
        "policy_code": DISABLED_EXEC_RISK_BUDGETING,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
