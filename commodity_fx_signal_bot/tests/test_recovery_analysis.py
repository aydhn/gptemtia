import pytest
import pandas as pd
from portfolio_regime.recovery_analysis import (
    calculate_recovery_time_from_drawdown,
    calculate_recovery_statistics,
    build_recovery_time_table
)

def test_recovery_analysis():
    idx = pd.date_range("2023-01-01", periods=4)
    curve = pd.Series([100, 90, 80, 110], index=idx)

    rec_time = calculate_recovery_time_from_drawdown(curve, idx[0], idx[2])
    assert rec_time == 2 # bars from trough to recovery

    df = pd.DataFrame({"cluster_id": ["1"], "recovery_bars": [10]})
    stats = calculate_recovery_statistics(df)
    assert stats["avg_recovery_bars"] == 10

    table = build_recovery_time_table(df)
    assert not table.empty
