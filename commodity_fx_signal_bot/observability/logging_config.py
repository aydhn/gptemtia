"""
Centralized logging configuration.
"""

import logging
import os
import re
from pathlib import Path
from typing import Dict, Any

from observability.observability_config import ObservabilityProfile


def mask_sensitive_values(text: str) -> str:
    """Mask sensitive values like tokens and chat IDs in text."""
    if not isinstance(text, str):
        return text

    # Mask typical Telegram bot tokens (digits:alphanumeric)
    text = re.sub(r'(\d{9,10}:[A-Za-z0-9_-]{35,})', '********', text)

    # Mask typical numeric chat IDs or user IDs (-digits or digits)
    text = re.sub(r'(chat_id=)(-\d+|\d+)', r'\1********', text)

    # Mask typical keys/secrets in URLs
    text = re.sub(r'(key|secret|token)=([^&\s]+)', r'\1=********', text)

    return text


class SensitiveFilter(logging.Filter):
    """Logging filter to mask sensitive values in log messages."""
    def filter(self, record: logging.LogRecord) -> bool:
        record.msg = mask_sensitive_values(str(record.msg))
        if hasattr(record, 'message'):
            record.message = mask_sensitive_values(str(record.message))
        if isinstance(record.args, dict):
            new_args = {}
            for k, v in record.args.items():
                if isinstance(v, str):
                    new_args[k] = mask_sensitive_values(v)
                else:
                    new_args[k] = v
            record.args = new_args
        elif isinstance(record.args, tuple):
            new_args = []
            for arg in record.args:
                if isinstance(arg, str):
                    new_args.append(mask_sensitive_values(arg))
                else:
                    new_args.append(arg)
            record.args = tuple(new_args)
        return True


def build_log_file_path(log_dir: Path, component: str = "system") -> Path:
    """Build a path for a log file, ensuring the directory exists."""
    log_dir.mkdir(parents=True, exist_ok=True)
    return log_dir / f"{component}.log"


def rotate_old_logs(log_dir: Path, max_log_files: int = 20) -> Dict[str, Any]:
    """Rotate log files, keeping only the most recent 'max_log_files' files."""
    if not log_dir.exists():
        return {"status": "skipped", "reason": "Directory does not exist"}

    # Example generic rotation logic that assumes file modification times
    files = [f for f in log_dir.glob("*.log") if f.is_file()]
    if len(files) <= max_log_files:
        return {"status": "skipped", "reason": "Log count below threshold", "count": len(files)}

    # Sort files by modification time, newest first
    files.sort(key=lambda x: x.stat().st_mtime, reverse=True)

    deleted_files = []
    # Delete oldest files
    for file_to_delete in files[max_log_files:]:
        try:
            file_to_delete.unlink()
            deleted_files.append(file_to_delete.name)
        except OSError as e:
            pass # Ignore deletion errors

    return {
        "status": "success",
        "deleted_count": len(deleted_files),
        "kept_count": max_log_files
    }


def configure_logging(profile: ObservabilityProfile, log_dir: Path) -> Dict[str, Any]:
    """Configure Python's root logger according to the observability profile."""
    # Create the sensitive filter
    sensitive_filter = SensitiveFilter()

    # Get root logger
    root_logger = logging.getLogger()

    # Set log level
    numeric_level = getattr(logging, profile.log_level.upper(), logging.INFO)
    root_logger.setLevel(numeric_level)

    # Remove existing handlers to avoid duplicates if called multiple times
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Define a standard format
    formatter = logging.Formatter(
        fmt='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    handlers_added = []

    # Add console handler
    if profile.log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(numeric_level)
        console_handler.setFormatter(formatter)
        console_handler.addFilter(sensitive_filter)
        root_logger.addHandler(console_handler)
        handlers_added.append("console")

    # Add file handler
    if profile.log_to_file:
        log_file = build_log_file_path(log_dir)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(numeric_level)
        file_handler.setFormatter(formatter)
        file_handler.addFilter(sensitive_filter)
        root_logger.addHandler(file_handler)
        handlers_added.append(f"file: {log_file.name}")

    return {
        "status": "configured",
        "log_level": profile.log_level,
        "handlers": handlers_added
    }


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance."""
    return logging.getLogger(name)
