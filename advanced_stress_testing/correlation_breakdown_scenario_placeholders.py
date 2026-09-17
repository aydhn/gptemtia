# -*- coding: utf-8 -*-
"""Phase 148: Correlation Breakdown Scenario Placeholders.

Provides specifications and registry for correlation regime shift and dependency breakdown placeholders.
Model contract / formula metadata only; no actual statistical breakdown calculation or PnL impact.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import ShockScenarioPlaceholder

CORRELATION_BREAKDOWN_SPECS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "gold_usd_correlation_inversion_placeholder",
        "shock_type": "CORRELATION_INVERSION",
        "description": "Altın ve Dolar Endeksi arasındaki negatif korelasyonun pozitif yöne kırılması yer tutucusu.",
        "magnitude_spec": "delta_correlation_from_neg_0_7_to_pos_0_8",
        "parameters": {"asset_pair": "GOLD_USD", "inversion_speed": "RAPID"},
    },
    {
        "placeholder_name": "cross_commodity_correlation_one_placeholder",
        "shock_type": "CORRELATION_CONVERGENCE",
        "description": "Kriz anında tüm emtia sepetinin birbiriyle korelasyonunun +1'e yakınsaması yer tutucusu.",
        "magnitude_spec": "portfolio_correlation_to_0_95",
        "parameters": {"assets": ["BRENT", "WTI", "COPPER", "SILVER"], "diversification_loss": True},
    },
    {
        "placeholder_name": "fx_carry_trade_unwind_correlation_placeholder",
        "shock_type": "CARRY_UNWIND",
        "description": "Carry trade çözülmesinde fonlama para birimleri ile riskli varlıklar arası korelasyon patlaması.",
        "magnitude_spec": "correlation_jump_plus_0_8",
        "parameters": {"funding_pairs": ["USDJPY", "EURUSD"], "unwind_velocity": "EXTREME"},
    },
]


def build_correlation_breakdown_scenario_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of correlation breakdown scenario placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in CORRELATION_BREAKDOWN_SPECS:
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
        "total_correlation_breakdown_placeholders": len(df),
        "all_execution_blocked": not bool(df["real_execution_allowed"].any()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
