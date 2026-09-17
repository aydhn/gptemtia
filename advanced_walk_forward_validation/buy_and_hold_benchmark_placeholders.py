# -*- coding: utf-8 -*-
"""Phase 147: Buy and Hold Benchmark Placeholders.

Placeholders representing passive buy-and-hold strategy contracts without trading recommendations.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_buy_and_hold_benchmark_placeholder_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for buy-and-hold benchmark placeholders."""
    rows = [
        {
            "placeholder_name": "buy_and_hold_single_asset_placeholder",
            "baseline_type": "BUY_AND_HOLD",
            "formula_spec": "R_bnh(t) = (P(t) - P(0)) / P(0) - TotalCost(entry, exit)",
            "description": "Varligin t0 aninda alinarak tn anina kadar tasindigi pasif referans yer tutucusu.",
            "execution_allowed": False,
            "trade_recommendation": False,
            "real_result_generated": False,
            "non_signal": True,
        },
        {
            "placeholder_name": "buy_and_hold_reinvested_placeholder",
            "baseline_type": "BUY_AND_HOLD_REINVESTED",
            "formula_spec": "R_bnh_div(t) = Product(1 + r_daily) - 1",
            "description": "Temettu veya tasima maliyetinin eklenip cikarildigi bilesik pasif getiri yer tutucusu.",
            "execution_allowed": False,
            "trade_recommendation": False,
            "real_result_generated": False,
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_buy_and_hold_placeholders": len(df),
        "zero_trade_recommendations": True,
        "zero_real_results": True,
        "non_signal": True,
    }
    return df, summary
