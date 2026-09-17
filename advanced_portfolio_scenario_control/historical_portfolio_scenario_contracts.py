# -*- coding: utf-8 -*-
"""Phase 156: Historical Portfolio Scenario Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_HISTORICAL_SCENARIOS = [
    {
        "scenario_id": "HIST-SCN-001",
        "historical_event": "2008 Global Financial Crisis (Lehman Shock)",
        "period_start": "2008-09-01",
        "period_end": "2008-11-30",
        "macro_backdrop": "Bankacilik krizi, likidite donmasi, genis capli varlik satis dalgasi",
        "observed_market_shock": "Emtia fiyatlarinda %50+ dusus, FX piyasasinda yuksek volatilite",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "HIST-SCN-002",
        "historical_event": "2020 COVID-19 Pandemic Flash Crash",
        "period_start": "2020-02-15",
        "period_end": "2020-04-30",
        "macro_backdrop": "Kuresel karantinalar, petrol fiyatinin negatif seviyeye inmesi",
        "observed_market_shock": "WTI negatif fiyat, kuresel FX paritelerinde sert kopmalar",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "HIST-SCN-003",
        "historical_event": "2022 Energy Shock and War Escalation",
        "period_start": "2022-02-20",
        "period_end": "2022-06-30",
        "macro_backdrop": "Jeopolitik catisma, dogalgaz ve bugday arz soklari, enflasyonist baski",
        "observed_market_shock": "Avrupa gaz fiyatlarinda %300 artis, tarimsal emtiada yuksek dalgalanma",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "HIST-SCN-004",
        "historical_event": "2011 US Debt Downgrade and European Sovereign Debt",
        "period_start": "2011-08-01",
        "period_end": "2011-10-31",
        "macro_backdrop": "ABD kredi notu indirimi ve Avrupa borc krizi soku",
        "observed_market_shock": "Altin rekor seviye, riskli varliklarda sert geri cekilme",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "HIST-SCN-005",
        "historical_event": "1997 Asian Financial Crisis Contagion",
        "period_start": "1997-07-01",
        "period_end": "1997-12-31",
        "macro_backdrop": "Gelisipte olan ulke kurlari devaluasyonu ve sermaye kacisi",
        "observed_market_shock": "Gelisipte olan FX kurlarinda %50+ deger kaybi",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_historical_portfolio_scenario_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for historical scenario contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_HISTORICAL_SCENARIOS)
    summary = {
        "total_historical_scenarios": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
