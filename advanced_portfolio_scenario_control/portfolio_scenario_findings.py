# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Findings Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_FINDINGS = [
    {
        "finding_id": "FND-156-001",
        "domain": "scenario_contract_integrity",
        "severity": "INFO",
        "description": "Tum senaryo ve drawdown kontrol sozlesmeleri offline ve contract_only modunda kuruldu",
        "manual_review_required": False,
        "status": "RESOLVED",
    },
    {
        "finding_id": "FND-156-002",
        "domain": "non_signal_invariance",
        "severity": "INFO",
        "description": "Sinyal uretilmedi, gercek emir verilmedi, portfoy degistirilmedi",
        "manual_review_required": False,
        "status": "RESOLVED",
    },
]

def build_portfolio_scenario_findings_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    df = pd.DataFrame(DEFAULT_FINDINGS)
    summary = {
        "total_findings": len(df),
        "critical_count": 0,
        "manual_review_required_count": int(df["manual_review_required"].sum()) if not df.empty else 0,
        "current_phase": profile.current_phase,
    }
    return df, summary
