# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Live Trading Disabled Report."""

from typing import Any, Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
    DISABLED_EXEC_LIVE_TRADING,
    PORTFOLIO_CONTRACT_READY,
)


def build_portfolio_live_trading_disabled_report(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict, Any]:
    """Build DataFrame report certifying live trading is strictly disabled."""
    rows = [
        {
            "operation": "portfolio_live_trading",
            "is_disabled": True,
            "policy_code": DISABLED_EXEC_LIVE_TRADING,
            "reason": "Phase 153 is an offline research and contract phase; live trading and real capital dispatch are strictly forbidden.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
        "operation": "portfolio_live_trading",
        "is_disabled": True,
        "policy_code": DISABLED_EXEC_LIVE_TRADING,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
