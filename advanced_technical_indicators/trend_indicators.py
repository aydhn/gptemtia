from typing import Tuple, Dict, Any
import numpy as np
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile

FORBIDDEN_COLUMNS = {
    "signal", "buy", "sell", "long", "short", "position",
    "target", "label", "prediction", "recommendation",
    "future_return", "forward_return", "next_return"
}


def _validate_output_field(col: str) -> None:
    if col.lower() in FORBIDDEN_COLUMNS:
        raise ValueError(f"Forbidden column name '{col}' detected. Non-signal indicator only.")


def _validate_required(df: pd.DataFrame, fields: list[str]) -> None:
    for f in fields:
        if f not in df.columns:
            raise ValueError(f"Required field '{f}' is missing from DataFrame.")


def add_macd(
    df: pd.DataFrame,
    field: str = "close",
    fast: int = 12,
    slow: int = 26,
    signal_window: int = 9,
    prefix: str = "macd",
) -> pd.DataFrame:
    _validate_required(df, [field])
    line_col = f"{prefix}_line"
    smooth_col = f"{prefix}_smooth"  # Replaces forbidden 'signal' name
    hist_col = f"{prefix}_hist"
    for col in [line_col, smooth_col, hist_col]:
        _validate_output_field(col)

    out = df.copy()
    ema_fast = out[field].ewm(span=fast, adjust=False).mean()
    ema_slow = out[field].ewm(span=slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    macd_smooth = macd_line.ewm(span=signal_window, adjust=False).mean()
    macd_hist = macd_line - macd_smooth

    out[line_col] = macd_line.astype(float)
    out[smooth_col] = macd_smooth.astype(float)
    out[hist_col] = macd_hist.astype(float)
    return out


def add_ppo(
    df: pd.DataFrame,
    field: str = "close",
    fast: int = 12,
    slow: int = 26,
    signal_window: int = 9,
    prefix: str = "ppo",
) -> pd.DataFrame:
    _validate_required(df, [field])
    line_col = f"{prefix}_line"
    smooth_col = f"{prefix}_smooth"
    hist_col = f"{prefix}_hist"
    for col in [line_col, smooth_col, hist_col]:
        _validate_output_field(col)

    out = df.copy()
    ema_fast = out[field].ewm(span=fast, adjust=False).mean()
    ema_slow = out[field].ewm(span=slow, adjust=False).mean()
    ppo_line = ((ema_fast - ema_slow) / ema_slow.replace(0, np.nan)) * 100.0
    ppo_smooth = ppo_line.ewm(span=signal_window, adjust=False).mean()
    ppo_hist = ppo_line - ppo_smooth

    out[line_col] = ppo_line.astype(float)
    out[smooth_col] = ppo_smooth.astype(float)
    out[hist_col] = ppo_hist.astype(float)
    return out


def add_donchian_channel(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    window: int = 20,
    prefix: str = "donchian",
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field])
    upper_col = f"{prefix}_upper_{window}"
    lower_col = f"{prefix}_lower_{window}"
    mid_col = f"{prefix}_mid_{window}"
    for col in [upper_col, lower_col, mid_col]:
        _validate_output_field(col)

    out = df.copy()
    upper = out[high_field].rolling(window=window).max()
    lower = out[low_field].rolling(window=window).min()
    mid = (upper + lower) / 2.0

    out[upper_col] = upper.astype(float)
    out[lower_col] = lower.astype(float)
    out[mid_col] = mid.astype(float)
    return out


def add_aroon(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    window: int = 25,
    prefix: str = "aroon",
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field])
    up_col = f"{prefix}_up_{window}"
    down_col = f"{prefix}_down_{window}"
    osc_col = f"{prefix}_osc_{window}"
    for col in [up_col, down_col, osc_col]:
        _validate_output_field(col)

    out = df.copy()

    def _days_since_max(s):
        return window - 1 - np.argmax(s)

    def _days_since_min(s):
        return window - 1 - np.argmin(s)

    high_dist = out[high_field].rolling(window=window).apply(_days_since_max, raw=True)
    low_dist = out[low_field].rolling(window=window).apply(_days_since_min, raw=True)

    aroon_up = ((window - high_dist) / float(window)) * 100.0
    aroon_down = ((window - low_dist) / float(window)) * 100.0
    aroon_osc = aroon_up - aroon_down

    out[up_col] = aroon_up.astype(float)
    out[down_col] = aroon_down.astype(float)
    out[osc_col] = aroon_osc.astype(float)
    return out


