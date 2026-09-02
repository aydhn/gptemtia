import pandas as pd
from pathlib import Path
from local_dr.profile import LocalDRProfile
from local_dr.archive_restore_traceability import *

def test_archive_restore_traceability():
    prof = LocalDRProfile()
    p = Path(".")
    res, info = build_archive_restore_traceability_report(p, prof)
    assert res.empty
    assert link_archive_items_to_restore_prerequisites(p, prof).empty
    assert detect_archive_restore_traceability_gaps(res).empty
    assert summarize_archive_restore_traceability(res) == {"summary": "done"}
