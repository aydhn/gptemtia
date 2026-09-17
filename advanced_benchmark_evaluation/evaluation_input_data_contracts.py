# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Input Data Contracts Module.

Defines input data contracts for offline evaluation and benchmark comparisons.
Requires strict monotonic UTC timestamps and source data preservation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DEPENDENCY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

INPUT_DATA_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "INP_DATA_OHLCV_STANDARDS",
        "input_type": "market_ohlcv",
        "requirements": "Monotonic UTC timestamp, non-negative volume, high >= low, open/close inside range",
        "description": "Temel fiyat ve bar verisi bütünlük sözleşmesi.",
    },
    {
        "contract_id": "INP_DATA_NO_LOOKAHEAD",
        "input_type": "temporal_alignment",
        "requirements": "Strict backward asof join, no negative shift, no future release leakage",
        "description": "Geleceğe bakış sızıntısını engelleyen veri hizalama sözleşmesi.",
    },
    {
        "contract_id": "INP_DATA_SOURCE_PRESERVATION",
        "input_type": "source_integrity",
        "requirements": "Raw source files immutable, non-destructive cleaning only, audit logged",
        "description": "Ham kaynak verilerin dokunulmazlığı ve değişmezliği sözleşmesi.",
    },
]


def build_evaluation_input_data_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of evaluation input data contracts."""
    rows: List[Dict[str, Any]] = []

    for c in INPUT_DATA_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "input_type": c["input_type"],
                "requirements": c["requirements"],
                "description": c["description"],
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DEPENDENCY_DOMAIN,
        "total_contracts": len(df),
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
