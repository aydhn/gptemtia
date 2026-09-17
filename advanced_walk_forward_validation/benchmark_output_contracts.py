# -*- coding: utf-8 -*-
"""Phase 147: Benchmark Output Contracts.

Defines schemas and permitted attributes for benchmark comparison outputs.
Strictly excludes realized alpha, beta, recommendations, and broker orders.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

BENCHMARK_OUTPUT_FIELDS: List[Dict[str, Any]] = [
    {
        "field_name": "benchmark_contract_status",
        "data_type": "STRING",
        "allowed": True,
        "description": "Benchmark sozlesme durumu (orn. benchmark_contract_ready).",
    },
    {
        "field_name": "benchmark_family",
        "data_type": "STRING",
        "allowed": True,
        "description": "Referans alinan benchmark turu (Buy & Hold, Cash, EW).",
    },
    {
        "field_name": "manual_review_required",
        "data_type": "BOOLEAN",
        "allowed": True,
        "description": "Insan incelemesi zorunlulugu bayragi.",
    },
    {
        "field_name": "actual_alpha_value",
        "data_type": "FLOAT",
        "allowed": False,
        "description": "Gerceklesmis alfa degeri (Faz 147'de kesinlikle yasaktir).",
    },
    {
        "field_name": "performance_outperformance_claim",
        "data_type": "STRING",
        "allowed": False,
        "description": "Benchmark ustunde basari iddiasi (Faz 147'de kesinlikle yasaktir).",
    },
]


def build_benchmark_output_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for benchmark output contracts."""
    rows = []
    for f in BENCHMARK_OUTPUT_FIELDS:
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
        "allowed_count": allowed_count,
        "blocked_count": len(df) - allowed_count,
        "zero_alpha_claims": True,
        "non_signal": True,
    }
    return df, summary
