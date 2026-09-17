# -*- coding: utf-8 -*-
"""Phase 153: Allocation Generation Disabled Report."""

from typing import Any, Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
    DISABLED_EXEC_ALLOCATION_GENERATION,
    PORTFOLIO_CONTRACT_READY,
)


def build_allocation_generation_disabled_report(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict, Any]:
    """Build DataFrame report certifying capital allocation and weight generation are disabled."""
    rows = [
        {
            "operation": "allocation_generation",
            "is_disabled": True,
            "policy_code": DISABLED_EXEC_ALLOCATION_GENERATION,
            "reason": "Phase 153 prohibits real capital allocation or target portfolio weight generation.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_DISABLED_EXECUTION_DOMAIN,
        "operation": "allocation_generation",
        "is_disabled": True,
        "policy_code": DISABLED_EXEC_ALLOCATION_GENERATION,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
