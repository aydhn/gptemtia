
import pytest
import pandas as pd
from secrets_hygiene.secrets_safety import (
    scan_secret_outputs_for_raw_values,
    validate_no_secret_value_output,
    validate_no_file_modification_actions,
    validate_no_forbidden_secret_workflows,
    build_secrets_safety_report
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_scan_secret_outputs_for_raw_values():
    df = pd.DataFrame([{"masked_value": "****"}])
    res = scan_secret_outputs_for_raw_values(df)
    assert res["status"] == "passed"

    df2 = pd.DataFrame([{"raw_value": "secret"}])
    res2 = scan_secret_outputs_for_raw_values(df2)
    assert res2["status"] == "failed"

def test_validate_no_file_modification():
    profile = get_default_secrets_hygiene_profile()
    df = pd.DataFrame([{"destructive": False}])
    res = validate_no_file_modification_actions(df, profile)
    assert res["status"] == "passed"

def test_validate_no_forbidden():
    res = validate_no_forbidden_secret_workflows(text="This will delete secret file")
    assert res["status"] == "failed"

    res2 = validate_no_forbidden_secret_workflows(text="This is a safe report")
    assert res2["status"] == "passed"

def test_build_safety_report():
    profile = get_default_secrets_hygiene_profile()
    df, s = build_secrets_safety_report({}, profile)
    assert not df.empty
