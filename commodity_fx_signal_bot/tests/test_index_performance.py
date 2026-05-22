import pandas as pd
from synthetic_indices.index_performance import (
    calculate_index_drawdown,
    calculate_index_volatility,
    calculate_index_performance
)
from synthetic_indices.index_models import SyntheticIndexSeries

def test_index_performance():
    dates = pd.date_range("2023-01-01", periods=10)
    levels = pd.Series([100, 105, 110, 108, 112, 115, 113, 118, 120, 125], index=dates)
    returns = levels.pct_change().dropna()

    series = SyntheticIndexSeries(
        index_id="test_idx",
        timeframe="1d",
        level_series=levels,
        return_series=returns,
        start_date=None,
        end_date=None,
        observation_count=10,
        warnings=[]
    )

    perf = calculate_index_performance(series)
    assert perf["total_return_pct"] == 25.0
    assert perf["max_drawdown_pct"] < 0 # Went from 110 to 108, 115 to 113
    assert perf["annualized_volatility_pct"] > 0

    dd = calculate_index_drawdown(levels)
    assert not dd.empty

    vol = calculate_index_volatility(returns)
    assert vol > 0
