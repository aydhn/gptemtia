# -*- coding: utf-8 -*-
"""Phase 148: Stress Signal Input Contracts.

Provides specifications and registry for hypothetical candidate strategy signals subjected to stress.
Contract and metadata definition only; non-signal invariant, zero live trading recommendations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

SIGNAL_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "signal_contract_id": "trend_following_candidate_signal_contract",
        "strategy_type": "MOMENTUM_TREND",
        "description": "Trend takip eden aday strateji sinyal yapısı sözleşmesi.",
        "zero_lookahead_verified": True,
        "is_investment_advice": False,
    },
    {
        "signal_contract_id": "mean_reversion_candidate_signal_contract",
        "strategy_type": "MEAN_REVERSION",
        "description": "Ortalamaya dönüş aday strateji sinyal yapısı sözleşmesi.",
        "zero_lookahead_verified": True,
        "is_investment_advice": False,
    },
    {
        "signal_contract_id": "breakout_candidate_signal_contract",
        "strategy_type": "VOLATILITY_BREAKOUT",
        "description": "Kanal kırılımı aday strateji sinyal yapısı sözleşmesi.",
        "zero_lookahead_verified": True,
        "is_investment_advice": False,
    },
]


def build_stress_signal_input_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stress signal input contracts."""
    rows: List[Dict[str, Any]] = []
    for s in SIGNAL_INPUT_CONTRACTS:
        rows.append(
            {
                "signal_contract_id": s["signal_contract_id"],
                "strategy_type": s["strategy_type"],
                "description": s["description"],
                "zero_lookahead_verified": s["zero_lookahead_verified"],
                "is_investment_advice": s["is_investment_advice"],
                "execution_allowed": False,
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_signal_input_contracts": len(df),
        "all_zero_lookahead_verified": bool(df["zero_lookahead_verified"].all()) if not df.empty else True,
        "zero_investment_advice": not bool(df["is_investment_advice"].any()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
