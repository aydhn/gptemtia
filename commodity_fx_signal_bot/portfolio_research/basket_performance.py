import pandas as pd
import numpy as np
from portfolio_research.portfolio_models import VirtualBasketDefinition, VirtualBasketPerformance
from portfolio_research.diversification import calculate_diversification_score
from portfolio_research.concentration_risk import calculate_hhi_concentration

def calculate_virtual_basket_returns(returns_df: pd.DataFrame, basket: VirtualBasketDefinition) -> pd.Series:
    if returns_df.empty or not basket.weights:
        return pd.Series(dtype=float)

    valid_symbols = [s for s in basket.symbols if s in returns_df.columns]
    if not valid_symbols:
        return pd.Series(dtype=float)

    w = {s: basket.weights[s] for s in valid_symbols}
    total_w = sum(w.values())
    if total_w == 0:
        return pd.Series(dtype=float)

    w = {s: wt/total_w for s, wt in w.items()}

    port_returns = pd.Series(0.0, index=returns_df.index)
    for sym in valid_symbols:
        port_returns += returns_df[sym] * w[sym]

    return port_returns

def calculate_virtual_basket_equity_curve(basket_returns: pd.Series, initial_value: float = 100.0) -> pd.DataFrame:
    if basket_returns.empty:
        return pd.DataFrame()

    cum_returns = np.exp(basket_returns.cumsum())
    equity = initial_value * cum_returns

    df = pd.DataFrame({
        "returns": basket_returns,
        "equity": equity
    })

    df["peak"] = df["equity"].cummax()
    df["drawdown_pct"] = (df["equity"] - df["peak"]) / df["peak"]

    return df

def calculate_virtual_basket_performance(basket: VirtualBasketDefinition, returns_df: pd.DataFrame, corr_df: pd.DataFrame | None = None) -> VirtualBasketPerformance:
    basket_returns = calculate_virtual_basket_returns(returns_df, basket)

    if basket_returns.empty:
        return VirtualBasketPerformance(
            basket_id=basket.basket_id,
            timeframe=basket.timeframe,
            start_date=None, end_date=None, observation_count=0,
            total_return_pct=None, annualized_return_pct=None, annualized_volatility_pct=None,
            max_drawdown_pct=None, sharpe_like_score=None, diversification_score=None, concentration_score=None,
            warnings=["No return data available for basket symbols."]
        )

    equity_df = calculate_virtual_basket_equity_curve(basket_returns)

    obs_count = len(basket_returns)
    start_date = basket_returns.index[0].isoformat() if hasattr(basket_returns.index[0], 'isoformat') else str(basket_returns.index[0])
    end_date = basket_returns.index[-1].isoformat() if hasattr(basket_returns.index[-1], 'isoformat') else str(basket_returns.index[-1])

    total_ret = (np.exp(basket_returns.sum()) - 1.0) * 100 if basket_returns.sum() != 0 else 0.0

    ann_factor = 252
    ann_ret = (np.exp(basket_returns.mean() * ann_factor) - 1.0) * 100
    ann_vol = basket_returns.std() * np.sqrt(ann_factor) * 100

    max_dd = equity_df["drawdown_pct"].min() * 100 if not equity_df.empty else 0.0

    sharpe = (ann_ret / ann_vol) if ann_vol > 0 else 0.0

    div_score = 0.0
    if corr_df is not None and not corr_df.empty:
        valid_symbols = [s for s in basket.symbols if s in corr_df.columns]
        if len(valid_symbols) >= 2:
            sub_corr = corr_df.loc[valid_symbols, valid_symbols]
            div_score = calculate_diversification_score(sub_corr)

    conc_score = calculate_hhi_concentration(basket.weights)

    return VirtualBasketPerformance(
        basket_id=basket.basket_id,
        timeframe=basket.timeframe,
        start_date=start_date,
        end_date=end_date,
        observation_count=obs_count,
        total_return_pct=total_ret,
        annualized_return_pct=ann_ret,
        annualized_volatility_pct=ann_vol,
        max_drawdown_pct=max_dd,
        sharpe_like_score=sharpe,
        diversification_score=div_score,
        concentration_score=conc_score,
        warnings=["Basket performance geçmiş/sanal analizdir. Sharpe-like score yatırım tavsiyesi değildir."]
    )

def build_basket_performance_table(baskets: list[VirtualBasketDefinition], returns_df: pd.DataFrame, corr_df: pd.DataFrame | None = None) -> pd.DataFrame:
    rows = []
    for basket in baskets:
        perf = calculate_virtual_basket_performance(basket, returns_df, corr_df)
        rows.append({
            "basket_id": perf.basket_id,
            "basket_type": basket.basket_type,
            "total_return_pct": perf.total_return_pct,
            "annualized_return_pct": perf.annualized_return_pct,
            "annualized_volatility_pct": perf.annualized_volatility_pct,
            "max_drawdown_pct": perf.max_drawdown_pct,
            "sharpe_like_score": perf.sharpe_like_score,
            "diversification_score": perf.diversification_score,
            "concentration_score": perf.concentration_score
        })

    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows)

def build_basket_equity_curves(baskets: list[VirtualBasketDefinition], returns_df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    curves = {}
    for basket in baskets:
        ret = calculate_virtual_basket_returns(returns_df, basket)
        if not ret.empty:
            curves[basket.basket_id] = calculate_virtual_basket_equity_curve(ret)
    return curves
