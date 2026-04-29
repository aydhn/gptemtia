import pandas as pd

try:
    pass

    TA_AVAILABLE = True
except ImportError:
    TA_AVAILABLE = False


def calculate_rsi(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    close = df["close"]
    delta = close.diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)

    avg_gain = gain.rolling(window=window, min_periods=window).mean()
    avg_loss = loss.rolling(window=window, min_periods=window).mean()

    # Calculate Wilder's smoothing
    for i in range(window, len(close)):
        avg_gain.iloc[i] = (avg_gain.iloc[i - 1] * (window - 1) + gain.iloc[i]) / window
        avg_loss.iloc[i] = (avg_loss.iloc[i - 1] * (window - 1) + loss.iloc[i]) / window

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    # Handle division by zero
    rsi.loc[avg_loss == 0] = 100
    rsi.loc[(avg_gain == 0) & (avg_loss == 0)] = 50

    return pd.DataFrame({f"rsi_{window}": rsi})


def calculate_stochastic(
    df: pd.DataFrame, window: int = 14, smooth_window: int = 3
) -> pd.DataFrame:
    high = df["high"]
    low = df["low"]
    close = df["close"]

    lowest_low = low.rolling(window=window, min_periods=window).min()
    highest_high = high.rolling(window=window, min_periods=window).max()

    stoch_k = 100 * ((close - lowest_low) / (highest_high - lowest_low))
    stoch_d = stoch_k.rolling(window=smooth_window, min_periods=smooth_window).mean()

    return pd.DataFrame(
        {
            f"stoch_k_{window}_{smooth_window}": stoch_k,
            f"stoch_d_{window}_{smooth_window}": stoch_d,
        }
    )


def calculate_stoch_rsi(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    rsi_df = calculate_rsi(df, window=window)
    rsi = rsi_df[f"rsi_{window}"]

    min_rsi = rsi.rolling(window=window, min_periods=window).min()
    max_rsi = rsi.rolling(window=window, min_periods=window).max()

    stoch_rsi = (rsi - min_rsi) / (max_rsi - min_rsi)

    return pd.DataFrame({f"stoch_rsi_{window}": stoch_rsi})


def calculate_roc(df: pd.DataFrame, window: int = 10) -> pd.DataFrame:
    close = df["close"]
    roc = ((close - close.shift(window)) / close.shift(window)) * 100
    return pd.DataFrame({f"roc_{window}": roc})


def calculate_momentum(df: pd.DataFrame, window: int = 10) -> pd.DataFrame:
    close = df["close"]
    momentum = close - close.shift(window)
    return pd.DataFrame({f"momentum_{window}": momentum})


def calculate_williams_r(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    high = df["high"]
    low = df["low"]
    close = df["close"]

    highest_high = high.rolling(window=window, min_periods=window).max()
    lowest_low = low.rolling(window=window, min_periods=window).min()

    williams_r = -100 * ((highest_high - close) / (highest_high - lowest_low))
    return pd.DataFrame({f"williams_r_{window}": williams_r})
