import logging
from pathlib import Path
import pytest

from observability.observability_config import ObservabilityProfile
from observability.logging_config import mask_sensitive_values, configure_logging, build_log_file_path, rotate_old_logs


def test_mask_sensitive_values():
    assert mask_sensitive_values("chat_id=1234567") == "chat_id=********"
    assert mask_sensitive_values("token=abc_123") == "token=********"
    assert mask_sensitive_values("123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789") == "********"
    assert mask_sensitive_values("Normal text message") == "Normal text message"
    assert mask_sensitive_values(None) is None


def test_build_log_file_path(tmp_path):
    log_dir = tmp_path / "logs"
    file_path = build_log_file_path(log_dir, "test_comp")

    assert log_dir.exists()
    assert file_path.name == "test_comp.log"


def test_rotate_old_logs(tmp_path):
    log_dir = tmp_path / "logs"
    log_dir.mkdir()

    # Create 5 files
    for i in range(5):
        f = log_dir / f"test_{i}.log"
        f.touch()

    result = rotate_old_logs(log_dir, max_log_files=3)
    assert result["status"] == "success"
    assert result["deleted_count"] == 2
    assert result["kept_count"] == 3

    files = list(log_dir.glob("*.log"))
    assert len(files) == 3


def test_configure_logging(tmp_path):
    profile = ObservabilityProfile(
        name="test",
        description="test",
        log_level="DEBUG",
        log_to_console=True,
        log_to_file=True,
        max_log_files=10
    )

    log_dir = tmp_path / "logs"
    result = configure_logging(profile, log_dir)

    assert result["status"] == "configured"
    assert result["log_level"] == "DEBUG"
    assert len(result["handlers"]) == 2

    # Check root logger
    root = logging.getLogger()
    assert root.level == logging.DEBUG
    # Cleanup to not mess with other tests
    for handler in root.handlers[:]:
        root.removeHandler(handler)
