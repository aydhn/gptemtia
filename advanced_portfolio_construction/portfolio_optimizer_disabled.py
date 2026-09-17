# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Optimizer Disabled Report."""

from typing import Any, Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
    DISABLED_EXEC_OPTIMIZER,
    PORTFOLIO_CONTRACT_READY,
)


def build_portfolio_optimizer_disabled_report(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict, Any]:
    """Build DataFrame report certifying portfolio optimizer execution is disabled."""
    rows = [
        {
            "operation": "portfolio_optimizer_execution",
            "is_disabled": True,
            "policy_code": DISABLED_EXEC_OPTIMIZER,
            "reason": "Phase 153 is offline contract specification; numerical optimizer execution (e.g., quadratic programming, scipy) is disabled.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
        "operation": "portfolio_optimizer_execution",
        "is_disabled": True,
        "policy_code": DISABLED_EXEC_OPTIMIZER,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
