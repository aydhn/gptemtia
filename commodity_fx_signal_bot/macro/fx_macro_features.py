import numpy as np
import pandas as pd


def calculate_fx_returns(
    series: pd.Series, windows: tuple[int, ...] = (21, 63, 126, 252)
) -> pd.DataFrame:
    """Calculate rolling returns for different windows."""
    df = pd.DataFrame(index=series.index)
    for w in windows:
        ret = series.pct_change(periods=w)
        ret = ret.replace([np.inf, -np.inf], np.nan)
        df[f"return_{w}d"] = ret
    return df


def calculate_fx_trend_features(series: pd.Series) -> pd.DataFrame:
    """Calculate moving averages and trend proxies."""
    df = pd.DataFrame(index=series.index)

    df["sma_50"] = series.rolling(window=50, min_periods=20).mean()
    df["sma_200"] = series.rolling(window=200, min_periods=60).mean()

    df["above_sma_200"] = (series > df["sma_200"]).astype(float)
    df.loc[df["sma_200"].isna(), "above_sma_200"] = np.nan

    # trend strength proxy: Distance from 200 SMA
    df["trend_strength_proxy"] = (series - df["sma_200"]) / df["sma_200"]
    df["trend_strength_proxy"] = df["trend_strength_proxy"].replace(
        [np.inf, -np.inf], np.nan
    )

    return df


def calculate_fx_volatility_features(series: pd.Series) -> pd.DataFrame:
    """Calculate historical volatility features."""
    df = pd.DataFrame(index=series.index)

    daily_ret = series.pct_change()
    daily_ret = daily_ret.replace([np.inf, -np.inf], np.nan)

    # annualized vol (~252 trading days)
    df["vol_21d"] = daily_ret.rolling(window=21).std() * np.sqrt(252)
    df["vol_63d"] = daily_ret.rolling(window=63).std() * np.sqrt(252)

    return df


def build_fx_macro_feature_frame(
    df: pd.DataFrame, prefix: str = "usdtry"
) -> tuple[pd.DataFrame, dict]:
    """Build FX macro features."""
    if df.empty or "value" not in df.columns:
        return pd.DataFrame(), {"error": "Empty dataframe or missing value column"}

    series = df["value"].copy()

    # forward fill to avoid NaN issues if requested
    series = series.ffill(limit=5)

    result = pd.DataFrame(index=df.index)

    # Calculate returns
    returns_df = calculate_fx_returns(series, windows=(21, 63, 126, 252))
    returns_df = returns_df.add_prefix(f"{prefix}_")
    result = pd.concat([result, returns_df], axis=1)

    # Calculate trend features
    trend_df = calculate_fx_trend_features(series)
    trend_df = trend_df.add_prefix(f"{prefix}_")
    result = pd.concat([result, trend_df], axis=1)

    # Calculate volatility features
    vol_df = calculate_fx_volatility_features(series)
    vol_df = vol_df.add_prefix(f"{prefix}_")
    result = pd.concat([result, vol_df], axis=1)

    # Depreciation pressure: Combining trend strength and positive returns
    # e.g., if return 126d > 0.1 (10%) and above sma 200
    if (
        f"{prefix}_return_126d" in result.columns
        and f"{prefix}_above_sma_200" in result.columns
    ):
        pressure = (result[f"{prefix}_return_126d"] > 0.10) & (
            result[f"{prefix}_above_sma_200"] > 0
        )
        result[f"{prefix}_depreciation_pressure"] = pressure.astype(float)

        # mask nan where inputs are nan
        mask = (
            result[f"{prefix}_return_126d"].isna()
            | result[f"{prefix}_above_sma_200"].isna()
        )
        result.loc[mask, f"{prefix}_depreciation_pressure"] = np.nan
    else:
        result[f"{prefix}_depreciation_pressure"] = np.nan

    summary = {"rows": len(result), "columns": list(result.columns), "prefix": prefix}

    return result, summary
