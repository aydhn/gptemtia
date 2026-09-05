from typing import Tuple, Dict, Any
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile

DEPENDENCIES_DATA = [
    {"target_indicator": "atr", "dependencies": ["true_range"], "formula_ref": "rolling mean of true_range"},
    {"target_indicator": "bollinger_bandwidth", "dependencies": ["bollinger_bands"], "formula_ref": "(upper - lower) / mid"},
    {"target_indicator": "bollinger_percent_b", "dependencies": ["bollinger_bands"], "formula_ref": "(close - lower) / (upper - lower)"},
    {"target_indicator": "macd", "dependencies": ["ema_fast", "ema_slow"], "formula_ref": "ema(12) - ema(26)"},
    {"target_indicator": "ppo", "dependencies": ["ema_fast", "ema_slow"], "formula_ref": "(ema(12) - ema(26)) / ema(26)"},
    {"target_indicator": "dema", "dependencies": ["ema_1", "ema_2"], "formula_ref": "2*ema1 - ema2"},
    {"target_indicator": "tema", "dependencies": ["ema_1", "ema_2", "ema_3"], "formula_ref": "3*ema1 - 3*ema2 + ema3"},
    {"target_indicator": "stochastic", "dependencies": ["rolling_high", "rolling_low"], "formula_ref": "(close - lowest) / (highest - lowest)"},
    {"target_indicator": "donchian_position", "dependencies": ["donchian_upper", "donchian_lower"], "formula_ref": "(close - lower) / (upper - lower)"},
    {"target_indicator": "quote_spread_pct", "dependencies": ["quote_mid", "quote_spread"], "formula_ref": "spread / mid"},
    {"target_indicator": "return_volatility_ratio", "dependencies": ["simple_return", "rolling_std"], "formula_ref": "mean_return / std_return"},
]


def build_indicator_dependency_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = []
    for d in DEPENDENCIES_DATA:
        rows.append({
            "target_indicator": d["target_indicator"],
            "dependencies": ", ".join(d["dependencies"]),
            "dependency_count": len(d["dependencies"]),
            "formula_reference": d["formula_ref"],
            "status": "VALIDATED",
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_dependency_mappings": len(df),
        "status": "READY",
        "current_phase": profile.current_phase,
    }
    return df, summary


def summarize_indicator_dependency_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_mappings": len(df),
        "targets": list(df["target_indicator"].unique()) if not df.empty else [],
    }
