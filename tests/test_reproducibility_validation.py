"""Test validation."""
import pandas as pd
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_validation import build_reproducibility_validation_report, validate_reproducibility_domains
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_validation():
    p = get_default_local_reproducibility_governance_profile()
    df, s = build_reproducibility_validation_report({}, p)
    assert not df.empty
    assert validate_reproducibility_domains(pd.DataFrame(), p)["valid"]
