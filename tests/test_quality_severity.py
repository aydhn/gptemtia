import pytest
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.quality_severity import (
    build_quality_severity_registry,
    summarize_quality_severity,
)


def test_quality_severity():
    profile = get_default_data_quality_profile()
    df, summary = build_quality_severity_registry(profile)
    assert len(df) == 5
    assert "quality_critical" in summary["severity_labels"]
    assert "quality_high" in summary["severity_labels"]
    assert "quality_medium" in summary["severity_labels"]
    assert "quality_low" in summary["severity_labels"]
    assert "quality_info" in summary["severity_labels"]
    assert summary["max_penalty"] > 0.3
