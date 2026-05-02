import numpy as np
import pandas as pd


def calculate_monthly_change(series: pd.Series) -> pd.Series:
    """Calculate month-over-month percentage change."""
    mom = series.pct_change()
    # Replace infinite values with NaN
    mom = mom.replace([np.inf, -np.inf], np.nan)
    return mom


def calculate_yoy_change(series: pd.Series, periods: int = 12) -> pd.Series:
    """Calculate year-over-year percentage change (default 12 periods for monthly data)."""
    yoy = series.pct_change(periods=periods)
    yoy = yoy.replace([np.inf, -np.inf], np.nan)
    return yoy


def calculate_annualized_inflation(series: pd.Series, periods: int = 12) -> pd.Series:
    """Calculate annualized inflation based on the n-period change."""
    # Assuming series is an index level, annualized from a single period
    mom = series.pct_change()
    # Replace infinite values with NaN early
    mom = mom.replace([np.inf, -np.inf], np.nan)
    annualized = ((1 + mom) ** periods) - 1
    annualized = annualized.replace([np.inf, -np.inf], np.nan)
    return annualized


def calculate_inflation_momentum(yoy_series: pd.Series, window: int = 3) -> pd.Series:
    """Calculate inflation momentum as the change in YoY inflation over a window."""
    mom_momentum = yoy_series.diff(periods=window)
    return mom_momentum


def build_inflation_feature_frame(
    df: pd.DataFrame, prefix: str
) -> tuple[pd.DataFrame, dict]:
    """Build inflation feature frame from a value column."""
    if df.empty or "value" not in df.columns:
        return pd.DataFrame(), {"error": "Empty dataframe or missing value column"}

    series = df["value"].copy()

    # Forward fill up to some reasonable limit so calculations work on missing months
    # Not using large limit here to prevent generating stale fake data
    series = series.ffill(limit=3)

    result = pd.DataFrame(index=df.index)

    result[f"{prefix}_level"] = series
    result[f"{prefix}_mom"] = calculate_monthly_change(series)
    result[f"{prefix}_yoy"] = calculate_yoy_change(series, periods=12)
    result[f"{prefix}_annualized"] = calculate_annualized_inflation(series, periods=12)

    yoy_series = result[f"{prefix}_yoy"]
    result[f"{prefix}_momentum_3m"] = calculate_inflation_momentum(yoy_series, window=3)

    result[f"{prefix}_yoy_rising"] = (result[f"{prefix}_momentum_3m"] > 0).astype(int)
    result[f"{prefix}_yoy_falling"] = (result[f"{prefix}_momentum_3m"] < 0).astype(int)

    # Since we use boolean astype(int), missing values will become 0. We might want them as NaN where original is NaN
    mask = result[f"{prefix}_momentum_3m"].isna()
    result.loc[mask, f"{prefix}_yoy_rising"] = np.nan
    result.loc[mask, f"{prefix}_yoy_falling"] = np.nan

    summary = {"rows": len(result), "columns": list(result.columns), "prefix": prefix}

    return result, summary
