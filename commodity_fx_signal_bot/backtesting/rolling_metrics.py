import pandas as pd
import numpy as np


def calculate_rolling_returns(
    equity_curve: pd.DataFrame, windows: tuple[int, ...] = (20, 60, 120, 252)
) -> pd.DataFrame:
    if equity_curve.empty or "equity" not in equity_curve.columns:
        return pd.DataFrame()

    df = pd.DataFrame(index=equity_curve.index)

    for window in windows:
        df[f"rolling_return_{window}"] = equity_curve["equity"].pct_change(
            periods=window
        )

    return df


def calculate_rolling_volatility(
    equity_curve: pd.DataFrame,
    windows: tuple[int, ...] = (20, 60, 120, 252),
    trading_days_per_year: int = 252,
) -> pd.DataFrame:
    if equity_curve.empty or "equity" not in equity_curve.columns:
        return pd.DataFrame()

    df = pd.DataFrame(index=equity_curve.index)
    daily_returns = equity_curve["equity"].pct_change()

    for window in windows:
        rolling_std = daily_returns.rolling(window=window).std()
        df[f"rolling_volatility_{window}"] = rolling_std * np.sqrt(
            trading_days_per_year
        )

    return df


def calculate_rolling_sharpe(
    equity_curve: pd.DataFrame,
    windows: tuple[int, ...] = (60, 120, 252),
    risk_free_rate_annual: float = 0.0,
    trading_days_per_year: int = 252,
) -> pd.DataFrame:
    if equity_curve.empty or "equity" not in equity_curve.columns:
        return pd.DataFrame()

    df = pd.DataFrame(index=equity_curve.index)
    daily_returns = equity_curve["equity"].pct_change()
    daily_rf = (1 + risk_free_rate_annual) ** (1 / trading_days_per_year) - 1
    excess_returns = daily_returns - daily_rf

    for window in windows:
        rolling_mean = excess_returns.rolling(window=window).mean()
        rolling_std = excess_returns.rolling(window=window).std()

        rolling_std_safe = rolling_std.replace(0, np.nan)

        rolling_sharpe = (rolling_mean / rolling_std_safe) * np.sqrt(
            trading_days_per_year
        )
        df[f"rolling_sharpe_{window}"] = rolling_sharpe.fillna(0)

    return df


def calculate_rolling_drawdown(
    equity_curve: pd.DataFrame, windows: tuple[int, ...] = (60, 120, 252)
) -> pd.DataFrame:
    if equity_curve.empty or "equity" not in equity_curve.columns:
        return pd.DataFrame()

    df = pd.DataFrame(index=equity_curve.index)

    for window in windows:
        rolling_peak = (
            equity_curve["equity"].rolling(window=window, min_periods=1).max()
        )
        drawdown = (equity_curve["equity"] - rolling_peak) / rolling_peak.replace(
            0, np.nan
        )
        rolling_max_dd = drawdown.rolling(window=window, min_periods=1).min()
        df[f"rolling_max_drawdown_{window}"] = abs(rolling_max_dd).fillna(0)

    return df


def build_rolling_metrics_frame(
    equity_curve: pd.DataFrame, windows: tuple[int, ...] = (20, 60, 120, 252)
) -> tuple[pd.DataFrame, dict]:
    if equity_curve.empty:
        return pd.DataFrame(), {}

    returns_df = calculate_rolling_returns(equity_curve, windows)
    vol_df = calculate_rolling_volatility(equity_curve, windows)
    sharpe_df = calculate_rolling_sharpe(equity_curve, windows)
    dd_df = calculate_rolling_drawdown(equity_curve, windows)

    df = pd.concat([returns_df, vol_df, sharpe_df, dd_df], axis=1)

    summary = {
        f"latest_rolling_return_{w}": (
            float(returns_df[f"rolling_return_{w}"].iloc[-1])
            if pd.notna(returns_df[f"rolling_return_{w}"].iloc[-1])
            else None
        )
        for w in windows
    }

    return df, summary
