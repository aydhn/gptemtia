# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Output Contracts.

Defines schemas and permitted attributes for walk-forward validation outputs.
Strictly excludes realized returns, signals, and live execution triggers.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

OUTPUT_CONTRACT_FIELDS: List[Dict[str, Any]] = [
    {
        "field_name": "contract_validation_status",
        "data_type": "STRING",
        "allowed": True,
        "description": "Dogrulama sozlesmesinin gecerlilik durumu (orn. validation_contract_ready).",
    },
    {
        "field_name": "blocked_reason",
        "data_type": "STRING",
        "allowed": True,
        "description": "Calismanin neden engellendigini belirten guvenlik gerekcesi.",
    },
    {
        "field_name": "manual_review_required",
        "data_type": "BOOLEAN",
        "allowed": True,
        "description": "Insan operator incelemesinin zorunlu oldugunu belirten bayrak.",
    },
    {
        "field_name": "oos_contract_ready",
        "data_type": "BOOLEAN",
        "allowed": True,
        "description": "OOS sozlesmelerinin tanimlanmis ve hazir oldugunu gosteren bayrak.",
    },
    {
        "field_name": "benchmark_contract_ready",
        "data_type": "BOOLEAN",
        "allowed": True,
        "description": "Benchmark karsilastirma sozlesmelerinin hazir oldugunu gosteren bayrak.",
    },
    {
        "field_name": "realized_oos_return",
        "data_type": "FLOAT",
        "allowed": False,
        "description": "Gerceklesmis OOS getiri degeri (Faz 147'de kesinlikle yasaktir).",
    },
    {
        "field_name": "trading_signal",
        "data_type": "STRING",
        "allowed": False,
        "description": "AL/SAT sinyali (Faz 147'de kesinlikle yasaktir).",
    },
    {
        "field_name": "trade_recommendation",
        "data_type": "STRING",
        "allowed": False,
        "description": "Pozisyon tavsiyesi (Faz 147'de kesinlikle yasaktir).",
    },
]


def build_walk_forward_output_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for walk-forward output contracts."""
    rows = []
    for f in OUTPUT_CONTRACT_FIELDS:
        rows.append(
            {
                "field_name": f["field_name"],
                "data_type": f["data_type"],
                "allowed": f["allowed"],
                "description": f["description"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    allowed_count = int(df["allowed"].sum()) if not df.empty else 0
    summary = {
        "total_fields": len(df),
        "allowed_fields_count": allowed_count,
        "blocked_fields_count": len(df) - allowed_count,
        "zero_signals": True,
        "zero_realized_returns": True,
        "non_signal": True,
    }
    return df, summary
