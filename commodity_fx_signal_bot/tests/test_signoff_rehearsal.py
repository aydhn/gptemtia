import pandas as pd
from local_acceptance.signoff_rehearsal import build_signoff_rehearsal_checklist, build_signoff_rehearsal_binder
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_signoff_rehearsal():
    p = get_default_local_acceptance_profile()
    df, s = build_signoff_rehearsal_checklist(p)
    assert not df.empty
    text, ts = build_signoff_rehearsal_binder(df, pd.DataFrame(), pd.DataFrame(), p)
    assert "Sign-off Rehearsal Binder" in text
