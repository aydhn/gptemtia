# -*- coding: utf-8 -*-
"""Phase 147: Equal Weight Benchmark Placeholders.

Placeholders representing equal-weight (1/N) multi-asset baselines without portfolio construction.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_equal_weight_benchmark_placeholder_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for equal-weight benchmark placeholders."""
    rows = [
        {
            "placeholder_name": "equal_weight_1_over_n_placeholder",
            "baseline_type": "EQUAL_WEIGHT",
            "formula_spec": "R_ew(t) = Sum(w_i * r_i(t)) where w_i = 1 / N",
            "description": "Portfoydeki tum varliklarin esit oranda agirliklandirildigi 1/N referans yer tutucusu.",
            "is_portfolio_construction": False,
            "execution_allowed": False,
            "non_signal": True,
        },
        {
            "placeholder_name": "equal_weight_rebalanced_monthly_placeholder",
            "baseline_type": "EQUAL_WEIGHT_REBALANCED",
            "formula_spec": "R_ew_reb(t) = NetOfCosts(Sum(w_i * r_i(t)), RebalanceCosts)",
            "description": "Aylik esit agirliga donus maliyeti dusulmus 1/N referans yer tutucusu.",
            "is_portfolio_construction": False,
            "execution_allowed": False,
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_equal_weight_placeholders": len(df),
        "zero_portfolio_construction": True,
        "zero_execution": True,
        "non_signal": True,
    }
    return df, summary
