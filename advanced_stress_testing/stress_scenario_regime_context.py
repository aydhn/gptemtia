# -*- coding: utf-8 -*-
"""Phase 148: Stress Scenario Regime Context.

Provides specifications and registry linking stress scenarios with market regime contexts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

REGIME_CONTEXTS: List[Dict[str, Any]] = [
    {
        "context_name": "regime_context_high_volatility_panic",
        "primary_regime": "HIGH_VOLATILITY",
        "market_condition": "PANIC_SELLING",
        "description": "Aşırı oynaklık ve panik satış rejim bağlamı.",
        "phase_135_ref": "regime_acceptance_high_vol_v1",
    },
    {
        "context_name": "regime_context_severe_trending_down",
        "primary_regime": "STRONG_DOWN_TREND",
        "market_condition": "BEAR_COLLAPSE",
        "description": "Güçlü aşağı yönlü çöküş trend rejim bağlamı.",
        "phase_135_ref": "regime_acceptance_trend_v1",
    },
    {
        "context_name": "regime_context_liquidity_vacuum",
        "primary_regime": "ILLIQUID_FROZEN",
        "market_condition": "ORDER_BOOK_COLLAPSE",
        "description": "Emir defteri boşalması ve derinlik çöküşü rejim bağlamı.",
        "phase_135_ref": "regime_acceptance_liquidity_v1",
    },
    {
        "context_name": "regime_context_macro_disruption",
        "primary_regime": "EVENT_SHOCK",
        "market_condition": "MACRO_SURPRISE",
        "description": "Merkez bankası ve makro olay şoku rejim bağlamı.",
        "phase_135_ref": "regime_acceptance_event_v1",
    },
]


def build_stress_scenario_regime_context_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry linking stress scenarios with regime contexts."""
    rows: List[Dict[str, Any]] = []
    for r in REGIME_CONTEXTS:
        rows.append(
            {
                "context_name": r["context_name"],
                "primary_regime": r["primary_regime"],
                "market_condition": r["market_condition"],
                "description": r["description"],
                "phase_135_ref": r["phase_135_ref"],
                "execution_allowed": False,
                "metric_calculation_allowed": False,
                "manual_review_required": True,
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_regime_contexts": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
