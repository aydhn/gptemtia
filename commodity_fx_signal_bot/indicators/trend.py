import numpy as np
import pandas as pd


def calculate_sma(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    sma = df["close"].rolling(window=window, min_periods=window).mean()
    return pd.DataFrame({f"sma_{window}": sma})


def calculate_ema(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    ema = df["close"].ewm(span=window, adjust=False, min_periods=window).mean()
    return pd.DataFrame({f"ema_{window}": ema})


def calculate_macd(
    df: pd.DataFrame, fast: int = 12, slow: int = 26, signal: int = 9
) -> pd.DataFrame:
    ema_fast = df["close"].ewm(span=fast, adjust=False, min_periods=fast).mean()
    ema_slow = df["close"].ewm(span=slow, adjust=False, min_periods=slow).mean()

    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False, min_periods=signal).mean()
    macd_hist = macd_line - signal_line

    return pd.DataFrame(
        {
            f"macd_{fast}_{slow}_{signal}": macd_line,
            f"macd_signal_{fast}_{slow}_{signal}": signal_line,
            f"macd_hist_{fast}_{slow}_{signal}": macd_hist,
        }
    )


def calculate_adx(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    high = df["high"]
    low = df["low"]
    close = df["close"]

    plus_dm = high.diff()
    minus_dm = low.diff()

    plus_dm[plus_dm < 0] = 0
    plus_dm[plus_dm < -minus_dm] = 0

    minus_dm = -minus_dm
    minus_dm[minus_dm < 0] = 0
    minus_dm[minus_dm < plus_dm] = 0

    tr1 = pd.DataFrame(high - low)
    tr2 = pd.DataFrame(abs(high - close.shift(1)))
    tr3 = pd.DataFrame(abs(low - close.shift(1)))
    frames = [tr1, tr2, tr3]
    tr = pd.concat(frames, axis=1, join="inner").max(axis=1)
    atr = tr.rolling(window=window, min_periods=window).mean()

    plus_di = 100 * (plus_dm.rolling(window=window, min_periods=window).mean() / atr)
    minus_di = 100 * (minus_dm.rolling(window=window, min_periods=window).mean() / atr)

    dx = 100 * abs((plus_di - minus_di) / (plus_di + minus_di))
    adx = dx.rolling(window=window, min_periods=window).mean()

    return pd.DataFrame(
        {
            f"adx_{window}": adx,
            f"plus_di_{window}": plus_di,
            f"minus_di_{window}": minus_di,
        }
    )


def calculate_aroon(df: pd.DataFrame, window: int = 25) -> pd.DataFrame:
    high = df["high"]
    low = df["low"]

    aroon_up = high.rolling(window=window, min_periods=window).apply(
        lambda x: float(np.argmax(x)) / window * 100
    )
    aroon_down = low.rolling(window=window, min_periods=window).apply(
        lambda x: float(np.argmin(x)) / window * 100
    )

    return pd.DataFrame(
        {f"aroon_up_{window}": aroon_up, f"aroon_down_{window}": aroon_down}
    )


def calculate_ichimoku_basic(df: pd.DataFrame) -> pd.DataFrame:
    high = df["high"]
    low = df["low"]

    # Tenkan-sen (Conversion Line): (9-period high + 9-period low)/2
    period9_high = high.rolling(window=9, min_periods=9).max()
    period9_low = low.rolling(window=9, min_periods=9).min()
    tenkan_sen = (period9_high + period9_low) / 2

    # Kijun-sen (Base Line): (26-period high + 26-period low)/2
    period26_high = high.rolling(window=26, min_periods=26).max()
    period26_low = low.rolling(window=26, min_periods=26).min()
    kijun_sen = (period26_high + period26_low) / 2

    # Senkou Span A (Leading Span A): (Conversion Line + Base Line)/2
    senkou_span_a = ((tenkan_sen + kijun_sen) / 2).shift(26)

    # Senkou Span B (Leading Span B): (52-period high + 52-period low)/2
    period52_high = high.rolling(window=52, min_periods=52).max()
    period52_low = low.rolling(window=52, min_periods=52).min()
    senkou_span_b = ((period52_high + period52_low) / 2).shift(26)

    return pd.DataFrame(
        {
            "ichimoku_tenkan": tenkan_sen,
            "ichimoku_kijun": kijun_sen,
            "ichimoku_span_a": senkou_span_a,
            "ichimoku_span_b": senkou_span_b,
        }
    )
