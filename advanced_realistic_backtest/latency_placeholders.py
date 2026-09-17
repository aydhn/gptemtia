# -*- coding: utf-8 -*-
"""Phase 146: Latency Placeholders.

Defines specifications and delay placeholders for realistic execution latency.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

LATENCY_MODELS: List[Dict[str, Any]] = [
    {
        "latency_model_name": "network_roundtrip_latency_placeholder",
        "description": "Istemci ile sunucu arasindaki ag gecikmesi (orn: 20-50 ms arasi simule gecikme).",
        "nominal_delay_ms": 30.0,
        "is_placeholder": True,
        "execution_allowed": False,
    },
    {
        "latency_model_name": "exchange_matching_engine_latency_placeholder",
        "description": "Borsa eslestirme motoru sira gecikmesi (orn: 5-15 ms).",
        "nominal_delay_ms": 10.0,
        "is_placeholder": True,
        "execution_allowed": False,
    },
    {
        "latency_model_name": "bar_interval_lag_placeholder",
        "description": "Bar seviyesinde calisan sistemler icin en az 1 bar gecikme (1-bar lag).",
        "nominal_delay_ms": 60000.0,
        "is_placeholder": True,
        "execution_allowed": False,
    },
]


def build_latency_placeholder_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of latency model placeholders."""
    rows = []
    for l in LATENCY_MODELS:
        rows.append(
            {
                "latency_model_name": l["latency_model_name"],
                "description": l["description"],
                "nominal_delay_ms": l["nominal_delay_ms"],
                "is_placeholder": l["is_placeholder"],
                "execution_allowed": l["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_latency_placeholders(df)
    return df, summary


def summarize_latency_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize latency placeholders."""
    return {
        "total_latency_models": len(df),
        "zero_latency_assumption_forbidden": True,
        "all_placeholders": bool(df["is_placeholder"].all()) if not df.empty else True,
        "non_signal": True,
    }
