# -*- coding: utf-8 -*-
"""Phase 155: Exposure Attribution Output Contracts Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


def build_exposure_attribution_output_contract_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for exposure attribution output contracts."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        {
            "output_name": "exposure_attribution_output_contract",
            "contract_validation_status": "exposure_attribution_contract_ready",
            "blocked_reason": "execution_contract_only",
            "manual_review_required": True,
            "actual_attribution_generated": False,
            "capital_allocation_recommended": False,
        }
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"output_contract_count": len(df), "status": "exposure_attribution_contract_ready"}
