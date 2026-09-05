import pandas as pd
from advanced_regime_matrix.regime_matrix_report_builder import (
    build_regime_matrix_profile_markdown_report,
    build_regime_feature_matrix_contracts_markdown_report,
    build_regime_state_dataset_contracts_markdown_report,
    build_regime_matrix_integrity_markdown_report,
    build_regime_matrix_validation_markdown_report,
    build_regime_matrix_safety_markdown_report,
    build_phase_128_handoff_markdown_report,
)
from reports.report_builder import (
    build_regime_matrix_text_report,
    build_regime_feature_matrix_contract_text_report,
    build_regime_state_dataset_contract_text_report,
    build_regime_matrix_schema_text_report,
    build_regime_matrix_integrity_text_report,
    build_regime_matrix_validation_text_report,
    build_regime_matrix_safety_text_report,
    build_phase_128_handoff_text_report,
)


def test_markdown_and_text_report_generation():
    summary = {
        "active_profile": "balanced_local_regime_matrix",
        "current_phase": 127,
        "next_phase": 128,
        "target_final_phase": 160,
        "total_contracts": 7,
        "ready_contracts": 7,
        "all_prefixed_correctly": True,
        "integrity_status": "INTEGRITY_VALID",
        "validation_status": "VALIDATION_PASS",
        "safety_status": "SECURE",
        "handoff_status": "READY",
        "total_rules": 8,
        "passed_rules": 8,
        "no_go_count": 15,
        "safe_go_count": 7,
        "total_handoff_items": 12,
        "ready_items": 12,
    }
    dummy_df = pd.DataFrame({"col_a": ["val_a"], "col_b": ["val_b"]})

    md_prof = build_regime_matrix_profile_markdown_report(summary, dummy_df)
    assert "Phase 127" in md_prof
    assert "balanced_local_regime_matrix" in md_prof

    txt_prof = build_regime_matrix_text_report(summary, dummy_df)
    assert "UYARI: Bu rapor Phase 127" in txt_prof
    assert "Target Final Phase: 160" in txt_prof

    txt_ho = build_phase_128_handoff_text_report(summary, dummy_df)
    assert "Phase 128" in txt_ho
