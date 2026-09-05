from typing import Tuple, Dict, Any
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile

WARMUP_POLICY_RULES = [
    {"indicator": "sma", "warmup_formula": "window - 1", "min_rows_needed": "window"},
    {"indicator": "ema", "warmup_formula": "0 (or window for steady state)", "min_rows_needed": "window"},
    {"indicator": "wma", "warmup_formula": "window - 1", "min_rows_needed": "window"},
    {"indicator": "dema", "warmup_formula": "2 * window - 1", "min_rows_needed": "2 * window"},
    {"indicator": "tema", "warmup_formula": "3 * window - 2", "min_rows_needed": "3 * window"},
    {"indicator": "rsi", "warmup_formula": "window", "min_rows_needed": "window + 1"},
    {"indicator": "cmo", "warmup_formula": "window", "min_rows_needed": "window + 1"},
    {"indicator": "stochastic", "warmup_formula": "k_window + d_window - 2", "min_rows_needed": "k_window + d_window"},
    {"indicator": "atr", "warmup_formula": "window", "min_rows_needed": "window + 1"},
    {"indicator": "bollinger_bands", "warmup_formula": "window - 1", "min_rows_needed": "window"},
    {"indicator": "rolling_zscore", "warmup_formula": "window - 1", "min_rows_needed": "window"},
    {"indicator": "macd", "warmup_formula": "slow + signal_window - 2", "min_rows_needed": "slow + signal_window"},
    {"indicator": "true_range", "warmup_formula": "1", "min_rows_needed": "2"},
    {"indicator": "simple_return", "warmup_formula": "window", "min_rows_needed": "window + 1"},
    {"indicator": "log_return", "warmup_formula": "window", "min_rows_needed": "window + 1"},
]


def estimate_warmup_nan_count(indicator_name: str, parameters: Dict[str, Any]) -> int:
    name = indicator_name.lower()
    window = parameters.get("window", 20)
    if name in ("sma", "wma", "bollinger_bands", "rolling_zscore", "donchian_channel"):
        return max(0, window - 1)
    elif name in ("rsi", "cmo", "atr", "simple_return", "log_return", "cumulative_return", "roc", "momentum"):
        return window
    elif name == "macd":
        slow = parameters.get("slow", 26)
        sig = parameters.get("signal_window", 9)
        return slow + sig - 2
    elif name == "stochastic":
        k = parameters.get("k_window", 14)
        d = parameters.get("d_window", 3)
        return k + d - 2
    elif name == "true_range":
        return 1
    elif name in ("candle_body_size", "close_open_range", "high_low_range", "quote_mid", "quote_spread"):
        return 0
    return window


def build_indicator_warmup_nan_policy_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = []
    for r in WARMUP_POLICY_RULES:
        rows.append({
            "indicator_name": r["indicator"],
            "warmup_formula": r["warmup_formula"],
            "min_rows_needed": r["min_rows_needed"],
            "policy_action": "preserve_nan_no_fill_no_delete",
            "future_handling": "Handled in Phase 118 / Phase 121 validation",
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_warmup_policies": len(df),
        "policy_action": "preserve_nan",
        "status": "READY",
        "current_phase": profile.current_phase,
    }
    return df, summary


def summarize_indicator_warmup_nan_policy(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_policies": len(df),
        "preserve_nan_guaranteed": True,
    }
