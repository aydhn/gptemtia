import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.secret_exclusion_verification import build_secret_exclusion_verification_report

def test_secret_exclusion_verification():
    profile = get_default_local_archive_profile()
    exc_df = pd.DataFrame([{"pattern": ".env*"}])
    item_df = pd.DataFrame([
        {"item_id": "1", "item_status": "archive_candidate", "relative_path": ".env.test"}
    ])

    df, summary = build_secret_exclusion_verification_report(exc_df, item_df, profile)

    assert not df.empty
    assert df.iloc[0]["relative_path"] == ".env.test"
    assert df.iloc[0]["expected_status"] == "archive_excluded"
