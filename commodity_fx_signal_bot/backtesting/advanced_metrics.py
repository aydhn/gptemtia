import pandas as pd
import numpy as np


def calculate_total_return(equity_curve: pd.DataFrame) -> float:
    if equity_curve.empty or "equity" not in equity_curve.columns:
        return 0.0
    initial = equity_curve["equity"].iloc[0]
    final = equity_curve["equity"].iloc[-1]
    if initial <= 0:
        return 0.0
    return (final - initial) / initial


def calculate_cagr(
    equity_curve: pd.DataFrame, trading_days_per_year: int = 252
) -> float:
    if (
        equity_curve.empty
        or "equity" not in equity_curve.columns
        or len(equity_curve) < 2
    ):
        return np.nan
    total_return = calculate_total_return(equity_curve)
    periods = len(equity_curve)
    years = periods / trading_days_per_year
    if years <= 0:
        return np.nan
    val = max(0, total_return + 1.0)
    return (val ** (1.0 / years)) - 1.0


def calculate_annualized_return(
    equity_curve: pd.DataFrame, trading_days_per_year: int = 252
) -> float:
    return calculate_cagr(equity_curve, trading_days_per_year)


def calculate_annualized_volatility(
    equity_curve: pd.DataFrame, trading_days_per_year: int = 252
) -> float:
    if (
        equity_curve.empty
        or "equity" not in equity_curve.columns
        or len(equity_curve) < 2
    ):
        return np.nan
    returns = equity_curve["equity"].pct_change().dropna()
    if len(returns) == 0:
        return 0.0
    daily_vol = returns.std()
    return daily_vol * np.sqrt(trading_days_per_year)


def calculate_sharpe_ratio(
    equity_curve: pd.DataFrame,
    risk_free_rate_annual: float = 0.0,
    trading_days_per_year: int = 252,
) -> float:
    if (
        equity_curve.empty
        or "equity" not in equity_curve.columns
        or len(equity_curve) < 2
    ):
        return np.nan
    returns = equity_curve["equity"].pct_change().dropna()
    if len(returns) == 0:
        return np.nan

    daily_rf = (1 + risk_free_rate_annual) ** (1 / trading_days_per_year) - 1
    excess_returns = returns - daily_rf

    std = excess_returns.std()
    if std == 0 or np.isnan(std):
        return 0.0

    return np.sqrt(trading_days_per_year) * (excess_returns.mean() / std)


def calculate_sortino_ratio(
    equity_curve: pd.DataFrame,
    risk_free_rate_annual: float = 0.0,
    trading_days_per_year: int = 252,
) -> float:
    if (
        equity_curve.empty
        or "equity" not in equity_curve.columns
        or len(equity_curve) < 2
    ):
        return np.nan
    returns = equity_curve["equity"].pct_change().dropna()
    if len(returns) == 0:
        return np.nan

    daily_rf = (1 + risk_free_rate_annual) ** (1 / trading_days_per_year) - 1
    excess_returns = returns - daily_rf

    downside_returns = excess_returns[excess_returns < 0]
    if len(downside_returns) == 0:
        return np.inf if excess_returns.mean() > 0 else 0.0

    downside_std = downside_returns.std()
    if downside_std == 0 or np.isnan(downside_std):
        return 0.0

    return np.sqrt(trading_days_per_year) * (excess_returns.mean() / downside_std)


def calculate_calmar_ratio(equity_curve: pd.DataFrame) -> float:
    if equity_curve.empty or "equity" not in equity_curve.columns:
        return np.nan

    cagr = calculate_cagr(equity_curve)
    if np.isnan(cagr):
        return np.nan

    rolling_max = equity_curve["equity"].cummax()
    drawdown = (equity_curve["equity"] - rolling_max) / rolling_max
    max_dd = abs(drawdown.min())

    if max_dd == 0:
        return np.inf if cagr > 0 else 0.0

    return cagr / max_dd


def calculate_profit_factor(trades_df: pd.DataFrame) -> float:
    if trades_df.empty or "net_pnl" not in trades_df.columns:
        return np.nan

    gross_profit = trades_df[trades_df["net_pnl"] > 0]["net_pnl"].sum()
    gross_loss = abs(trades_df[trades_df["net_pnl"] < 0]["net_pnl"].sum())

    if gross_loss == 0:
        return np.inf if gross_profit > 0 else 0.0

    return float(gross_profit / gross_loss)


