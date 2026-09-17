# -*- coding: utf-8 -*-
"""Phase 148: Execution Disruption Scenario Placeholders.

Provides specifications and registry for broker/exchange outages, order rejections, and latency shocks.
Model contract / formula metadata only; no live trading or execution interaction.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import ShockScenarioPlaceholder

EXECUTION_DISRUPTION_SPECS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "exchange_connectivity_loss_placeholder",
        "shock_type": "INFRASTRUCTURE_OUTAGE",
        "description": "Borsa / Likidite Havuzu Bağlantı Kopması: 15 dakika boyunca emir iletememe simülasyonu.",
        "magnitude_spec": "15_minutes_complete_blackout",
        "parameters": {"unfillable_orders": True, "forced_queueing": True},
    },
    {
        "placeholder_name": "order_rejection_surge_placeholder",
        "shock_type": "ORDER_REJECTION",
        "description": "Yüksek Oynaklıkta Anlık Emir Reddi (%40 Red Oranı) yer tutucusu.",
        "magnitude_spec": "40pct_order_rejection_ratio",
        "parameters": {"rejection_reason": "OFF_MARKET_PRICE_OR_NO_LIQUIDITY"},
    },
    {
        "placeholder_name": "latency_spike_500ms_placeholder",
        "shock_type": "LATENCY_SPIKE",
        "description": "Ağ Tıkanıklığı ve Emir İletim Gecikmesi (500 ms Latency Şoku) yer tutucusu.",
        "magnitude_spec": "500ms_execution_delay",
        "parameters": {"adverse_price_movement_probability": 0.75},
    },
]


def build_execution_disruption_scenario_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of execution disruption scenario placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in EXECUTION_DISRUPTION_SPECS:
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
        "total_disruption_placeholders": len(df),
        "all_execution_blocked": not bool(df["real_execution_allowed"].any()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
