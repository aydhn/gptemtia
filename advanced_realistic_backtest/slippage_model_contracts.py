# -*- coding: utf-8 -*-
"""Phase 146: Slippage Model Contracts.

Defines specifications for slippage modeling (fixed bps, spread-based,
volatility-based, liquidity-based, participation rate, regime-aware).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

SLIPPAGE_MODELS: List[Dict[str, Any]] = [
    {
        "slippage_model_name": "fixed_bps_slippage_contract",
        "slippage_type": "FIXED_BPS",
        "description": "Her islem icin sabit baz puan (orn: 3 bps) fiyattan olumsuz kayma sozlesmesi.",
        "formula": "price * (fixed_bps / 10000.0)",
        "default_parameter": {"bps": 3.0},
        "real_slippage_calculated": False,
        "performance_guaranteed": False,
    },
    {
        "slippage_model_name": "spread_based_slippage_contract",
        "slippage_type": "SPREAD_BASED",
        "description": "Alis-satis makasinin bir carpani olarak hesaplanan kayma modeli.",
        "formula": "spread * spread_multiplier",
        "default_parameter": {"spread_multiplier": 0.5},
        "real_slippage_calculated": False,
        "performance_guaranteed": False,
    },
    {
        "slippage_model_name": "volatility_based_slippage_contract",
        "slippage_type": "VOLATILITY_BASED",
        "description": "ATR veya gerceklesen volatiliteye bagli dinamik kayma sozlesmesi.",
        "formula": "volatility_factor * ATR_14",
        "default_parameter": {"volatility_factor": 0.1},
        "real_slippage_calculated": False,
        "performance_guaranteed": False,
    },
    {
        "slippage_model_name": "liquidity_based_slippage_contract",
        "slippage_type": "LIQUIDITY_BASED",
        "description": "Emir hacminin ortalama gunluk hacme oranina gore artan kayma modeli.",
        "formula": "base_slippage * (order_size / (ADV_20 * max_participation)) ** alpha",
        "default_parameter": {"alpha": 0.5, "max_participation": 0.1},
        "real_slippage_calculated": False,
        "performance_guaranteed": False,
    },
    {
        "slippage_model_name": "participation_rate_slippage_contract",
        "slippage_type": "PARTICIPATION_RATE",
        "description": "Piyasa katilim oranina dayali piyasa etki ve kayma modeli.",
        "formula": "gamma * participation_rate ** 0.5",
        "default_parameter": {"gamma": 0.05},
        "real_slippage_calculated": False,
        "performance_guaranteed": False,
    },
    {
        "slippage_model_name": "regime_aware_slippage_contract",
        "slippage_type": "REGIME_AWARE",
        "description": "Phase 126-135 rejim durumuna (Stres, Kirilganlik, Trend, Sıkışma) gore olceklenen kayma.",
        "formula": "base_slippage * regime_slippage_multiplier",
        "default_parameter": {"stress_multiplier": 2.5, "calm_multiplier": 1.0},
        "real_slippage_calculated": False,
        "performance_guaranteed": False,
    },
]


def build_slippage_model_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of slippage model contracts."""
    rows = []
    for s in SLIPPAGE_MODELS:
        rows.append(
            {
                "slippage_model_name": s["slippage_model_name"],
                "slippage_type": s["slippage_type"],
                "description": s["description"],
                "formula": s["formula"],
                "default_parameter": str(s["default_parameter"]),
                "real_slippage_calculated": s["real_slippage_calculated"],
                "performance_guaranteed": s["performance_guaranteed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_slippage_model_contracts(df)
    return df, summary


def validate_slippage_model_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that slippage model does not claim live guarantees or real calculations."""
    issues = []
    if contract.get("real_slippage_calculated", False):
        issues.append("real_slippage_calculated must be False in Phase 146")
    if contract.get("performance_guaranteed", False):
        issues.append("performance_guaranteed must be False")
    return {
        "slippage_model_name": contract.get("slippage_model_name", "UNKNOWN"),
        "is_valid": len(issues) == 0,
        "issues": issues,
    }


def summarize_slippage_model_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize slippage model contract registry."""
    return {
        "total_slippage_models": len(df),
        "all_zero_guarantee": bool((~df["performance_guaranteed"]).all()) if not df.empty else True,
        "all_real_calculation_blocked": bool((~df["real_slippage_calculated"]).all()) if not df.empty else True,
        "slippage_types": df["slippage_type"].tolist() if not df.empty else [],
        "non_signal": True,
    }
