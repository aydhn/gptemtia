import pandas as pd
from pathlib import Path
from local_dr.profile import LocalDRProfile
from local_dr.docs_restore_simulation import *

def test_docs_restore_simulation():
    prof = LocalDRProfile()
    p = Path(".")
    res, info = build_docs_restore_simulation_report(p, prof)
    assert res.empty
    assert simulate_required_docs_restore(p, prof).empty
    assert detect_docs_restore_gaps(res).empty
    assert summarize_docs_restore_simulation(res) == {"summary": "done"}
