# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Domain Registry."""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_labels import ALL_DOMAINS


def build_risk_reporting_domain_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of all 28 Risk Reporting domains."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows: List[Dict[str, Any]] = []
    for d in ALL_DOMAINS:
        rows.append({
            "domain_name": d,
            "current_phase": profile.current_phase,
            "target_final_phase": profile.target_final_phase,
            "next_phase": profile.next_phase,
            "non_production": True,
            "dry_run": True,
            "local_only": True,
            "status": "active",
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain_count": len(df),
        "total_domains": len(df),
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
        "all_domains_non_production": True,
    }
    return df, summary
