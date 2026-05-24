import pandas as pd

from governance.governance_quality import (
    check_for_forbidden_trade_terms_in_governance,
    check_for_sensitive_data_in_governance,
)


def test_sensitive_data():
    df = pd.DataFrame([{"path": "data/secret_key.txt"}])
    res = check_for_sensitive_data_in_governance(df)
    assert res["sensitive_data_found"]

def test_forbidden_terms():
    res = check_for_forbidden_trade_terms_in_governance(text="This report gives a BUY signal")
    assert res["forbidden_trade_terms_found"]
