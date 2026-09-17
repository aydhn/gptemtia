# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Signal Input Contracts."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    SIGNAL_INPUT_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


SIGNAL_INPUT_SPECS = [
    {"signal_type": "trend_following_score", "source_phase": "Phase 116-125 Feature Engine", "expected_dtype": "float64", "range_min": -1.0, "range_max": 1.0, "description": "Trend gucu girdi sozlesmesi (metadata only)."},
    {"signal_type": "mean_reversion_score", "source_phase": "Phase 117 Technical Indicators", "expected_dtype": "float64", "range_min": -1.0, "range_max": 1.0, "description": "Ortalamaya donus girdi sozlesmesi (metadata only)."},
    {"signal_type": "momentum_score", "source_phase": "Phase 118 Feature Grid", "expected_dtype": "float64", "range_min": -1.0, "range_max": 1.0, "description": "Momentum girdi sozlesmesi (metadata only)."},
    {"signal_type": "macro_event_sentiment_score", "source_phase": "Phase 120 Feature Fusion", "expected_dtype": "float64", "range_min": -1.0, "range_max": 1.0, "description": "Makro/haber metadata girdi sozlesmesi (metadata only)."},
    {"signal_type": "regime_state_indicator", "source_phase": "Phase 127 Regime Matrix", "expected_dtype": "int64", "range_min": 0, "range_max": 10, "description": "Piyasa rejimi girdi sozlesmesi (metadata only)."},
]


def build_portfolio_signal_input_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for signal input contracts."""
    rows = []
    for s in SIGNAL_INPUT_SPECS:
        rows.append({
            "signal_type": s["signal_type"],
            "source_phase": s["source_phase"],
            "expected_dtype": s["expected_dtype"],
            "range_min": s["range_min"],
            "range_max": s["range_max"],
            "description": s["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "signal_generation_allowed": False,
            "directional_claim_allowed": False,
            "real_signal_produced": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": SIGNAL_INPUT_DOMAIN,
        "active_profile": profile.profile_name,
        "total_signal_inputs": len(df),
        "all_contract_only": True,
        "all_zero_signal_generation": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
