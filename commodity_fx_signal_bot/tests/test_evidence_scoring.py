import pytest
import pandas as pd
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.evidence_scoring import (
    calculate_evidence_completeness_score,
    calculate_evidence_freshness_score,
    build_evidence_completeness_report,
    build_evidence_freshness_report
)

def test_evidence_scoring():
    profile = get_default_evidence_governance_profile()

    status_df = pd.DataFrame([
        {"status": "control_evidenced"},
        {"status": "control_partially_evidenced"},
        {"status": "control_missing_evidence"}
    ])

    comp_score = calculate_evidence_completeness_score(status_df)
    assert comp_score == 0.5 # (1.0 + 0.5 + 0) / 3

    art_df = pd.DataFrame([
        {"freshness_label": "evidence_fresh"},
        {"freshness_label": "evidence_warning_stale"},
        {"freshness_label": "evidence_stale"}
    ])

    fresh_score = calculate_evidence_freshness_score(art_df, profile)
    assert fresh_score == 0.5 # (1.0 + 0.5 + 0) / 3

    df1, _ = build_evidence_completeness_report(status_df)
    df2, _ = build_evidence_freshness_report(art_df, profile)
    assert not df1.empty
    assert not df2.empty
