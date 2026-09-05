import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.provider_metadata_quality_rules import (
    build_provider_metadata_quality_rule_set,
    check_provider_metadata_quality,
)


def test_provider_metadata_quality_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_provider_metadata_quality_rule_set(profile)
    assert len(df_rules) >= 2

    # Credential leakage detection
    leaked_df = pd.DataFrame([{"provider_name": "test", "api_key": "secret_token_123"}])
    findings = check_provider_metadata_quality(leaked_df, "prov_test")
    assert any(f.severity_label == "quality_critical" for f in findings)
    assert any("credential/secret" in f.message for f in findings)
