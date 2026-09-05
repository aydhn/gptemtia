from advanced_data_normalization.phase_114_handoff import (
    build_phase_114_lineage_provenance_handoff_report,
    summarize_phase_114_handoff,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_phase_114_handoff():
    prof = get_default_data_normalization_profile()
    df, summary = build_phase_114_lineage_provenance_handoff_report(prof)
    assert not df.empty
    assert summary["target_phase"] == 114
    assert summary["destructive_actions"] is False
    assert len(df) >= 10
