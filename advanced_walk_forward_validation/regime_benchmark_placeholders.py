# -*- coding: utf-8 -*-
"""Phase 147: Regime Benchmark Placeholders.

Placeholders representing regime-conditioned baseline strategies.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_regime_benchmark_placeholder_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime benchmark placeholders."""
    rows = [
        {
            "placeholder_name": "regime_switching_cash_asset_placeholder",
            "baseline_type": "REGIME_SWITCHING_BASELINE",
            "formula_spec": "R_regime(t) = R_asset(t) if Regime(t) == CALM else R_cash(t)",
            "description": "Volatilite rejiminde nakde gecen, sakin donemde varlik tutan basit kural tabanli referans.",
            "execution_allowed": False,
            "non_signal": True,
        },
        {
            "placeholder_name": "trend_following_baseline_placeholder",
            "baseline_type": "TREND_HEURISTIC_BASELINE",
            "formula_spec": "R_trend(t) = Sign(MA(50) - MA(200)) * R_asset(t)",
            "description": "Hareketli ortalama kesisimine gore pozisyon alan standart teknik baseline yer tutucusu.",
            "execution_allowed": False,
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_regime_placeholders": len(df),
        "all_execution_disabled": True,
        "non_signal": True,
    }
    return df, summary
