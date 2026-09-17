# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Input Data Contracts Module.

Defines schemas and requirements for raw asset price series and trade blotter inputs.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    OUTPUT_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

INPUT_DATA_CONTRACTS: List[Dict[str, Any]] = [
    {
        "input_contract_name": "asset_ohlcv_time_series_contract",
        "required_fields": "timestamp, symbol, open, high, low, close, volume",
        "timestamp_alignment": "strictly_ascending_monotonic",
        "null_policy": "NO_FORWARD_FILL_PERMITTED_BEFORE_RESAMPLING",
        "description": "Historical price and volume series schema required for return extraction.",
    },
    {
        "input_contract_name": "trade_blotter_ledger_contract",
        "required_fields": "trade_id, timestamp_entry, timestamp_exit, symbol, side, entry_price, exit_price, pnl, return_pct",
        "timestamp_alignment": "strictly_exit_timestamp_ordered",
        "null_policy": "REJECT_INCOMPLETE_RECORDS",
        "description": "Executed trade records required for trade sequence reshuffling and permutation analysis.",
    },
]


def build_monte_carlo_input_data_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the Monte Carlo input data contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for c in INPUT_DATA_CONTRACTS:
        rows.append(
            {
                "input_contract_name": c["input_contract_name"],
                "required_fields": c["required_fields"],
                "timestamp_alignment": c["timestamp_alignment"],
                "null_policy": c["null_policy"],
                "description": c["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": OUTPUT_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": OUTPUT_CONTRACT_DOMAIN,
        "total_input_data_contracts": len(df),
        "all_valid": True,
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
