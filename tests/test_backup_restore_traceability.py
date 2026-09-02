import pandas as pd
from pathlib import Path
from local_dr.profile import LocalDRProfile
from local_dr.backup_restore_traceability import *

def test_backup_restore_traceability():
    prof = LocalDRProfile()
    p = Path(".")
    res, info = build_backup_restore_traceability_report(p, prof)
    assert res.empty
    assert link_backup_outputs_to_restore_checklists(p, prof).empty
    assert detect_backup_restore_traceability_gaps(res).empty
    assert summarize_backup_restore_traceability(res) == {"summary": "done"}
