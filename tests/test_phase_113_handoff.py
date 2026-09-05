import pytest
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.phase_113_handoff import (
    build_phase_113_normalization_handoff_report,
    summarize_phase_113_handoff,
)


def test_phase_113_handoff():
    profile = get_default_data_quality_profile()
    df, summary = build_phase_113_normalization_handoff_report(profile)
    assert len(df) >= 10
    assert summary["target_phase"] == 113
    assert "FX symbol normalization enforcement" in summary["areas"]
    assert "Commodity symbol normalization enforcement" in summary["areas"]
    assert "News topic/tag normalization" in summary["areas"]
