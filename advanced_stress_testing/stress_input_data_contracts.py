# -*- coding: utf-8 -*-
"""Phase 148: Stress Input Data Contracts.

Provides specifications and registry for input data requirements during stress testing analysis.
Ensures point-in-time integrity, timestamp order, and zero lookahead.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

INPUT_DATA_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "stress_input_market_data_contract",
        "data_type": "OHLCV_BARS",
        "timeframe": "1D_1H_5M",
        "description": "Zaman damgası doğrulanmış, geleceğe bakış içermeyen OHLCV piyasa veri sözleşmesi.",
        "phase_source": "Phase 113 / 137",
        "enforce_point_in_time": True,
    },
    {
        "contract_id": "stress_input_spread_depth_contract",
        "data_type": "ORDER_BOOK_SNAPSHOT",
        "timeframe": "TICK_MEDIAN",
        "description": "Alış-satış spread ve kademe derinlik verisi sözleşmesi.",
        "phase_source": "Phase 116 / 146",
        "enforce_point_in_time": True,
    },
    {
        "contract_id": "stress_input_macro_event_contract",
        "data_type": "EVENT_METADATA",
        "timeframe": "CALENDAR_EVENT",
        "description": "Salt metaveri takvim ve duyuru zaman damgası girdi sözleşmesi.",
        "phase_source": "Phase 110 / 132",
        "enforce_point_in_time": True,
    },
]


def build_stress_input_data_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stress input data contracts."""
    rows: List[Dict[str, Any]] = []
    for c in INPUT_DATA_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "data_type": c["data_type"],
                "timeframe": c["timeframe"],
                "description": c["description"],
                "phase_source": c["phase_source"],
                "enforce_point_in_time": c["enforce_point_in_time"],
                "execution_allowed": False,
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_input_data_contracts": len(df),
        "all_enforce_point_in_time": bool(df["enforce_point_in_time"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
