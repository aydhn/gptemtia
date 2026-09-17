# -*- coding: utf-8 -*-
"""Phase 148: Historical Stress Scenario Contracts.

Provides specifications and registry for historical crisis scenario contracts
(GFC 2008, Covid Crash 2020, Negative Oil 2020, Flash Crash 2010, FX Depeg 2015, Energy Shock 2022).
Contract and metadata definition only; no actual historical data execution or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

HISTORICAL_SCENARIOS: List[Dict[str, Any]] = [
    {
        "scenario_name": "historical_gfc_2008_crisis",
        "crisis_period": "2008-09-01_to_2009-03-31",
        "description": "2008 Küresel Finans Krizi: Likidite çöküşü, hisse/emtia satış dalgası, USD değer kazanımı.",
        "primary_asset_impact": "EQUITY_COMMODITY_LIQUIDATION",
        "volatility_multiplier_ref": "3.5x",
        "spread_multiplier_ref": "4.0x",
        "execution_allowed": False,
        "pnl_calculation_allowed": False,
    },
    {
        "scenario_name": "historical_covid19_market_crash_2020",
        "crisis_period": "2020-02-20_to_2020-04-30",
        "description": "2020 Covid-19 Şoku: Küresel kapanma, anlık talep çöküşü, aşırı volatilite ve nakde kaçış.",
        "primary_asset_impact": "CROSS_ASSET_CORRELATION_ONE",
        "volatility_multiplier_ref": "4.0x",
        "spread_multiplier_ref": "5.0x",
        "execution_allowed": False,
        "pnl_calculation_allowed": False,
    },
    {
        "scenario_name": "historical_wti_negative_oil_2020",
        "crisis_period": "2020-04-15_to_2020-04-22",
        "description": "2020 Negatif Petrol Olayı: Fiziksel depolama kapasitesi tıkanması, WTI eksi fiyat anomalisi.",
        "primary_asset_impact": "COMMODITY_STORAGE_CONSTRAINTS",
        "volatility_multiplier_ref": "6.0x",
        "spread_multiplier_ref": "8.0x",
        "execution_allowed": False,
        "pnl_calculation_allowed": False,
    },
    {
        "scenario_name": "historical_flash_crash_2010",
        "crisis_period": "2010-05-06",
        "description": "2010 Flash Crash: Algoritmik likidite buharlaşması, anlık derin çöküş ve toparlanma.",
        "primary_asset_impact": "INTRADAY_LIQUIDITY_EVAPORATION",
        "volatility_multiplier_ref": "5.0x",
        "spread_multiplier_ref": "10.0x",
        "execution_allowed": False,
        "pnl_calculation_allowed": False,
    },
    {
        "scenario_name": "historical_chf_peg_break_2015",
        "crisis_period": "2015-01-15",
        "description": "2015 İsviçre Frangı Depeg: Ani kur rejimi sonlandırma, devasa fiyat boşluğu (gap) ve aracı kurum batışları.",
        "primary_asset_impact": "FX_DISCONTINUITY_GAP",
        "volatility_multiplier_ref": "7.0x",
        "spread_multiplier_ref": "15.0x",
        "execution_allowed": False,
        "pnl_calculation_allowed": False,
    },
    {
        "scenario_name": "historical_energy_shock_2022",
        "crisis_period": "2022-02-24_to_2022-08-31",
        "description": "2022 Jeopolitik Enerji Krizi: Doğalgaz, petrol ve tarım emtiasında arz şoku ve aşırı backwardation.",
        "primary_asset_impact": "COMMODITY_SUPPLY_SHOCK",
        "volatility_multiplier_ref": "3.0x",
        "spread_multiplier_ref": "3.5x",
        "execution_allowed": False,
        "pnl_calculation_allowed": False,
    },
]


def build_historical_stress_scenario_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of historical crisis scenario contracts."""
    rows: List[Dict[str, Any]] = []
    for s in HISTORICAL_SCENARIOS:
        rows.append(
            {
                "scenario_name": s["scenario_name"],
                "crisis_period": s["crisis_period"],
                "description": s["description"],
                "primary_asset_impact": s["primary_asset_impact"],
                "volatility_multiplier_ref": s["volatility_multiplier_ref"],
                "spread_multiplier_ref": s["spread_multiplier_ref"],
                "execution_allowed": s["execution_allowed"],
                "pnl_calculation_allowed": s["pnl_calculation_allowed"],
                "non_signal": True,
                "local_only": True,
                "manual_review_required": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_historical_scenarios": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_pnl_calculation_blocked": not bool(df["pnl_calculation_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
