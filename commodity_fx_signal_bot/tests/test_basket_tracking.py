import pandas as pd
from portfolio_research.basket_tracking import (
    build_basket_tracking_table,
    summarize_basket_tracking
)

def test_basket_tracking():
    curr = pd.DataFrame({
        "basket_id": ["b1", "b2"],
        "total_return_pct": [10, 5],
        "max_drawdown_pct": [-5, -10],
        "annualized_volatility_pct": [15, 20],
        "diversification_score": [0.8, 0.5]
    })

    prev = pd.DataFrame({
        "basket_id": ["b1", "b3"],
        "total_return_pct": [8, 5],
        "max_drawdown_pct": [-6, -10],
        "annualized_volatility_pct": [15, 20],
        "diversification_score": [0.7, 0.5]
    })

    track = build_basket_tracking_table(curr, prev)
    assert not track.empty

    summary = summarize_basket_tracking(track)
    assert summary["tracked_baskets"] == 2
