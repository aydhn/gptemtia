"""
Tests for path definitions and directory creation.
"""

from config.paths import (
    CACHE_DIR,
    LOGS_DIR,
    PROCESSED_DATA_DIR,
    RAW_DATA_DIR,
    REPORTS_DIR,
    ensure_project_directories,
)


def test_ensure_project_directories():
    """Ensure that the function creates directories without errors."""
    # Run the function
    ensure_project_directories()

    # Assert directories exist
    assert LOGS_DIR.exists()
    assert LOGS_DIR.is_dir()

    assert REPORTS_DIR.exists()
    assert REPORTS_DIR.is_dir()

    assert RAW_DATA_DIR.exists()
    assert RAW_DATA_DIR.is_dir()

    assert PROCESSED_DATA_DIR.exists()
    assert PROCESSED_DATA_DIR.is_dir()

    assert CACHE_DIR.exists()
    assert CACHE_DIR.is_dir()
