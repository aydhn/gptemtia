# -*- coding: utf-8 -*-
"""Phase 146: Backtest Metric Placeholders.

Defines placeholder specifications for performance metrics (Sharpe, drawdown, turnover, cost-adjusted return).
Strictly does NOT calculate real metrics or assert performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

METRIC_PLACEHOLDERS: List[Dict[str, Any]] = [
    {"metric_name": "total_return_placeholder", "category": "RETURN", "description": "Toplam portfoy getirisi yer tutucusu.", "is_placeholder": True, "calculated": False},
    {"metric_name": "drawdown_placeholder", "category": "RISK", "description": "Maksimum tepe-dip kayip orani yer tutucusu.", "is_placeholder": True, "calculated": False},
    {"metric_name": "sharpe_placeholder", "category": "RISK_ADJUSTED", "description": "Risksiz faize gore duzeltilmis getiri orani yer tutucusu.", "is_placeholder": True, "calculated": False},
    {"metric_name": "sortino_placeholder", "category": "RISK_ADJUSTED", "description": "Asagi yonlu volatiliteye gore duzeltilmis getiri yer tutucusu.", "is_placeholder": True, "calculated": False},
    {"metric_name": "calmar_placeholder", "category": "RISK_ADJUSTED", "description": "Yillik getiri / Max Drawdown orani yer tutucusu.", "is_placeholder": True, "calculated": False},
    {"metric_name": "win_rate_placeholder", "category": "TRADE_STAT", "description": "Karli islem yuzdesi yer tutucusu.", "is_placeholder": True, "calculated": False},
    {"metric_name": "turnover_placeholder", "category": "ACTIVITY", "description": "Portfoy devir hizi yer tutucusu.", "is_placeholder": True, "calculated": False},
    {"metric_name": "exposure_placeholder", "category": "ACTIVITY", "description": "Piyasada kalma ve pozisyon aciklik orani yer tutucusu.", "is_placeholder": True, "calculated": False},
    {"metric_name": "cost_adjusted_return_placeholder", "category": "REALISM", "description": "Komisyon ve kayma sonrasi net getiri yer tutucusu.", "is_placeholder": True, "calculated": False},
    {"metric_name": "slippage_impact_placeholder", "category": "REALISM", "description": "Kaymanin brut getiri uzerindeki asindirici etkisi yer tutucusu.", "is_placeholder": True, "calculated": False},
]


def build_backtest_metric_placeholder_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of backtest metric placeholders."""
    rows = []
    for m in METRIC_PLACEHOLDERS:
        rows.append(
            {
                "metric_name": m["metric_name"],
                "category": m["category"],
                "description": m["description"],
                "is_placeholder": m["is_placeholder"],
                "calculated": m["calculated"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_metric_placeholders(df)
    return df, summary


def summarize_backtest_metric_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize backtest metric placeholders."""
    return {
        "total_metric_placeholders": len(df),
        "all_placeholders": bool(df["is_placeholder"].all()) if not df.empty else True,
        "all_zero_calculated": bool((~df["calculated"]).all()) if not df.empty else True,
        "performance_claim_strictly_prohibited": True,
        "non_signal": True,
    }
