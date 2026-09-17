# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Metric Calculation Disabled Report."""

from typing import Any, Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
    DISABLED_EXEC_METRIC_CALCULATION,
    PORTFOLIO_CONTRACT_READY,
)


def build_portfolio_metric_calculation_disabled_report(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict, Any]:
    """Build DataFrame report certifying portfolio metric calculation is disabled."""
    rows = [
        {
            "operation": "portfolio_metric_calculation",
            "is_disabled": True,
            "policy_code": DISABLED_EXEC_METRIC_CALCULATION,
            "reason": "Phase 153 registers metric placeholders only; calculation of Sharpe, VaR, ES, HHI etc. is disabled.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
        "operation": "portfolio_metric_calculation",
        "is_disabled": True,
        "policy_code": DISABLED_EXEC_METRIC_CALCULATION,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
