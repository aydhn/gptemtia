from typing import Optional
import numpy as np
import pandas as pd

FORBIDDEN_OUTPUT_NAMES = {
    "signal", "buy", "sell", "long", "short",
    "position", "target", "label", "prediction", "recommendation",
}


def _check_output_field(output_field: str) -> None:
    if output_field.lower() in FORBIDDEN_OUTPUT_NAMES:
        raise ValueError(
            f"Forbidden output column name '{output_field}'. "
            f"The feature engine strictly prohibits signal/target column names."
        )


def add_close_return(
    df: pd.DataFrame,
    close_field: str = "close",
    window: int = 1,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    if close_field not in df.columns:
        raise ValueError(f"Required close field '{close_field}' not found in DataFrame.")
    out_col = output_field or f"close_return_{window}"
    _check_output_field(out_col)

    res = df.copy()
    if res.empty:
        res[out_col] = pd.Series(dtype=float)
        return res

    res[out_col] = res[close_field].pct_change(periods=window)
    return res


def add_log_return(
    df: pd.DataFrame,
    close_field: str = "close",
    window: int = 1,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    if close_field not in df.columns:
        raise ValueError(f"Required close field '{close_field}' not found in DataFrame.")
    out_col = output_field or f"log_return_{window}"
    _check_output_field(out_col)

    res = df.copy()
    if res.empty:
        res[out_col] = pd.Series(dtype=float)
        return res

    series = res[close_field]
    shifted = series.shift(window)
    valid_mask = (series > 0) & (shifted > 0)
    log_ret = pd.Series(np.nan, index=res.index, dtype=float)
    log_ret[valid_mask] = np.log(series[valid_mask] / shifted[valid_mask])
    res[out_col] = log_ret
    return res


def add_rolling_mean(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    if field not in df.columns:
        raise ValueError(f"Required field '{field}' not found in DataFrame.")
    out_col = output_field or f"rolling_mean_{window}"
    _check_output_field(out_col)

    res = df.copy()
    if res.empty:
        res[out_col] = pd.Series(dtype=float)
        return res

    res[out_col] = res[field].rolling(window=window).mean()
    return res


def add_rolling_std(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    if field not in df.columns:
        raise ValueError(f"Required field '{field}' not found in DataFrame.")
    out_col = output_field or f"rolling_std_{window}"
    _check_output_field(out_col)

    res = df.copy()
    if res.empty:
        res[out_col] = pd.Series(dtype=float)
        return res

    res[out_col] = res[field].rolling(window=window).std()
    return res


def add_sma(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    out_col = output_field or f"sma_{window}"
    return add_rolling_mean(df, field=field, window=window, output_field=out_col)


def add_ema(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    if field not in df.columns:
        raise ValueError(f"Required field '{field}' not found in DataFrame.")
    out_col = output_field or f"ema_{window}"
    _check_output_field(out_col)

    res = df.copy()
    if res.empty:
        res[out_col] = pd.Series(dtype=float)
        return res

    res[out_col] = res[field].ewm(span=window, adjust=False).mean()
    return res


def add_true_range(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    output_field: str = "true_range",
) -> pd.DataFrame:
    for f in [high_field, low_field, close_field]:
        if f not in df.columns:
            raise ValueError(f"Required field '{f}' not found in DataFrame.")
    _check_output_field(output_field)

    res = df.copy()
    if res.empty:
        res[output_field] = pd.Series(dtype=float)
        return res

    high = res[high_field]
    low = res[low_field]
    prev_close = res[close_field].shift(1)

    tr1 = high - low
    tr2 = (high - prev_close).abs()
    tr3 = (low - prev_close).abs()

    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    res[output_field] = tr
    return res


def add_atr(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    window: int = 14,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    out_col = output_field or f"atr_{window}"
    _check_output_field(out_col)

    res = add_true_range(df, high_field=high_field, low_field=low_field, close_field=close_field, output_field="_tmp_tr")
    res[out_col] = res["_tmp_tr"].rolling(window=window).mean()
    res.drop(columns=["_tmp_tr"], inplace=True)
    return res


def add_rsi(
    df: pd.DataFrame,
    close_field: str = "close",
    window: int = 14,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    if close_field not in df.columns:
        raise ValueError(f"Required close field '{close_field}' not found in DataFrame.")
    out_col = output_field or f"rsi_{window}"
    _check_output_field(out_col)

    res = df.copy()
    if res.empty:
        res[out_col] = pd.Series(dtype=float)
        return res

    delta = res[close_field].diff(1)
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)

    avg_gain = gain.rolling(window=window, min_periods=window).mean()
    avg_loss = loss.rolling(window=window, min_periods=window).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    rsi = 100.0 - (100.0 / (1.0 + rs))

    rsi = rsi.where(~(avg_loss == 0), 100.0)
    rsi = rsi.where(~((avg_loss == 0) & (avg_gain == 0)), 50.0)

    res[out_col] = rsi
    return res


def add_bollinger_zscore(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    if field not in df.columns:
        raise ValueError(f"Required field '{field}' not found in DataFrame.")
    out_col = output_field or f"bollinger_zscore_{window}"
    _check_output_field(out_col)

    res = df.copy()
    if res.empty:
        res[out_col] = pd.Series(dtype=float)
        return res

    mean = res[field].rolling(window=window).mean()
    std = res[field].rolling(window=window).std()

    res[out_col] = (res[field] - mean) / (2.0 * std.replace(0, np.nan))
    return res


def add_quote_mid(
    df: pd.DataFrame,
    bid_field: str = "bid",
    ask_field: str = "ask",
    output_field: str = "quote_mid",
) -> pd.DataFrame:
    for f in [bid_field, ask_field]:
        if f not in df.columns:
            raise ValueError(f"Required field '{f}' not found in DataFrame.")
    _check_output_field(output_field)

    res = df.copy()
    if res.empty:
        res[output_field] = pd.Series(dtype=float)
        return res

    res[output_field] = (res[bid_field] + res[ask_field]) / 2.0
    return res


def add_quote_spread(
    df: pd.DataFrame,
    bid_field: str = "bid",
    ask_field: str = "ask",
    output_field: str = "quote_spread",
) -> pd.DataFrame:
    for f in [bid_field, ask_field]:
        if f not in df.columns:
            raise ValueError(f"Required field '{f}' not found in DataFrame.")
    _check_output_field(output_field)

    res = df.copy()
    if res.empty:
        res[output_field] = pd.Series(dtype=float)
        return res

    res[output_field] = res[ask_field] - res[bid_field]
    return res
