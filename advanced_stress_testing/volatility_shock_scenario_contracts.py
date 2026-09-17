# -*- coding: utf-8 -*-
"""Phase 148: Volatility Shock Scenario Contracts.

Provides specifications and registry for volatility expansion and volatility regime shocks.
Contract and metadata definition only; no actual volatility shock application or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

VOLATILITY_SHOCKS: List[Dict[str, Any]] = [
    {
        "shock_name": "volatility_spike_2x_contract",
        "multiplier": 2.0,
        "description": "2x Volatilite Genişlemesi: Standart ATR ve gerçekleşen volatilitenin 2 katına çıkması.",
        "duration_bars": 10,
        "decay_mode": "EXPONENTIAL",
        "execution_allowed": False,
    },
    {
        "shock_name": "volatility_spike_3x_contract",
        "multiplier": 3.0,
        "description": "3x Şiddetli Volatilite Şoku: Önemli makro veri sürprizi veya kriz başlangıcı.",
        "duration_bars": 20,
        "decay_mode": "LINEAR",
        "execution_allowed": False,
    },
    {
        "shock_name": "volatility_spike_5x_tail_contract",
        "multiplier": 5.0,
        "description": "5x Kuyruk Riski Volatilite Patlaması: Black Swan tipi ani likidite buharlaşması ve fiyat salınımı.",
        "duration_bars": 5,
        "decay_mode": "STEP_FUNCTION",
        "execution_allowed": False,
    },
    {
        "shock_name": "volatility_smile_flattening_contract",
        "multiplier": 2.5,
        "description": "Volatilite Eğrisi Düzleşmesi: Derin OTM opsiyon ve kuyruk risk fiyatlamasının aşırı yükselmesi.",
        "duration_bars": 15,
        "decay_mode": "LOGARITHMIC",
        "execution_allowed": False,
    },
    {
        "shock_name": "intraday_gap_volatility_contract",
        "multiplier": 4.0,
        "description": "Gün İçi Fiyat Boşluğu Volatilitesi: Dakikalık çubuklarda normal range'in 4 katı sıçramalar.",
        "duration_bars": 8,
        "decay_mode": "EXPONENTIAL",
        "execution_allowed": False,
    },
]


def build_volatility_shock_scenario_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of volatility shock scenario contracts."""
    rows: List[Dict[str, Any]] = []
    for s in VOLATILITY_SHOCKS:
        rows.append(
            {
                "shock_name": s["shock_name"],
                "multiplier": s["multiplier"],
                "description": s["description"],
                "duration_bars": s["duration_bars"],
                "decay_mode": s["decay_mode"],
                "execution_allowed": s["execution_allowed"],
                "non_signal": True,
                "local_only": True,
                "manual_review_required": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_volatility_shocks": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
