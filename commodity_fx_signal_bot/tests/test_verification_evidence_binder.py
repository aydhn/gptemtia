import pandas as pd
from local_acceptance.verification_evidence_binder import build_final_verification_evidence_binder
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_final_verification_evidence_binder():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame()
    text, _ = build_final_verification_evidence_binder(df, df, df, df, df, p)
    assert "Verification Evidence" in text
