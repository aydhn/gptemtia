# -*- coding: utf-8 -*-
"""Phase 148: Gap Risk Scenario Placeholders.

Provides specifications and registry for weekend and overnight price discontinuity gap risk placeholders.
Model contract / formula metadata only; no actual price gap injection or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import ShockScenarioPlaceholder

GAP_RISK_SPECS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "weekend_opening_gap_placeholder",
        "shock_type": "PRICE_DISCONTINUITY",
        "description": "Hafta sonu haber akışından kaynaklanan Pazar akşamı açılış fiyat boşluğu yer tutucusu.",
        "magnitude_spec": "3x_standard_daily_atr",
        "parameters": {"gap_direction": "BIDIRECTIONAL", "bypass_stop_loss": True},
    },
    {
        "placeholder_name": "overnight_session_gap_placeholder",
        "shock_type": "OVERNIGHT_GAP",
        "description": "Seans kapanış ile ertesi gün açılışı arasındaki fiyat boşluğu yer tutucusu.",
        "magnitude_spec": "1.5x_standard_daily_atr",
        "parameters": {"gap_direction": "ADVERSE", "bypass_stop_loss": True},
    },
    {
        "placeholder_name": "macro_announcement_intraday_gap_placeholder",
        "shock_type": "INTRADAY_JUMP",
        "description": "Veri açıklanma anındaki ardışık çubuksuz dikey fiyat atlaması yer tutucusu.",
        "magnitude_spec": "2.0x_standard_daily_atr",
        "parameters": {"jump_latency_ms": 50, "liquidity_void": True},
    },
]


def build_gap_risk_scenario_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of gap risk scenario placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in GAP_RISK_SPECS:
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
        "total_gap_risk_placeholders": len(df),
        "all_execution_blocked": not bool(df["real_execution_allowed"].any()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
