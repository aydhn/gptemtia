import pytest
import pandas as pd
from portfolio_regime.regime_correlation import (
    calculate_correlation_by_regime,
    calculate_average_correlation_by_regime,
    identify_regime_correlation_spikes
)

def test_correlation_by_regime():
    import numpy as np
    ret_df = pd.DataFrame({"A": np.random.normal(0, 0.01, 15), "B": np.random.normal(0, 0.01, 15)}, index=range(15))
    reg_df = pd.DataFrame({"regime_label": ["risk_on_regime"]*15}, index=range(15))

    corrs = calculate_correlation_by_regime(ret_df, reg_df)
    assert "risk_on_regime" in corrs

    avg = calculate_average_correlation_by_regime(corrs)
    assert not avg.empty

    spikes = identify_regime_correlation_spikes(avg, threshold=0.0)
    pass
