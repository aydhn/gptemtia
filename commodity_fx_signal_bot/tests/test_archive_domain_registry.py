import pytest
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.archive_domain_registry import build_archive_domain_registry

def test_archive_domain_registry():
    profile = get_default_local_archive_profile()
    df, summary = build_archive_domain_registry(profile)

    assert not df.empty
    assert "domain_id" in df.columns
    assert "domain_label" in df.columns

    # Check security domain warning
    sec = df[df["domain_label"] == "security_archive"]
    if not sec.empty:
        assert len(sec.iloc[0]["warnings"]) > 0
