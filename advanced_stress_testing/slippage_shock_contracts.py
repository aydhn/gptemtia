# -*- coding: utf-8 -*-
"""Phase 148: Slippage Shock Contracts.

Provides specifications and registry for catastrophic slippage and order execution drift contracts.
Contract and metadata definition only; no actual slippage execution or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

SLIPPAGE_SHOCKS: List[Dict[str, Any]] = [
    {
        "contract_name": "catastrophic_slippage_5x_contract",
        "slippage_multiplier": 5.0,
        "description": "5x Katastrofik Kayma (Slippage): Aşırı oynaklıkta piyasa emrinin beklenen fiyattan 5 kat daha kötü gerçekleşmesi.",
        "slippage_model_ref": "slippage_model_v1",
        "execution_allowed": False,
        "slippage_calculation_allowed": False,
    },
    {
        "contract_name": "stop_loss_slippage_blowout_contract",
        "slippage_multiplier": 8.0,
        "description": "Zarar Kes (Stop-Loss) Kayma Patlaması: Fiyat boşluğunda stop seviyesinin çok altında doldurulması.",
        "slippage_model_ref": "slippage_model_v1",
        "execution_allowed": False,
        "slippage_calculation_allowed": False,
    },
    {
        "contract_name": "illiquid_market_order_slippage_contract",
        "slippage_multiplier": 4.0,
        "description": "Sığ Piyasa Koşullarında Piyasa Emri Kayması: Çoklu kademe süpürme (order book walk) maliyeti.",
        "slippage_model_ref": "slippage_model_v1",
        "execution_allowed": False,
        "slippage_calculation_allowed": False,
    },
]


def build_slippage_shock_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of slippage shock contracts."""
    rows: List[Dict[str, Any]] = []
    for s in SLIPPAGE_SHOCKS:
        rows.append(
            {
                "contract_name": s["contract_name"],
                "slippage_multiplier": s["slippage_multiplier"],
                "description": s["description"],
                "slippage_model_ref": s["slippage_model_ref"],
                "execution_allowed": s["execution_allowed"],
                "slippage_calculation_allowed": s["slippage_calculation_allowed"],
                "non_signal": True,
                "local_only": True,
                "manual_review_required": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_slippage_shocks": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_slippage_calculation_blocked": not bool(df["slippage_calculation_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
