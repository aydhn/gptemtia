# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Execution Disabled Report."""

from typing import Any, Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
    DISABLED_EXEC_PORTFOLIO_CONSTRUCTION,
    PORTFOLIO_CONTRACT_READY,
)


def build_portfolio_construction_execution_disabled_report(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying portfolio construction execution is disabled."""
    rows = [
        {
            "operation": "portfolio_construction_execution",
            "is_disabled": True,
            "policy_code": DISABLED_EXEC_PORTFOLIO_CONSTRUCTION,
            "reason": "Phase 153 is strictly contract-only; automated portfolio construction execution is disabled.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
        "operation": "portfolio_construction_execution",
        "is_disabled": True,
        "policy_code": DISABLED_EXEC_PORTFOLIO_CONSTRUCTION,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
