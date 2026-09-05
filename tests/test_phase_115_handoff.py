from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.phase_115_handoff import (
    build_phase_115_provider_benchmark_handoff_report,
    summarize_phase_115_handoff,
)


def test_phase_115_handoff():
    profile = get_default_data_lineage_profile()
    df, summary = build_phase_115_provider_benchmark_handoff_report(profile)
    assert len(df) >= 8
    assert summary["target_phase"] == 115
    assert summary["target_final_phase"] == 160
    assert summary["current_phase"] == 114
