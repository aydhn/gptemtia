# -*- coding: utf-8 -*-
"""Phase 155: Portfolio Optimization Dependencies Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


def build_risk_reporting_portfolio_optimization_dependency_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 154 portfolio optimization dependencies."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        {
            "dependency_name": "portfolio_optimization_contracts_dependency",
            "source_phase": 154,
            "target_phase": 155,
            "contract_type": "portfolio_optimization_spec",
            "status": "AVAILABLE_CONTRACT_ONLY",
        }
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"dependency_count": len(df), "is_satisfied": True}
