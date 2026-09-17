# -*- coding: utf-8 -*-
"""Phase 155: Portfolio Construction Dependencies Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


def build_risk_reporting_portfolio_construction_dependency_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 153 portfolio construction dependencies."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        {
            "dependency_name": "portfolio_construction_contracts_dependency",
            "source_phase": 153,
            "target_phase": 155,
            "contract_type": "portfolio_construction_spec",
            "status": "AVAILABLE_CONTRACT_ONLY",
        }
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"dependency_count": len(df), "is_satisfied": True}
