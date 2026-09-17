# -*- coding: utf-8 -*-
"""Phase 147: Benchmark Universe Contracts.

Defines eligible instrument universes for benchmark baselines.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

UNIVERSE_SPECS: List[Dict[str, Any]] = [
    {
        "universe_id": "UNI-01",
        "universe_name": "precious_metals_universe",
        "instruments": ["XAU/USD", "XAG/USD", "XPT/USD", "XPD/USD"],
        "asset_class": "COMMODITIES",
        "description": "Altin, gumus, platin ve paladyumdan olusan degerli metaller evreni.",
    },
    {
        "universe_id": "UNI-02",
        "universe_name": "energy_commodities_universe",
        "instruments": ["BRENT", "WTI", "NATGAS"],
        "asset_class": "COMMODITIES",
        "description": "Ham petrol ve dogal gazdan olusan enerji emtialari evreni.",
    },
    {
        "universe_id": "UNI-03",
        "universe_name": "major_forex_universe",
        "instruments": ["EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF"],
        "asset_class": "FOREX",
        "description": "Majör doviz ciftlerinden olusan benchmark evreni.",
    },
]


def build_benchmark_universe_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for benchmark universe registry."""
    rows = []
    for u in UNIVERSE_SPECS:
        rows.append(
            {
                "universe_id": u["universe_id"],
                "universe_name": u["universe_name"],
                "instruments": ",".join(u["instruments"]),
                "instrument_count": len(u["instruments"]),
                "asset_class": u["asset_class"],
                "description": u["description"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_universes": len(df),
        "total_instruments_mapped": int(df["instrument_count"].sum()) if not df.empty else 0,
        "non_signal": True,
    }
    return df, summary
