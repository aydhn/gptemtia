# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Model Training Disabled Report."""

from typing import Any, Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
    DISABLED_EXEC_MODEL_TRAINING,
    PORTFOLIO_CONTRACT_READY,
)


def build_portfolio_model_training_disabled_report(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict, Any]:
    """Build DataFrame report certifying model training is disabled in portfolio construction."""
    rows = [
        {
            "operation": "portfolio_model_training",
            "is_disabled": True,
            "policy_code": DISABLED_EXEC_MODEL_TRAINING,
            "reason": "Phase 153 is a contract layer; no ML model training, fitting, or fine-tuning is permitted.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
        "operation": "portfolio_model_training",
        "is_disabled": True,
        "policy_code": DISABLED_EXEC_MODEL_TRAINING,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
