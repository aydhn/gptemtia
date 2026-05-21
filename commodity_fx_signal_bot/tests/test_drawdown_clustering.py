import pytest
import pandas as pd
from portfolio_regime.regime_config import PortfolioRegimeProfile
from portfolio_regime.drawdown_clustering import (
    calculate_drawdown_series,
    identify_drawdown_clusters,
    classify_drawdown_cluster,
    drawdown_clusters_to_dataframe
)

def test_drawdown_clustering():
    profile = PortfolioRegimeProfile(name="test", description="")
    curve = pd.Series([100, 90, 80, 110], index=pd.date_range("2023-01-01", periods=4))

    dd = calculate_drawdown_series(curve)
    assert dd.iloc[2] == -0.2

    clusters = identify_drawdown_clusters(dd, "b1", profile)
    assert len(clusters) > 0

    assert classify_drawdown_cluster(-0.2, 10, None) == "deep_drawdown_cluster"

    df = drawdown_clusters_to_dataframe(clusters)
    assert not df.empty
