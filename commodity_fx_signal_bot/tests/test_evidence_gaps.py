import pytest
import pandas as pd
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.evidence_gaps import (
    detect_evidence_gaps,
    evidence_gaps_to_dataframe,
    summarize_evidence_gaps
)

def test_evidence_gaps():
    profile = get_default_evidence_governance_profile()

    status_df = pd.DataFrame([
        {"control_id": "c1", "status": "control_missing_evidence"},
        {"control_id": "c2", "status": "control_stale_evidence"},
        {"control_id": "c3", "status": "control_evidenced"}
    ])

    trace_df = pd.DataFrame()

    gaps = detect_evidence_gaps(status_df, trace_df, profile)
    assert len(gaps) == 2

    df = evidence_gaps_to_dataframe(gaps)
    assert not df.empty

    sum = summarize_evidence_gaps(df)
    assert sum["total_gaps"] == 2
