# -*- coding: utf-8 -*-
"""Phase 153: Position Sizing Execution Disabled Report."""

from typing import Any, Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
    DISABLED_EXEC_POSITION_SIZING,
    PORTFOLIO_CONTRACT_READY,
)


def build_position_sizing_execution_disabled_report(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying position sizing execution is disabled."""
    rows = [
        {
            "operation": "position_sizing_execution",
            "is_disabled": True,
            "policy_code": DISABLED_EXEC_POSITION_SIZING,
            "reason": "Phase 153 defines contracts only; calculating real position sizing (lot, shares) is disabled.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
        "operation": "position_sizing_execution",
        "is_disabled": True,
        "policy_code": DISABLED_EXEC_POSITION_SIZING,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
