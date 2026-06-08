
import pytest
import pandas as pd
from pathlib import Path
from secrets_hygiene.test_fixture_scanner import (
    scan_tests_for_secret_like_values,
    classify_test_secret_finding,
    audit_test_fixtures_for_dummy_values
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_scan_tests_for_secret_like():
    profile = get_default_secrets_hygiene_profile()
    df, s = scan_tests_for_secret_like_values(Path("."), profile)
    assert df.empty

def test_classify_test_secret_finding():
    c = classify_test_secret_finding(pd.Series({"raw_value": "dummy_key"}))
    assert c["status"] == "low_secret_warning"

    c2 = classify_test_secret_finding(pd.Series({"raw_value": "AKIAIOSFODNN7EXAMPLE"}))
    assert c2["status"] == "high_secret_risk"
