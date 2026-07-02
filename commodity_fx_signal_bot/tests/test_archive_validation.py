import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.archive_validation import build_archive_validation_report

def test_archive_validation():
    profile = get_default_local_archive_profile()

    tables = {
        "domain_df": pd.DataFrame([{"domain_id": "1"}]),
        "item_df": pd.DataFrame([{"item_id": "1"}])
    }

    df, summary = build_archive_validation_report(tables, profile)

    assert not df.empty
    assert summary["is_valid"] is True

    # Test failure
    tables_fail = {
        "domain_df": pd.DataFrame([{"not_id": "1"}]),
    }
    df_fail, sum_fail = build_archive_validation_report(tables_fail, profile)

    assert sum_fail["is_valid"] is False
    assert sum_fail["failed_checks"] > 0