def add_adx_dmi_placeholder(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    window: int = 14,
    prefix: str = "adx",
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    plus_di_col = f"{prefix}_plus_di_{window}"
    minus_di_col = f"{prefix}_minus_di_{window}"
    adx_col = f"{prefix}_val_{window}"
    for col in [plus_di_col, minus_di_col, adx_col]:
        _validate_output_field(col)

    out = df.copy()
    high = out[high_field]
    low = out[low_field]
    close = out[close_field]
    prev_close = close.shift(1)
    prev_high = high.shift(1)
    prev_low = low.shift(1)

    tr = np.maximum(high - low, np.maximum(np.abs(high - prev_close), np.abs(low - prev_close)))
    atr_val = pd.Series(tr).rolling(window=window).mean().replace(0, np.nan)

    up_move = high - prev_high
    down_move = prev_low - low

    plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0.0)
    minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0.0)

    plus_di = 100.0 * (pd.Series(plus_dm, index=out.index).rolling(window=window).mean() / atr_val)
    minus_di = 100.0 * (pd.Series(minus_dm, index=out.index).rolling(window=window).mean() / atr_val)
    dx_denom = (plus_di + minus_di).replace(0, np.nan)
    dx = 100.0 * np.abs(plus_di - minus_di) / dx_denom
    adx_series = dx.rolling(window=window).mean()

    out[plus_di_col] = plus_di.astype(float)
    out[minus_di_col] = minus_di.astype(float)
    out[adx_col] = adx_series.astype(float)
    return out


def add_ichimoku_placeholder(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    prefix: str = "ichimoku",
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    tenkan_col = f"{prefix}_tenkan"
    kijun_col = f"{prefix}_kijun"
    senkou_a_col = f"{prefix}_senkou_a"
    senkou_b_col = f"{prefix}_senkou_b"
    for col in [tenkan_col, kijun_col, senkou_a_col, senkou_b_col]:
        _validate_output_field(col)

    out = df.copy()
    high = out[high_field]
    low = out[low_field]

    # Tenkan-sen (9)
    tenkan = (high.rolling(window=9).max() + low.rolling(window=9).min()) / 2.0
    # Kijun-sen (26)
    kijun = (high.rolling(window=26).max() + low.rolling(window=26).min()) / 2.0
    # Senkou Span A (mean of tenkan & kijun, unshifted to avoid forward lookahead)
    senkou_a = (tenkan + kijun) / 2.0
    # Senkou Span B (52 period midpoint, unshifted to avoid forward lookahead)
    senkou_b = (high.rolling(window=52).max() + low.rolling(window=52).min()) / 2.0

    out[tenkan_col] = tenkan.astype(float)
    out[kijun_col] = kijun.astype(float)
    out[senkou_a_col] = senkou_a.astype(float)
    out[senkou_b_col] = senkou_b.astype(float)
    return out


def build_trend_indicator_expansion_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "macd", "output_pattern": "macd_line, macd_smooth, macd_hist", "parameters": {"fast": 12, "slow": 26, "signal": 9}},
        {"indicator_name": "ppo", "output_pattern": "ppo_line, ppo_smooth, ppo_hist", "parameters": {"fast": 12, "slow": 26, "signal": 9}},
        {"indicator_name": "donchian_channel", "output_pattern": "donchian_upper, donchian_lower, donchian_mid", "parameters": {"window": 20}},
        {"indicator_name": "aroon", "output_pattern": "aroon_up, aroon_down, aroon_osc", "parameters": {"window": 25}},
        {"indicator_name": "adx_dmi", "output_pattern": "adx_plus_di, adx_minus_di, adx_val", "parameters": {"window": 14}},
        {"indicator_name": "ichimoku", "output_pattern": "ichimoku_tenkan, kijun, senkou_a, senkou_b", "parameters": {}},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_trend"
    df["non_signal"] = True
    summary = {
        "family": "family_trend",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
