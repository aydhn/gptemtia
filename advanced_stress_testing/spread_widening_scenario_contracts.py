# -*- coding: utf-8 -*-
"""Phase 148: Spread Widening Scenario Contracts.

Provides specifications and registry for bid-ask spread expansion and pricing disruption contracts.
Contract and metadata definition only; no actual transaction execution or cost calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

SPREAD_WIDENING_SHOCKS: List[Dict[str, Any]] = [
    {
        "shock_name": "spread_expansion_3x_contract",
        "spread_multiplier": 3.0,
        "description": "3x Spread Genişlemesi: Standart medyan spread'in 3 katına yükselmesi.",
        "applicable_assets": "ALL_FX_AND_COMMODITIES",
        "duration_minutes": 60,
        "execution_allowed": False,
    },
    {
        "shock_name": "spread_expansion_5x_contract",
        "spread_multiplier": 5.0,
        "description": "5x Şiddetli Spread Patlaması: Yüksek oynaklıkta likidite sağlayıcıların kotasyon aralığını açması.",
        "applicable_assets": "CROSS_RATES_AND_METALS",
        "duration_minutes": 120,
        "execution_allowed": False,
    },
    {
        "shock_name": "spread_expansion_10x_extreme_contract",
        "spread_multiplier": 10.0,
        "description": "10x Katastrofik Spread Şoku: Kriz anında tekil piyasa yapıcı kotasyonları.",
        "applicable_assets": "EXOTIC_FX_AND_ENERGY",
        "duration_minutes": 30,
        "execution_allowed": False,
    },
    {
        "shock_name": "off_hours_spread_blowout_contract",
        "spread_multiplier": 4.0,
        "description": "Seans Arası ve Hafta Sonu Spread Açılması: Cuma kapanış ve Pazar açılış spread patlaması.",
        "applicable_assets": "ALL_ASSETS",
        "duration_minutes": 240,
        "execution_allowed": False,
    },
    {
        "shock_name": "news_release_spread_spike_contract",
        "spread_multiplier": 6.0,
        "description": "Kritik Makro Veri Açıklanma Anı Spread Şoku (NFP, TÜFE, Faiz kararı anı 5 dakikalık spike).",
        "applicable_assets": "USD_PAIRS_AND_PRECIOUS_METALS",
        "duration_minutes": 15,
        "execution_allowed": False,
    },
]


def build_spread_widening_scenario_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of spread widening scenario contracts."""
    rows: List[Dict[str, Any]] = []
    for s in SPREAD_WIDENING_SHOCKS:
        rows.append(
            {
                "shock_name": s["shock_name"],
                "spread_multiplier": s["spread_multiplier"],
                "description": s["description"],
                "applicable_assets": s["applicable_assets"],
                "duration_minutes": s["duration_minutes"],
                "execution_allowed": s["execution_allowed"],
                "non_signal": True,
                "local_only": True,
                "manual_review_required": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_spread_shocks": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
