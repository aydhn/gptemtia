from advanced_data_normalization.session_alignment_requirements import (
    build_session_alignment_requirement_registry,
    summarize_session_alignment_requirements,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_session_alignment_requirements():
    prof = get_default_data_normalization_profile()
    df, summary = build_session_alignment_requirement_registry(prof)
    assert not df.empty
    assert summary["total_requirements"] >= 5
