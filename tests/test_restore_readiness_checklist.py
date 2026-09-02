import pandas as pd
from pathlib import Path
from local_dr.profile import LocalDRProfile
from local_dr.restore_readiness_checklist import *

def test_restore_readiness_checklist():
    prof = LocalDRProfile()
    p = Path(".")
    res, info = build_restore_readiness_dry_run_checklist(p, prof)
    assert res.empty
    assert check_restore_prerequisite_presence(p, prof).empty
    assert check_restore_documentation_presence(p, prof).empty
    assert summarize_restore_readiness_checklist(res) == {"summary": "done"}
