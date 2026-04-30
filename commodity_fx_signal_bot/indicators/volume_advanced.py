import logging
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


def detect_volume_usability(df: pd.DataFrame) -> pd.DataFrame:
    if "volume" not in df.columns:
        return pd.DataFrame(
            {"volume_valid_ratio": 0.0, "volume_is_usable": False}, index=df.index
        )
    valid_ratio = (df["volume"] > 0).mean()
    is_usable = valid_ratio >= 0.60
    return pd.DataFrame(
        {"volume_valid_ratio": valid_ratio, "volume_is_usable": is_usable},
        index=df.index,
    )


def calculate_multi_volume_sma(
    df: pd.DataFrame, windows: tuple[int, ...] = (10, 20, 50, 100)
) -> pd.DataFrame:
    res = pd.DataFrame(index=df.index)
    if "volume" not in df.columns:
        return res
    for w in windows:
        res[f"volume_sma_{w}"] = df["volume"].rolling(w, min_periods=1).mean()
    return res


def calculate_multi_volume_zscore(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50)
) -> pd.DataFrame:
    res = pd.DataFrame(index=df.index)
    if "volume" not in df.columns:
        return res
    for w in windows:
        sma = df["volume"].rolling(w, min_periods=1).mean()
        std = df["volume"].rolling(w, min_periods=1).std()
        z = (df["volume"] - sma) / std
        res[f"volume_zscore_{w}"] = z.replace([np.inf, -np.inf], np.nan)
    return res


def calculate_relative_volume(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50)
) -> pd.DataFrame:
    res = pd.DataFrame(index=df.index)
    if "volume" not in df.columns:
        return res
    for w in windows:
        sma = df["volume"].rolling(w, min_periods=1).mean()
        res[f"relative_volume_{w}"] = (df["volume"] / sma).replace(
            [np.inf, -np.inf], np.nan
        )
    return res


def calculate_obv_advanced(df: pd.DataFrame) -> pd.DataFrame:
    if "volume" not in df.columns or "close" not in df.columns:
        return pd.DataFrame(index=df.index)
    close_diff = df["close"].diff()
    direction = pd.Series(0, index=df.index)
    direction[close_diff > 0] = 1
    direction[close_diff < 0] = -1
    obv = (df["volume"] * direction).cumsum()
    return pd.DataFrame({"obv": obv})


def calculate_obv_slope(df: pd.DataFrame, window: int = 10) -> pd.DataFrame:
    if "volume" not in df.columns or "close" not in df.columns:
        return pd.DataFrame(index=df.index)
    obv = calculate_obv_advanced(df)["obv"]
    slope = obv.diff(window) / window
    return pd.DataFrame({f"obv_slope_{window}": slope})


def calculate_mfi_multi(
    df: pd.DataFrame, windows: tuple[int, ...] = (14, 20)
) -> pd.DataFrame:
    res = pd.DataFrame(index=df.index)
    if "volume" not in df.columns:
        return res
    typical_price = (df["high"] + df["low"] + df["close"]) / 3
    raw_mf = typical_price * df["volume"]
    diff = typical_price.diff()
    pos_flow = pd.Series(0.0, index=df.index)
    neg_flow = pd.Series(0.0, index=df.index)
    pos_flow[diff > 0] = raw_mf[diff > 0]
    neg_flow[diff < 0] = raw_mf[diff < 0]

    for w in windows:
        pos_mf = pos_flow.rolling(w, min_periods=1).sum()
        neg_mf = neg_flow.rolling(w, min_periods=1).sum()
        mfi = 100 - (100 / (1 + (pos_mf / neg_mf)))
        res[f"mfi_{w}"] = mfi.replace([np.inf, -np.inf], np.nan)
    return res


