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

# Data Lake directories
LAKE_DIR = DATA_DIR / "lake"
LAKE_OHLCV_DIR = LAKE_DIR / "ohlcv"
LAKE_MACRO_DIR = LAKE_DIR / "macro"
LAKE_SYNTHETIC_DIR = LAKE_DIR / "synthetic"
LAKE_MANIFESTS_DIR = LAKE_DIR / "manifests"
LAKE_JOURNALS_DIR = LAKE_DIR / "journals"

# Processed Lake Directories
LAKE_PROCESSED_DIR = LAKE_DIR / "processed"
LAKE_PROCESSED_OHLCV_DIR = LAKE_PROCESSED_DIR / "ohlcv"
LAKE_QUALITY_REPORTS_DIR = LAKE_PROCESSED_DIR / "quality_reports"
LAKE_CLEANING_REPORTS_DIR = LAKE_PROCESSED_DIR / "cleaning_reports"

LAKE_TMP_DIR = LAKE_DIR / "tmp"


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
        CACHE_DIR,
        LAKE_DIR,
        LAKE_OHLCV_DIR,
        LAKE_MACRO_DIR,
        LAKE_SYNTHETIC_DIR,
        LAKE_MANIFESTS_DIR,
        LAKE_JOURNALS_DIR,
        LAKE_PROCESSED_DIR,
        LAKE_PROCESSED_OHLCV_DIR,
        LAKE_QUALITY_REPORTS_DIR,
        LAKE_CLEANING_REPORTS_DIR,
        LAKE_TMP_DIR,
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
