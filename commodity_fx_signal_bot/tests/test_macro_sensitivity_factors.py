import pandas as pd
from factor_research.macro_sensitivity_factors import calculate_rolling_beta_proxy

def test_macro_sensitivity():
    s1 = pd.Series([0.01]*60)
    s2 = pd.Series([0.02]*60)
    beta = calculate_rolling_beta_proxy(s1, s2, 60)
    # Variance of constant is 0
    assert beta is None or pd.isna(beta) or beta == 0.0 or beta == 0.5
