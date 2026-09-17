# -*- coding: utf-8 -*-
"""Phase 148: Macro Shock Scenario Placeholders.

Provides specifications and registry for central bank rate surprises and macroeconomic shock placeholders.
Model contract / formula metadata only; no actual macro simulation or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import ShockScenarioPlaceholder

MACRO_SHOCK_SPECS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "interest_rate_surprise_100bp_placeholder",
        "shock_type": "MONETARY_POLICY_SURPRISE",
        "description": "Merkez Bankası Acil Faiz Artışı (+100 bps Sürpriz) yer tutucusu.",
        "magnitude_spec": "+100_basis_points",
        "parameters": {"target_rate": "FED_FUNDS_OR_POLICY", "asset_impact": "CURRENCY_SURGE_COMMODITY_DROP"},
    },
    {
        "placeholder_name": "cpi_inflation_shock_plus_3pct_placeholder",
        "shock_type": "INFLATION_SURPRISE",
        "description": "Beklentilerin 300 bps Üzerinde Gelen TÜFE Enflasyon Şoku yer tutucusu.",
        "magnitude_spec": "+3.0pct_above_consensus",
        "parameters": {"asset_impact": "GOLD_RALLY_BOND_YIELD_SPIKE"},
    },
    {
        "placeholder_name": "gdp_contraction_recession_placeholder",
        "shock_type": "RECESSION_GROWTH_SHOCK",
        "description": "Ani Küresel Büyüme Daralması (-2.5% GSYH Şoku) yer tutucusu.",
        "magnitude_spec": "-2.5pct_annual_gdp",
        "parameters": {"asset_impact": "CRUDE_OIL_COPPER_DEMAND_CRASH"},
    },
]


def build_macro_shock_scenario_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of macro shock scenario placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in MACRO_SHOCK_SPECS:
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
        "total_macro_shocks": len(df),
        "all_execution_blocked": not bool(df["real_execution_allowed"].any()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
