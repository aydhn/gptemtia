# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Prediction Disabled Report."""

from typing import Any, Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
    DISABLED_EXEC_PREDICTION,
    PORTFOLIO_CONTRACT_READY,
)


def build_portfolio_prediction_disabled_report(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict, Any]:
    """Build DataFrame report certifying model prediction and inference are disabled."""
    rows = [
        {
            "operation": "portfolio_prediction",
            "is_disabled": True,
            "policy_code": DISABLED_EXEC_PREDICTION,
            "reason": "Phase 153 prohibits model inference, target return forecasting, or score generation.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
        "operation": "portfolio_prediction",
        "is_disabled": True,
        "policy_code": DISABLED_EXEC_PREDICTION,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