def calculate_expectancy(trades_df: pd.DataFrame) -> float:
    if trades_df.empty or "net_pnl" not in trades_df.columns:
        return np.nan

    wins = trades_df[trades_df["net_pnl"] > 0]
    losses = trades_df[trades_df["net_pnl"] < 0]

    win_rate = len(wins) / len(trades_df)
    loss_rate = len(losses) / len(trades_df)

    avg_win = wins["net_pnl"].mean() if not wins.empty else 0.0
    avg_loss = abs(losses["net_pnl"].mean()) if not losses.empty else 0.0

    return (win_rate * avg_win) - (loss_rate * avg_loss)


def calculate_payoff_ratio(trades_df: pd.DataFrame) -> float:
    if trades_df.empty or "net_pnl" not in trades_df.columns:
        return np.nan

    wins = trades_df[trades_df["net_pnl"] > 0]
    losses = trades_df[trades_df["net_pnl"] < 0]

    avg_win = wins["net_pnl"].mean() if not wins.empty else 0.0
    avg_loss = abs(losses["net_pnl"].mean()) if not losses.empty else 0.0

    if avg_loss == 0:
        return np.inf if avg_win > 0 else 0.0

    return float(avg_win / avg_loss)


def calculate_recovery_factor(equity_curve: pd.DataFrame) -> float:
    if equity_curve.empty or "equity" not in equity_curve.columns:
        return np.nan

    total_net_profit = equity_curve["equity"].iloc[-1] - equity_curve["equity"].iloc[0]

    rolling_max = equity_curve["equity"].cummax()
    drawdown = rolling_max - equity_curve["equity"]
    max_dd_amount = drawdown.max()

    if max_dd_amount == 0:
        return np.inf if total_net_profit > 0 else 0.0

    return float(total_net_profit / max_dd_amount)


def calculate_exposure_time_proxy(
    trades_df: pd.DataFrame, price_df: pd.DataFrame | None = None
) -> float:
    if trades_df.empty or "holding_bars" not in trades_df.columns:
        return 0.0

    total_bars_in_market = trades_df["holding_bars"].sum()
    if price_df is not None and not price_df.empty:
        total_bars = len(price_df)
    else:
        total_bars = total_bars_in_market

    if total_bars == 0:
        return 0.0

    return min(1.0, float(total_bars_in_market / total_bars))


def build_advanced_performance_metrics(
    trades_df: pd.DataFrame, equity_curve: pd.DataFrame, initial_equity: float
) -> dict:
    if equity_curve.empty:
        return {}

    metrics = {}

    metrics["total_return_pct"] = calculate_total_return(equity_curve)
    metrics["cagr"] = calculate_cagr(equity_curve)
    metrics["annualized_return"] = calculate_annualized_return(equity_curve)
    metrics["annualized_volatility"] = calculate_annualized_volatility(equity_curve)
    metrics["sharpe_ratio"] = calculate_sharpe_ratio(equity_curve)
    metrics["sortino_ratio"] = calculate_sortino_ratio(equity_curve)
    metrics["calmar_ratio"] = calculate_calmar_ratio(equity_curve)

    rolling_max = equity_curve["equity"].cummax()
    drawdown = (equity_curve["equity"] - rolling_max) / rolling_max
    metrics["max_drawdown_pct"] = (
        float(abs(drawdown.min())) if not drawdown.empty else 0.0
    )

    metrics["profit_factor"] = calculate_profit_factor(trades_df)
    metrics["expectancy"] = calculate_expectancy(trades_df)
    metrics["payoff_ratio"] = calculate_payoff_ratio(trades_df)
    metrics["recovery_factor"] = calculate_recovery_factor(equity_curve)

    metrics["trade_count"] = len(trades_df)

    if not trades_df.empty and "net_pnl" in trades_df.columns:
        wins = trades_df[trades_df["net_pnl"] > 0]
        losses = trades_df[trades_df["net_pnl"] < 0]

        metrics["win_rate"] = len(wins) / len(trades_df)
        metrics["avg_win"] = float(wins["net_pnl"].mean()) if not wins.empty else 0.0
        metrics["avg_loss"] = (
            float(losses["net_pnl"].mean()) if not losses.empty else 0.0
        )
        metrics["avg_trade_return"] = (
            float(trades_df["return_pct"].mean())
            if "return_pct" in trades_df.columns
            else 0.0
        )
        metrics["median_trade_return"] = (
            float(trades_df["return_pct"].median())
            if "return_pct" in trades_df.columns
            else 0.0
        )
    else:
        metrics["win_rate"] = 0.0
        metrics["avg_win"] = 0.0
        metrics["avg_loss"] = 0.0
        metrics["avg_trade_return"] = 0.0
        metrics["median_trade_return"] = 0.0

    metrics["exposure_time_proxy"] = calculate_exposure_time_proxy(
        trades_df, equity_curve
    )

    for k, v in metrics.items():
        if isinstance(v, float) and (np.isnan(v) or np.isinf(v)):
            metrics[k] = None

    return metrics
