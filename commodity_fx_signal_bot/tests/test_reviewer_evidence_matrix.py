import pandas as pd
from pathlib import Path
from local_acceptance.reviewer_evidence_matrix import build_reviewer_evidence_request_matrix
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_reviewer_evidence_request_matrix():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame([{"question": "test", "warnings": []}])
    res_df, s = build_reviewer_evidence_request_matrix(df, Path("."), p)
    assert "mapped_evidence" in res_df.columns
