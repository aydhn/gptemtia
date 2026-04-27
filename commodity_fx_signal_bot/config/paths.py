"""
Path definitions and directory management for the project.
"""
import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.resolve()

# Base directories
DATA_DIR = PROJECT_ROOT / "data"
LOGS_DIR = PROJECT_ROOT / "logs"
REPORTS_DIR = PROJECT_ROOT / "reports" / "output"

# Specific data directories
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
CACHE_DIR = DATA_DIR / "cache"

def ensure_project_directories() -> None:
    """
    Ensure that all required project directories exist.
    Creates them if they do not exist.
    """
    directories = [
        LOGS_DIR,
        REPORTS_DIR,
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        CACHE_DIR
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
