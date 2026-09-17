# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Control Domain Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_DOMAINS = [
    {
        "domain_id": "DOM-156-001",
        "domain_name": "portfolio_scenario_testing_contracts",
        "description": "Portfoy stres, kriz ve sok senaryolari sozlesme altyapisi",
        "scope_count": 10,
        "is_contract_only": True,
        "execution_disabled": True,
    },
    {
        "domain_id": "DOM-156-002",
        "domain_name": "portfolio_drawdown_control_contracts",
        "description": "Portfoy drawdown esik, ihlal ve toparlanma sozlesme altyapisi",
        "scope_count": 8,
        "is_contract_only": True,
        "execution_disabled": True,
    },
    {
        "domain_id": "DOM-156-003",
        "domain_name": "portfolio_control_action_placeholders",
        "description": "Risk azaltma, de-risk, hedge, rebalance ve dondurma aksiyon yer tutuculari",
        "scope_count": 8,
        "is_contract_only": True,
        "execution_disabled": True,
    },
    {
        "domain_id": "DOM-156-004",
        "domain_name": "scenario_control_outputs_metrics",
        "description": "Senaryo ve drawdown kontrol cikti semalari ve metrik yer tutuculari",
        "scope_count": 12,
        "is_contract_only": True,
        "execution_disabled": True,
    },
    {
        "domain_id": "DOM-156-005",
        "domain_name": "portfolio_scenario_guards_governance",
        "description": "Lookahead, trade claim, broker execution ve snoop onleme korumalari",
        "scope_count": 14,
        "is_contract_only": True,
        "execution_disabled": True,
    },
]


def build_portfolio_scenario_control_domain_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Phase 156 domains."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_DOMAINS)
    summary = {
        "total_domains": len(df),
        "all_contract_only": bool(df["is_contract_only"].all()) if not df.empty else True,
        "all_execution_disabled": bool(df["execution_disabled"].all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
