# -*- coding: utf-8 -*-
"""Phase 148: Funding Rate Shock Placeholders.

Provides specifications and registry for financing costs, overnight swap, and funding rate shock placeholders.
Model contract / formula metadata only; no actual cost deduction or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import ShockScenarioPlaceholder

FUNDING_SHOCK_SPECS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "fx_swap_rate_spike_placeholder",
        "shock_type": "OVERNIGHT_FINANCING",
        "description": "Döviz Likidite Sıkışmasında Swap / Gecelik Taşıma Faizinin 5 Katına Çıkması yer tutucusu.",
        "magnitude_spec": "5x_baseline_swap_cost",
        "parameters": {"affected_pairs": "CROSS_AND_EM_FX", "holding_penalty_daily_bps": 25},
    },
    {
        "placeholder_name": "commodity_storage_financing_shock_placeholder",
        "shock_type": "COMMODITY_CARRY",
        "description": "Fiziksel Emtia Depolama, Sigorta ve Finansman Masraflarında %100 Artış yer tutucusu.",
        "magnitude_spec": "+100pct_carrying_cost",
        "parameters": {"affected_commodities": "METALS_AND_ENERGY"},
    },
]


def build_funding_rate_shock_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of funding rate shock placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in FUNDING_SHOCK_SPECS:
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
        "total_funding_rate_shocks": len(df),
        "all_execution_blocked": not bool(df["real_execution_allowed"].any()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
