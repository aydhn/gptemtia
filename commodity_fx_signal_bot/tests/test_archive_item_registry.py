import pytest
from pathlib import Path
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.archive_item_registry import classify_archive_domain_from_path, classify_archive_item_status

def test_classify_domain():
    root = Path("/app")
    p1 = Path("/app/docs/README.md")
    assert classify_archive_domain_from_path(p1, root) == "documentation_archive"

    p2 = Path("/app/config/settings.py")
    assert classify_archive_domain_from_path(p2, root) == "config_archive"

def test_classify_status():
    root = Path("/app")
    profile = get_default_local_archive_profile()

    p1 = Path("/app/.env")
    assert classify_archive_item_status(p1, root, profile) == "archive_excluded"

    p2 = Path("/app/secret.json")
    assert classify_archive_item_status(p2, root, profile) == "archive_excluded"

    p3 = Path("/app/main.py")
    assert classify_archive_item_status(p3, root, profile) == "archive_candidate"
