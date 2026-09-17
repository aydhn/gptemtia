# -*- coding: utf-8 -*-
"""Phase 147: Cost-Aware Benchmark Placeholders.

Placeholders representing benchmarks evaluated after subtracting transaction costs and slippage.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_cost_aware_benchmark_placeholder_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for cost-aware benchmark placeholders."""
    rows = [
        {
            "placeholder_name": "net_of_cost_buy_and_hold_placeholder",
            "baseline_type": "NET_BUY_HOLD",
            "cost_model_ref": "commission_fee_spread_model",
            "formula_spec": "R_net(t) = R_gross(t) - (Commission + Spread + Slippage)",
            "description": "Giris ve cikis islem maliyetleri ile kayma etkisi dusulmus pasif tutma referansi.",
            "execution_allowed": False,
            "real_costs_calculated": False,
            "non_signal": True,
        },
        {
            "placeholder_name": "turnover_penalized_benchmark_placeholder",
            "baseline_type": "TURNOVER_PENALIZED",
            "cost_model_ref": "proportional_turnover_cost_model",
            "formula_spec": "R_net(t) = R_gross(t) - Turnover(t) * AverageCostRate",
            "description": "Portfoy devir hizi yuksek olan stratejileri gercekci maliyetle cezalandiran referans sozlesme.",
            "execution_allowed": False,
            "real_costs_calculated": False,
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_cost_aware_placeholders": len(df),
        "zero_costs_calculated": True,
        "all_execution_disabled": True,
        "non_signal": True,
    }
    return df, summary
