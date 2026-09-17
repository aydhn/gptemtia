# -*- coding: utf-8 -*-
"""Phase 148: Market Impact Shock Placeholders.

Provides specifications and registry for non-linear market impact, square-root law,
and liquidity exhaustion placeholders.
Model contract / formula metadata only; no actual market impact simulation or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import ShockScenarioPlaceholder

MARKET_IMPACT_SPECS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "large_order_square_root_impact_placeholder",
        "shock_type": "MARKET_IMPACT_SQUARE_ROOT",
        "description": "Büyük Lotlu Emirlerin Karekök Kuralı ile Fiyatı Kendi Aleyhine İtmesi yer tutucusu.",
        "magnitude_spec": "impact_proportional_to_sigma_times_sqrt_volume_ratio",
        "parameters": {"participation_rate": 0.15, "impact_constant_eta": 0.5},
    },
    {
        "placeholder_name": "predatory_hft_front_running_impact_placeholder",
        "shock_type": "ADVERSE_SELECTION",
        "description": "Yüksek Frekanslı Algoritmaların Emir Akışını Sezerek Fiyatı Önceden İtmesi yer tutucusu.",
        "magnitude_spec": "extra_adverse_selection_cost_2x",
        "parameters": {"adverse_selection_bps": 12},
    },
    {
        "placeholder_name": "liquidity_exhaustion_exponential_impact_placeholder",
        "shock_type": "EXPONENTIAL_IMPACT",
        "description": "Likidite Havuzu Boşaldığında Üstel Artan Piyasa Etkisi yer tutucusu.",
        "magnitude_spec": "exponential_penalty_when_volume_ratio_gt_0_20",
        "parameters": {"exhaustion_threshold": 0.20},
    },
]


def build_market_impact_shock_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of market impact shock placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in MARKET_IMPACT_SPECS:
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
        "total_market_impact_shocks": len(df),
        "all_execution_blocked": not bool(df["real_execution_allowed"].any()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