def calculate_cmf_multi(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50)
) -> pd.DataFrame:
    res = pd.DataFrame(index=df.index)
    if "volume" not in df.columns:
        return res
    mf_mult = ((df["close"] - df["low"]) - (df["high"] - df["close"])) / (
        df["high"] - df["low"]
    )
    mf_mult = mf_mult.replace([np.inf, -np.inf, np.nan], 0)
    mf_vol = mf_mult * df["volume"]

    for w in windows:
        cmf = (
            mf_vol.rolling(w, min_periods=1).sum()
            / df["volume"].rolling(w, min_periods=1).sum()
        )
        res[f"cmf_{w}"] = cmf.replace([np.inf, -np.inf], np.nan)
    return res


def calculate_accumulation_distribution(df: pd.DataFrame) -> pd.DataFrame:
    if "volume" not in df.columns:
        return pd.DataFrame(index=df.index)
    mf_mult = ((df["close"] - df["low"]) - (df["high"] - df["close"])) / (
        df["high"] - df["low"]
    )
    mf_mult = mf_mult.replace([np.inf, -np.inf, np.nan], 0)
    adl = (mf_mult * df["volume"]).cumsum()
    return pd.DataFrame({"accumulation_distribution": adl})


def calculate_chaikin_oscillator(
    df: pd.DataFrame, fast: int = 3, slow: int = 10
) -> pd.DataFrame:
    if "volume" not in df.columns:
        return pd.DataFrame(index=df.index)
    adl = calculate_accumulation_distribution(df)["accumulation_distribution"]
    ema_fast = adl.ewm(span=fast, adjust=False).mean()
    ema_slow = adl.ewm(span=slow, adjust=False).mean()
    return pd.DataFrame({f"chaikin_osc_{fast}_{slow}": ema_fast - ema_slow})


def calculate_price_volume_trend(df: pd.DataFrame) -> pd.DataFrame:
    if "volume" not in df.columns:
        return pd.DataFrame(index=df.index)
    close_pct = df["close"].pct_change().fillna(0)
    pvt = (df["volume"] * close_pct).cumsum()
    return pd.DataFrame({"pvt": pvt})


def calculate_volume_price_confirmation(
    df: pd.DataFrame, price_window: int = 10, volume_window: int = 20
) -> pd.DataFrame:
    if "volume" not in df.columns:
        return pd.DataFrame(index=df.index)
    price_pct = df["close"].pct_change(price_window)
    vol_sma = df["volume"].rolling(volume_window).mean()
    vol_pct = df["volume"] / vol_sma - 1
    confirm = price_pct * vol_pct
    diverge = -confirm
    return pd.DataFrame(
        {
            f"price_volume_confirm_{price_window}_{volume_window}": confirm,
            f"price_volume_diverge_{price_window}_{volume_window}": diverge,
        }
    )


def calculate_dollar_volume_proxy(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50)
) -> pd.DataFrame:
    res = pd.DataFrame(index=df.index)
    if "volume" not in df.columns:
        return res
    dv = df["close"] * df["volume"]
    res["dollar_volume_proxy"] = dv
    for w in windows:
        res[f"dollar_volume_sma_{w}"] = dv.rolling(w).mean()
    return res


def calculate_liquidity_proxy(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50)
) -> pd.DataFrame:
    res = pd.DataFrame(index=df.index)
    if "volume" not in df.columns:
        return res
    tr = df["high"] - df["low"]
    tr = tr.replace(0, np.nan)
    for w in windows:
        amihud = (
            (df["close"].pct_change().abs() / (df["volume"] * df["close"]))
            .rolling(w)
            .mean()
        )
        # Liquidity proxy is inverse amihud basically or just 1/amihud
        res[f"liquidity_proxy_{w}"] = (1 / amihud).replace([np.inf, -np.inf], np.nan)
    return res


def calculate_volume_percentile(
    df: pd.DataFrame, source_col: str = "volume", window: int = 120
) -> pd.DataFrame:
    if source_col not in df.columns:
        return pd.DataFrame(index=df.index)
    pct = (
        df[source_col]
        .rolling(window)
        .apply(lambda x: pd.Series(x).rank(pct=True).iloc[-1])
    )
    return pd.DataFrame({f"volume_percentile_{window}": pct})
