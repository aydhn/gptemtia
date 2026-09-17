# -*- coding: utf-8 -*-
"""Phase 155: Backtest Acceptance Dependencies Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


def build_risk_reporting_backtest_acceptance_dependency_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 152 backtest acceptance dependencies."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        {
            "dependency_name": "backtest_acceptance_dependency",
            "source_phase": 152,
            "target_phase": 155,
            "contract_type": "acceptance_report_spec",
            "status": "AVAILABLE_CONTRACT_ONLY",
        }
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"dependency_count": len(df), "is_satisfied": True}
