import numpy as np
import pandas as pd


def calculate_true_range(df: pd.DataFrame) -> pd.DataFrame:
    high = df["high"]
    low = df["low"]
    close_prev = df["close"].shift(1)

    tr1 = high - low
    tr2 = abs(high - close_prev)
    tr3 = abs(low - close_prev)

    frames = [tr1, tr2, tr3]
    tr = pd.concat(frames, axis=1, join="inner").max(axis=1)

    return pd.DataFrame({"true_range": tr})


def calculate_atr(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    tr = calculate_true_range(df)["true_range"]
    atr = tr.rolling(window=window, min_periods=window).mean()
    return pd.DataFrame({f"atr_{window}": atr})


def calculate_bollinger_bands(
    df: pd.DataFrame, window: int = 20, num_std: float = 2.0
) -> pd.DataFrame:
    close = df["close"]
    sma = close.rolling(window=window, min_periods=window).mean()
    std = close.rolling(window=window, min_periods=window).std()

    upper_band = sma + (std * num_std)
    lower_band = sma - (std * num_std)

    bandwidth = (upper_band - lower_band) / sma
    percent_b = (close - lower_band) / (upper_band - lower_band)

    # Handle division by zero when upper == lower
    percent_b = percent_b.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame(
        {
            f"bb_upper_{window}_{int(num_std)}": upper_band,
            f"bb_mid_{window}_{int(num_std)}": sma,
            f"bb_lower_{window}_{int(num_std)}": lower_band,
            f"bb_width_{window}_{int(num_std)}": bandwidth,
            f"bb_percent_b_{window}_{int(num_std)}": percent_b,
        }
    )


def calculate_keltner_channels(
    df: pd.DataFrame, window: int = 20, atr_window: int = 10, multiplier: float = 2.0
) -> pd.DataFrame:
    ema = df["close"].ewm(span=window, adjust=False, min_periods=window).mean()
    atr = calculate_atr(df, window=atr_window)[f"atr_{atr_window}"]

    upper = ema + (multiplier * atr)
    lower = ema - (multiplier * atr)

    return pd.DataFrame(
        {
            f"keltner_upper_{window}": upper,
            f"keltner_mid_{window}": ema,
            f"keltner_lower_{window}": lower,
        }
    )


def calculate_donchian_channels(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    upper = df["high"].rolling(window=window, min_periods=window).max()
    lower = df["low"].rolling(window=window, min_periods=window).min()
    mid = (upper + lower) / 2

    return pd.DataFrame(
        {
            f"donchian_high_{window}": upper,
            f"donchian_low_{window}": lower,
            f"donchian_mid_{window}": mid,
        }
    )


def calculate_historical_volatility(
    df: pd.DataFrame, window: int = 20, annualization: int = 252
) -> pd.DataFrame:
    log_returns = np.log(df["close"] / df["close"].shift(1))
    hist_vol = log_returns.rolling(window=window, min_periods=window).std() * np.sqrt(
        annualization
    )
    return pd.DataFrame({f"hist_vol_{window}": hist_vol})
