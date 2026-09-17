# -*- coding: utf-8 -*-
"""Phase 148: Cross-Asset Contagion Scenario Placeholders.

Provides specifications and registry for cross-asset shock transmission and contagion placeholders.
Model contract / formula metadata only; no actual contagion simulation or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import ShockScenarioPlaceholder

CONTAGION_SPECS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "fx_to_commodity_contagion_placeholder",
        "shock_type": "CROSS_ASSET_TRANSMISSION",
        "description": "Gelişmekte Olan Para Birimlerinde Devalüasyonun Emtia İthalat Talebine Bulaşması.",
        "magnitude_spec": "30pct_currency_depreciation_leading_to_15pct_commodity_demand_drop",
        "parameters": {"source_asset_class": "FX", "target_asset_class": "COMMODITIES"},
    },
    {
        "placeholder_name": "bond_yield_spike_to_precious_metals_contagion_placeholder",
        "shock_type": "SOVEREIGN_TRANSMISSION",
        "description": "ABD 10 Yıllık Tahvil Faizlerinde Ani +75 bps Sıçramanın Değerli Metallere Bulaşması.",
        "magnitude_spec": "+75bps_real_yield_leading_to_sharp_gold_revaluation",
        "parameters": {"source_asset_class": "RATES", "target_asset_class": "PRECIOUS_METALS"},
    },
    {
        "placeholder_name": "energy_supply_crunch_to_industrial_metals_contagion_placeholder",
        "shock_type": "PRODUCTION_INPUT_TRANSMISSION",
        "description": "Enerji Arz Krizinin Elektrik Yoğun Sanayi Metalleri Üretimine Bulaşması (Bakır/Alüminyum).",
        "magnitude_spec": "+100pct_gas_power_cost_leading_to_smelter_shutdowns",
        "parameters": {"source_asset_class": "ENERGY", "target_asset_class": "BASE_METALS"},
    },
]


def build_cross_asset_contagion_scenario_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of cross-asset contagion scenario placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in CONTAGION_SPECS:
        placeholder = ShockScenarioPlaceholder(
            placeholder_name=spec["placeholder_name"],
            shock_type=spec["shock_type"],
            description=spec["description"],
            magnitude_spec=spec["magnitude_spec"],
            parameters=spec["parameters"],
            real_execution_allowed=False,
            non_signal=True,
            contains_trading_recommendation=False,
        )
        rows.append(
            {
                "placeholder_name": placeholder.placeholder_name,
                "shock_type": placeholder.shock_type,
                "description": placeholder.description,
                "magnitude_spec": placeholder.magnitude_spec,
                "parameters": str(placeholder.parameters),
                "real_execution_allowed": placeholder.real_execution_allowed,
                "non_signal": placeholder.non_signal,
                "contains_trading_recommendation": placeholder.contains_trading_recommendation,
                "manual_review_required": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_contagion_placeholders": len(df),
        "all_execution_blocked": not bool(df["real_execution_allowed"].any()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
