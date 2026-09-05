import pandas as pd
from advanced_feature_factor_acceptance.feature_factor_acceptance_report_builder import (
    build_feature_factor_acceptance_profile_markdown_report,
    build_feature_engine_inventory_markdown_report,
    build_feature_engine_dependency_markdown_report,
    build_acceptance_gate_markdown_report,
    build_acceptance_score_markdown_report,
    build_manual_review_markdown_report,
    build_compliance_markdown_report,
    build_contract_markdown_report,
    build_acceptance_manifest_markdown_report,
    build_health_markdown_report,
    build_validation_markdown_report,
    build_phase_126_handoff_markdown_report,
    build_feature_factor_acceptance_disclaimer,
)

def test_acceptance_report_builder():
    disc = build_feature_factor_acceptance_disclaimer()
    assert "YASAL UYARI VE NON-SIGNAL GÜVENCESİ" in disc
    assert "Canlı emir" in disc

    dummy_df = pd.DataFrame([{"col1": "val1"}])
    dummy_s = {"total": 1, "non_signal": True}

    rep1 = build_feature_factor_acceptance_profile_markdown_report(dummy_s, dummy_df)
    assert "# Phase 125 Feature/Factor Acceptance Profiles Report" in rep1
    assert "YASAL UYARI" in rep1

    rep2 = build_feature_engine_inventory_markdown_report(dummy_s, dummy_df)
    assert "# Phase 116-125 Feature Engine Block Inventory Report" in rep2

    rep3 = build_feature_engine_dependency_markdown_report(dummy_s, dummy_df)
    assert "# Phase 116-125 Feature Engine Block Dependencies Report" in rep3

    rep4 = build_acceptance_gate_markdown_report(dummy_s, dummy_df)
    assert "# Phase 125 Feature Engine Block Acceptance Gate Registry" in rep4

    rep5 = build_acceptance_score_markdown_report(dummy_s, dummy_df)
    assert "# Phase 125 Feature Engine Block Acceptance Score Report" in rep5

    rep6 = build_manual_review_markdown_report(dummy_s, dummy_df)
    assert "# Phase 125 Feature Engine Block Manual Review Queue" in rep6

    rep7 = build_compliance_markdown_report(dummy_s, dummy_df)
    assert "# Phase 125 Feature Engine Block Compliance Audit" in rep7

    rep8 = build_contract_markdown_report(dummy_s, dummy_df)
    assert "# Phase 125 Feature Engine Block Contract Audit" in rep8

    rep9 = build_acceptance_manifest_markdown_report(dummy_s, dummy_df)
    assert "# Phase 116-125 Acceptance Manifest Report" in rep9

    rep10 = build_health_markdown_report(dummy_s, dummy_df)
    assert "# Phase 125 Feature Factor Acceptance Health Report" in rep10

    rep11 = build_validation_markdown_report(dummy_s, dummy_df)
    assert "# Phase 125 Feature Factor Acceptance Validation Report" in rep11

    rep12 = build_phase_126_handoff_markdown_report(dummy_s, dummy_df)
    assert "# Phase 126 Regime Classification Handoff Report" in rep12
