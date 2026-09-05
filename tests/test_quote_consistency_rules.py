import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.quote_consistency_rules import (
    build_quote_consistency_rule_contract,
    check_quote_consistency,
)


def test_quote_consistency_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_quote_consistency_rule_contract(profile)
    assert len(df_rules) >= 2

    # Inverted quote: bid > ask
    bad_quote = pd.DataFrame([
        {"timestamp": "2026-09-01", "bid": 1.10, "ask": 1.05, "spread": -0.05}
    ])
    findings = check_quote_consistency(bad_quote, "dataset_fx_quote", "test_p")
    assert any(f.field_name == "bid" for f in findings)
    assert any(f.field_name == "spread" for f in findings)
