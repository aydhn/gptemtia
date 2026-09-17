# -*- coding: utf-8 -*-
"""Phase 147: Cash Benchmark Placeholders.

Placeholders representing risk-free cash/deposit benchmarks.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_cash_benchmark_placeholder_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for cash benchmark placeholders."""
    rows = [
        {
            "placeholder_name": "cash_sofr_overnight_placeholder",
            "baseline_type": "RISK_FREE_CASH",
            "rate_reference": "SOFR_OVERNIGHT",
            "formula_spec": "R_cash(t) = Product(1 + r_f(t) / 360) - 1",
            "description": "Gecelik risksiz faiz oranini referans alan nakit getiri yer tutucusu.",
            "execution_allowed": False,
            "non_signal": True,
        },
        {
            "placeholder_name": "zero_interest_cash_placeholder",
            "baseline_type": "ZERO_YIELD_CASH",
            "rate_reference": "FLAT_ZERO",
            "formula_spec": "R_cash(t) = 0.0",
            "description": "Nominal sifir faizli kasa nakit referansi.",
            "execution_allowed": False,
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_cash_placeholders": len(df),
        "all_execution_disabled": True,
        "non_signal": True,
    }
    return df, summary
