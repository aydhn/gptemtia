
import pandas as pd
from local_closure.closure_validation import build_closure_validation_report, validate_closure_domains
from local_closure.closure_config import get_default_local_closure_profile

def test_val():
    p = get_default_local_closure_profile()
    assert validate_closure_domains(pd.DataFrame(), p)["valid"]
    df, summary = build_closure_validation_report({}, p)
    assert not df.empty
