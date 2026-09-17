# -*- coding: utf-8 -*-
"""Phase 146: Backtest Feature Input Contracts.

Defines point-in-time feature ingestion contracts from FeatureStore without future leakage.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

FEATURE_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "featurestore_point_in_time_contract",
        "description": "FeatureStore'dan cekilen faktor ve ozniteliklerin zaman damgasi eslestirme sozlesmesi.",
        "join_type": "ASOF_BACKWARD_ONLY",
        "tolerance": "0ms",
        "allow_forward_look": False,
    },
    {
        "contract_name": "regime_state_input_contract",
        "description": "Phase 126-135 rejim etiketlerinin sadece geriye donuk olarak backtest motoruna sunulmasi sozlesmesi.",
        "join_type": "ASOF_BACKWARD_ONLY",
        "tolerance": "0ms",
        "allow_forward_look": False,
    },
]


def build_backtest_feature_input_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of feature input contracts."""
    rows = []
    for f in FEATURE_INPUT_CONTRACTS:
        rows.append(
            {
                "contract_name": f["contract_name"],
                "description": f["description"],
                "join_type": f["join_type"],
                "tolerance": f["tolerance"],
                "allow_forward_look": f["allow_forward_look"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_feature_input_contracts(df)
    return df, summary


def summarize_backtest_feature_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize feature input contracts."""
    return {
        "total_feature_contracts": len(df),
        "zero_forward_look": bool((~df["allow_forward_look"]).all()) if not df.empty else True,
        "asof_backward_only": True,
        "non_signal": True,
    }
