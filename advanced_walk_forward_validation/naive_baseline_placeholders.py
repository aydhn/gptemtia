# -*- coding: utf-8 -*-
"""Phase 147: Naive Baseline Placeholders.

Placeholders representing a naive zero-trade strategy baseline.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_naive_baseline_placeholder_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for naive baseline placeholders."""
    rows = [
        {
            "placeholder_name": "naive_zero_trade_baseline",
            "baseline_type": "NO_TRADE",
            "formula_spec": "R_t = 0.0, Cost_t = 0.0, Position_t = 0.0",
            "description": "Sifir islem, sifir risk ve sifir maliyet iceren temel benchmark tabani.",
            "execution_allowed": False,
            "real_result_generated": False,
            "non_signal": True,
        },
        {
            "placeholder_name": "naive_constant_weight_baseline",
            "baseline_type": "CONSTANT_WEIGHT",
            "formula_spec": "w_i = 1 / N, delta_w = 0",
            "description": "Hic rebalance yapilmayan sabit agirlikli baslangic tabani.",
            "execution_allowed": False,
            "real_result_generated": False,
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_naive_baselines": len(df),
        "all_execution_blocked": True,
        "zero_results_generated": True,
        "non_signal": True,
    }
    return df, summary
