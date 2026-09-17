# -*- coding: utf-8 -*-
"""Phase 148: Transaction Cost Shock Contracts.

Provides specifications and registry for stressed broker commissions and fee surge contracts.
Contract and metadata definition only; no actual fee calculation or PnL deduction.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

TRANSACTION_COST_SHOCKS: List[Dict[str, Any]] = [
    {
        "contract_name": "commission_rate_surge_3x_contract",
        "multiplier": 3.0,
        "description": "3x Aracı Kurum Komisyon Artışı: Kriz ve yüksek volatilite dönemlerinde artan işlem komisyonları.",
        "cost_model_ref": "cost_model_v1",
        "execution_allowed": False,
        "cost_calculation_allowed": False,
    },
    {
        "contract_name": "exchange_fee_regulatory_shock_contract",
        "multiplier": 2.5,
        "description": "Borsa ve Düzenleyici Kurum Harç Şoku: Finansal işlem vergisi ve borsa takas ücreti artışı.",
        "cost_model_ref": "cost_model_v1",
        "execution_allowed": False,
        "cost_calculation_allowed": False,
    },
    {
        "contract_name": "stressed_financing_fee_contract",
        "multiplier": 4.0,
        "description": "Stresli Kaldıraç / Finansman Maliyeti: Teminat tamamlama dönemlerinde yükselen gecelik borçlanma faizi.",
        "cost_model_ref": "cost_model_v1",
        "execution_allowed": False,
        "cost_calculation_allowed": False,
    },
]


def build_transaction_cost_shock_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of transaction cost shock contracts."""
    rows: List[Dict[str, Any]] = []
    for c in TRANSACTION_COST_SHOCKS:
        rows.append(
            {
                "contract_name": c["contract_name"],
                "multiplier": c["multiplier"],
                "description": c["description"],
                "cost_model_ref": c["cost_model_ref"],
                "execution_allowed": c["execution_allowed"],
                "cost_calculation_allowed": c["cost_calculation_allowed"],
                "non_signal": True,
                "local_only": True,
                "manual_review_required": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_transaction_cost_shocks": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_cost_calculation_blocked": not bool(df["cost_calculation_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
