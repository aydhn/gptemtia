import pandas as pd
from advanced_regime_featurestore_integration.phase_135_handoff import (
    build_phase_135_regime_classification_acceptance_handoff_report,
    summarize_phase_135_handoff,
    CANONICAL_HANDOFF_PREREQUISITES,
)


def test_build_phase_135_handoff():
    df, summary = build_phase_135_regime_classification_acceptance_handoff_report()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 14
    assert summary["all_satisfied"] is True
    assert summary["handoff_status"] == "READY"
    assert summary["source_phase"] == 134
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 135
    assert summary["non_signal"] is True


def test_summarize_phase_135_handoff():
    df, _ = build_phase_135_regime_classification_acceptance_handoff_report()
    summary = summarize_phase_135_handoff(df)
    assert summary["total_items"] == 14
    assert summary["all_ready"] is True
    assert summary["handoff_status"] == "READY"
