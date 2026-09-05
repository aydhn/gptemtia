from pathlib import Path
import pytest
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.factor_metadata_health import (
    build_factor_metadata_health_check,
    summarize_factor_metadata_health,
)


def test_build_factor_metadata_health_check():
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_factor_metadata_profile()

    df, summary = build_factor_metadata_health_check(project_root, profile)
    assert not df.empty
    assert summary["total_checks"] >= 8
    assert summary["health_status"] == "HEALTHY"
    assert summary["prerequisites_ready"] is True
    assert summary["non_signal"] is True

    stats = summarize_factor_metadata_health(df)
    assert stats["is_healthy"] is True
    assert stats["failed_checks"] == 0
