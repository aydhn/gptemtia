
import pytest
from pathlib import Path
from secrets_hygiene.leakage_scanner import (
    scan_reports_for_secret_leakage,
    scan_data_lake_for_secret_leakage,
    scan_generated_docs_for_secret_leakage
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_reports_leakage_scan():
    profile = get_default_secrets_hygiene_profile()
    df, s = scan_reports_for_secret_leakage(Path("."), profile)
    assert df.empty

def test_data_lake_leakage_scan():
    profile = get_default_secrets_hygiene_profile()
    df, s = scan_data_lake_for_secret_leakage(Path("."), profile)
    assert df.empty

def test_generated_docs_leakage_scan():
    profile = get_default_secrets_hygiene_profile()
    df, s = scan_generated_docs_for_secret_leakage(Path("."), profile)
    assert df.empty
