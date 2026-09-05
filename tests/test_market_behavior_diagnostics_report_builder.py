import pandas as pd
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_report_builder import (
    build_market_behavior_diagnostics_disclaimer,
    build_market_behavior_diagnostics_profile_markdown_report,
    build_candidate_state_quality_markdown_report,
    build_regime_family_quality_markdown_report,
    build_behavior_diagnostics_markdown_report,
    build_behavior_quality_score_markdown_report,
    build_phase_130_handoff_markdown_report,
)


def test_market_behavior_diagnostics_report_builder():
    disclaimer = build_market_behavior_diagnostics_disclaimer()
    assert "Phase 129" in disclaimer
    assert "AL/SAT" in disclaimer

    sample_df = pd.DataFrame([{"name": "test_item", "score": 0.95}])
    md_prof = build_market_behavior_diagnostics_profile_markdown_report({"total_profiles": 1}, sample_df)
    assert "Phase 129" in md_prof
    assert "test_item" in md_prof

    md_csq = build_candidate_state_quality_markdown_report({"total_candidate_states": 1}, sample_df)
    assert "Phase 129" in md_csq

    md_rfq = build_regime_family_quality_markdown_report({"total_families": 1}, sample_df)
    assert "Phase 129" in md_rfq

    md_bdiag = build_behavior_diagnostics_markdown_report({"total_contexts": 1}, sample_df)
    assert "Phase 129" in md_bdiag

    md_score = build_behavior_quality_score_markdown_report({"overall_quality_score": 0.95}, sample_df)
    assert "Phase 129" in md_score

    md_handoff = build_phase_130_handoff_markdown_report({"handoff_status": "READY"}, sample_df)
    assert "Phase 130" in md_handoff
