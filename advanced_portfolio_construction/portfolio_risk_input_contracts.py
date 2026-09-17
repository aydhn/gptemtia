# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Risk Input Contracts."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    RISK_INPUT_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


RISK_INPUT_SPECS = [
    {"risk_metric_type": "historical_volatility_input", "timeframe": "daily", "window_days": 60, "expected_dtype": "float64", "description": "Tarihsel volatilite girdi sozlesmesi (metadata only)."},
    {"risk_metric_type": "semi_variance_input", "timeframe": "daily", "window_days": 120, "expected_dtype": "float64", "description": "Asagi yonlu yari-varyans girdi sozlesmesi (metadata only)."},
    {"risk_metric_type": "correlation_matrix_input", "timeframe": "daily", "window_days": 120, "expected_dtype": "matrix_float64", "description": "Korelasyon matrisi girdi sozlesmesi (metadata only)."},
    {"risk_metric_type": "drawdown_depth_input", "timeframe": "daily", "window_days": 252, "expected_dtype": "float64", "description": "Cekilme derinligi girdi sozlesmesi (metadata only)."},
    {"risk_metric_type": "liquidity_spread_cost_input", "timeframe": "daily", "window_days": 30, "expected_dtype": "float64", "description": "Likidite spread maliyet girdi sozlesmesi (metadata only)."},
]


def build_portfolio_risk_input_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for risk input contracts."""
    rows = []
    for r in RISK_INPUT_SPECS:
        rows.append({
            "risk_metric_type": r["risk_metric_type"],
            "timeframe": r["timeframe"],
            "window_days": r["window_days"],
            "expected_dtype": r["expected_dtype"],
            "description": r["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "risk_metric_calculation_allowed": False,
            "real_risk_calculated": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": RISK_INPUT_DOMAIN,
        "active_profile": profile.profile_name,
        "total_risk_inputs": len(df),
        "all_contract_only": True,
        "all_zero_risk_calculation": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
