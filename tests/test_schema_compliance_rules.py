import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.schema_compliance_rules import (
    build_schema_compliance_rule_set,
    check_schema_compliance,
    summarize_schema_compliance_rules,
)


def test_schema_compliance_rules():
    profile = get_default_data_quality_profile()
    df_rules, sum_rules = build_schema_compliance_rule_set(profile)
    assert len(df_rules) >= 2

    # Check missing required field detection
    test_df = pd.DataFrame([{"pair": "USD/TRY", "bid": 34.0}])
    required = ["pair", "bid", "ask", "timestamp"]
    findings = check_schema_compliance(test_df, required, "dataset_fx_quote", "test_prov")
    assert len(findings) == 2  # ask and timestamp missing
    assert any(f.field_name == "ask" for f in findings)
    assert any(f.field_name == "timestamp" for f in findings)
    assert findings[0].severity_label == "quality_critical"
