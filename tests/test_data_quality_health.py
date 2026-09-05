import pytest
from pathlib import Path
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.data_quality_health import (
    build_data_quality_health_check,
    build_default_data_quality_health_findings,
    summarize_data_quality_health,
)


def test_data_quality_health(tmp_path):
    profile = get_default_data_quality_profile()
    df = build_default_data_quality_health_findings(profile)
    assert len(df) >= 30
    assert bool(df["passed"].all())

    _, summary = build_data_quality_health_check(tmp_path, profile)
    assert summary["failing_checks"] == 0
    assert summary["passing_checks"] >= 30
