import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.archive_quality import build_archive_quality_report, check_for_forbidden_terms_in_archive

def test_forbidden_terms():
    res1 = check_for_forbidden_terms_in_archive("We have cloud upload here")
    assert not res1["is_safe"]
    assert "cloud upload" in res1["forbidden_terms_found"]

    res2 = check_for_forbidden_terms_in_archive("This is NOT a cloud backup")
    assert res2["is_safe"]

def test_archive_quality_report():
    qual = build_archive_quality_report(
        summary={"text": "Hello"},
        domain_df=pd.DataFrame([{"1": 1}]),
        item_df=pd.DataFrame([{"1": 1}]),
        risk_df=pd.DataFrame()
    )

    assert qual["passed"] is True
    assert qual["no_cloud_upload_confirmed"] is True

    # Failing case
    qual_fail = build_archive_quality_report(
        summary={"text": "cloud upload done"},
    )

    assert qual_fail["passed"] is False
    assert "cloud upload" in qual_fail["forbidden_terms_found"]
