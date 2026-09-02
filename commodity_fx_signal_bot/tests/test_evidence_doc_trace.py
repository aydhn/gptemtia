import pandas as pd
from pathlib import Path
from local_acceptance.evidence_doc_trace import build_evidence_doc_trace_matrix
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_evidence_doc_trace_matrix():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame([{"test": "val"}])
    res, s = build_evidence_doc_trace_matrix(df, Path("."), p)
    assert "linked_doc" in res.columns
