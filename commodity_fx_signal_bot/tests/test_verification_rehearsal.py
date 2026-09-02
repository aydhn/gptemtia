from pathlib import Path
from local_acceptance.verification_rehearsal import build_final_verification_rehearsal_plan
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_final_verification_rehearsal_plan():
    p = get_default_local_acceptance_profile()
    df, s = build_final_verification_rehearsal_plan(Path("."), p)
    assert not df.empty
