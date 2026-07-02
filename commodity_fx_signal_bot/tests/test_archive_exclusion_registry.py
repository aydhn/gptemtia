import pytest
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.archive_exclusion_registry import build_default_archive_exclusions

def test_default_exclusions():
    profile = get_default_local_archive_profile()
    df = build_default_archive_exclusions(profile)

    assert not df.empty
    patterns = df["pattern"].tolist()
    assert ".env*" in patterns
    assert "*.key" in patterns
    assert "__pycache__/*" in patterns
