# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Scope Registry.

Defines operational scope, permitted boundaries, and prohibited actions for Phase 147.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

SCOPE_ITEMS: List[Dict[str, Any]] = [
    {
        "scope_name": "local_offline_split_contract_framework",
        "allowed": True,
        "description": "Zaman serisi bolumleme, rolling/expanding pencere sozlesmeleri tanimlanabilir.",
    },
    {
        "scope_name": "purge_embargo_policy_contracts",
        "allowed": True,
        "description": "Bilgi sizintisini ve overlap etkisini onleyen embargo ve purge sozlesmeleri tanimlanabilir.",
    },
    {
        "scope_name": "oos_benchmark_comparison_framework",
        "allowed": True,
        "description": "Benchmark evreni, Buy & Hold, nakit ve esit agirlikli referans sozlesmeleri olusturulabilir.",
    },
    {
        "scope_name": "validation_and_benchmark_metric_placeholders",
        "allowed": True,
        "description": "Metrik formulleri, hesaplama mantigi ve yer tutuculari tanimlanabilir.",
    },
    {
        "scope_name": "bias_and_no_lookahead_guards",
        "allowed": True,
        "description": "Data snooping, lookahead ve survivorship bias engelleyici muhafizlar calisabilir.",
    },
    {
        "scope_name": "live_order_execution",
        "allowed": False,
        "description": "Canli emir gonderimi kesinlikle yasaktir.",
    },
    {
        "scope_name": "broker_api_integration",
        "allowed": False,
        "description": "Broker API entegrasyonu kesinlikle yasaktir.",
    },
    {
        "scope_name": "actual_model_training_or_inference",
        "allowed": False,
        "description": "Gercek model egitimi (fit) veya cikarim (predict) kesinlikle yasaktir.",
    },
    {
        "scope_name": "optimizer_or_hyperparameter_search",
        "allowed": False,
        "description": "Optimizasyon veya hiperparametre arama kesinlikle yasaktir.",
    },
    {
        "scope_name": "actual_walk_forward_execution",
        "allowed": False,
        "description": "Gercek walk-forward backtest simülasyonu calistirilamaz.",
    },
    {
        "scope_name": "actual_benchmark_metric_calculation",
        "allowed": False,
        "description": "Gercek Sharpe, alpha, beta veya getiri hesaplanamaz.",
    },
    {
        "scope_name": "performance_or_return_guarantee",
        "allowed": False,
        "description": "Performans veya getiri garantisi iddiasinda bulunulamaz.",
    },
    {
        "scope_name": "live_trading_or_broker_approval",
        "allowed": False,
        "description": "Canli islem veya broker onay beyani verilemez.",
    },
]


def build_walk_forward_scope_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for walk-forward scope registry."""
    rows = []
    for s in SCOPE_ITEMS:
        rows.append(
            {
                "scope_name": s["scope_name"],
                "allowed": s["allowed"],
                "description": s["description"],
                "enforced": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_walk_forward_scope(df)
    return df, summary


def summarize_walk_forward_scope(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize walk-forward scope registry."""
    allowed_count = int(df["allowed"].sum()) if not df.empty else 0
    blocked_count = len(df) - allowed_count
    return {
        "total_scope_items": len(df),
        "allowed_count": allowed_count,
        "blocked_count": blocked_count,
        "all_enforced": True,
        "non_signal": True,
    }
