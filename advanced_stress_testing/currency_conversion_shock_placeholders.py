# -*- coding: utf-8 -*-
"""Phase 148: Currency Conversion Shock Placeholders.

Provides specifications and registry for multi-currency conversion, base currency volatility,
and settlement haircut placeholders.
Model contract / formula metadata only; no actual currency exchange or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import ShockScenarioPlaceholder

CURRENCY_CONVERSION_SPECS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "usd_devaluation_rebalance_placeholder",
        "shock_type": "BASE_CURRENCY_DISRUPTION",
        "description": "Portföy Baz Para Biriminin (USD/TRY vb.) Ani Değer Kaybı ve Dönüşüm Kaybı yer tutucusu.",
        "magnitude_spec": "20pct_base_currency_swing",
        "parameters": {"conversion_friction_bps": 50},
    },
    {
        "placeholder_name": "cross_currency_settlement_haircut_placeholder",
        "shock_type": "SETTLEMENT_HAIRCUT",
        "description": "Farklı Para Birimlerindeki Teminat Değerlemesinde Stres İskontosu (Haircut) yer tutucusu.",
        "magnitude_spec": "15pct_collateral_haircut",
        "parameters": {"haircut_rate": 0.15},
    },
]


def build_currency_conversion_shock_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of currency conversion shock placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in CURRENCY_CONVERSION_SPECS:
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
        "total_currency_conversion_shocks": len(df),
        "all_execution_blocked": not bool(df["real_execution_allowed"].any()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
