import pytest
import pandas as pd
from evidence_governance.traceability_matrix import (
    build_evidence_traceability_matrix,
    summarize_traceability_matrix
)

def test_traceability_matrix():
    pol_df = pd.DataFrame([{"policy_id": "p1", "policy_name": "pn1", "policy_domain": "c_dom"}])
    ctrl_df = pd.DataFrame([{"control_id": "c1", "control_name": "cn1", "control_domain": "c_dom"}])
    map_df = pd.DataFrame([{"control_id": "c1", "artifact_id": "a1", "status": "control_evidenced", "mapping_strength": "direct"}])
    art_df = pd.DataFrame([{"artifact_id": "a1", "relative_path": "path", "artifact_label": "lbl", "freshness_label": "fresh"}])

    trace_df = build_evidence_traceability_matrix(pol_df, ctrl_df, map_df, art_df)

    assert not trace_df.empty
    assert "policy_id" in trace_df.columns
    assert "artifact_id" in trace_df.columns

    sum = summarize_traceability_matrix(trace_df)
    assert sum["total_trace_links"] == 1
