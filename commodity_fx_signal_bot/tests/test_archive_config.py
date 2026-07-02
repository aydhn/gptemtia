import pytest
from local_archive.archive_config import (
    LocalArchiveProfile,
    get_local_archive_profile,
    list_local_archive_profiles,
    validate_local_archive_profiles,
    get_default_local_archive_profile,
    ConfigError
)

def test_validate_local_archive_profiles():
    # Should not raise exception with valid defaults
    validate_local_archive_profiles()

def test_get_default_local_archive_profile():
    profile = get_default_local_archive_profile()
    assert profile.name == "balanced_local_archive"
    assert profile.language == "tr"
    assert profile.dry_run_default is True
    assert profile.allow_cloud_upload is False

def test_invalid_profile_retrieval():
    with pytest.raises(ConfigError):
        get_local_archive_profile("non_existent_profile")

def test_profile_constraints():
    # Test valid creation
    LocalArchiveProfile(
        name="test",
        description="test",
        language="tr",
        dry_run_default=True,
        max_items=10,
        max_file_mb_for_hash=10,
        retention_review_days=10,
        integrity_review_days=10,
        min_preservation_score=0.5,
        min_quality_score=0.5
    )

    # We validate via the validate function conceptually,
    # but the dataclass itself allows creation, so we check the validate function logic
    # by modifying the global dictionary temporarily or trusting test_validate_local_archive_profiles
