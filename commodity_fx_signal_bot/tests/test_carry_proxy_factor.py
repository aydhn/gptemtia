import pandas as pd
from factor_research.carry_proxy_factor import calculate_fx_try_carry_proxy

def test_carry_proxy():
    metadata = pd.DataFrame({"symbol": ["USDTRY=X", "EURUSD=X"]})
    s = calculate_fx_try_carry_proxy(metadata)
    assert s.loc["USDTRY=X"] == 1.0
    assert s.loc["EURUSD=X"] == 0.0
