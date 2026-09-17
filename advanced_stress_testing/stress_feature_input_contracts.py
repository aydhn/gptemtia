# -*- coding: utf-8 -*-
"""Phase 148: Stress Feature Input Contracts.

Provides specifications and registry for feature input contracts used in stress scenario modeling.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

FEATURE_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "feature_set_id": "volatility_features_stress_contract",
        "description": "ATR, Bollinger genişliği, Parkinson ve gerçekleşen oynaklık öznitelik sözleşmesi.",
        "phase_source": "Phase 118",
        "no_lookahead_verified": True,
    },
    {
        "feature_set_id": "trend_momentum_features_stress_contract",
        "description": "Hareketli ortalama eğimleri, MACD ve RSI öznitelik sözleşmesi.",
        "phase_source": "Phase 119",
        "no_lookahead_verified": True,
    },
    {
        "feature_set_id": "liquidity_spread_features_stress_contract",
        "description": "Tekil spread, Amihud illikidite oranı ve işlem hacim oranları sözleşmesi.",
        "phase_source": "Phase 116 / 129",
        "no_lookahead_verified": True,
    },
]


def build_stress_feature_input_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stress feature input contracts."""
    rows: List[Dict[str, Any]] = []
    for f in FEATURE_INPUT_CONTRACTS:
        rows.append(
            {
                "feature_set_id": f["feature_set_id"],
                "description": f["description"],
                "phase_source": f["phase_source"],
                "no_lookahead_verified": f["no_lookahead_verified"],
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_feature_input_contracts": len(df),
        "all_no_lookahead_verified": bool(df["no_lookahead_verified"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
