# -*- coding: utf-8 -*-
"""Phase 155: Portfolio Exposure Summary Contracts Registry."""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


DEFAULT_EXPOSURE_SUMMARY_CONTRACTS = [
    {
        "contract_name": "portfolio_gross_net_summary",
        "description": "Portfoy brut ve net exposure duzeylerini ozetleyen sozlesme",
        "is_placeholder": True,
        "is_calculated": False,
        "allows_execution": False,
    },
    {
        "contract_name": "portfolio_asset_class_breakdown_summary",
        "description": "Emtia ve doviz siniflari bazinda maruziyet dökümü ozet sozlesmesi",
        "is_placeholder": True,
        "is_calculated": False,
        "allows_execution": False,
    },
    {
        "contract_name": "portfolio_concentration_profile_summary",
        "description": "HHI ve ilk-K varlik yogunluk profili ozet sozlesmesi",
        "is_placeholder": True,
        "is_calculated": False,
        "allows_execution": False,
    },
]


def build_portfolio_exposure_summary_contract_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of portfolio exposure summary contracts."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for c in DEFAULT_EXPOSURE_SUMMARY_CONTRACTS:
        item = dict(c)
        item["current_phase"] = profile.current_phase
        item["target_final_phase"] = profile.target_final_phase
        item["next_phase"] = profile.next_phase
        rows.append(item)

    df = pd.DataFrame(rows)
    summary = {
        "summary_contract_count": len(df),
        "all_placeholder": bool(df["is_placeholder"].all()) if not df.empty else True,
        "zero_calculated": bool((df["is_calculated"] == False).all()) if not df.empty else True,
    }
    return df, summary
