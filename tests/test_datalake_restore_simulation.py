import pandas as pd
from pathlib import Path
from local_dr.profile import LocalDRProfile
from local_dr.datalake_restore_simulation import *

def test_datalake_restore_simulation():
    prof = LocalDRProfile()
    p = Path(".")
    res, info = build_datalake_restore_simulation_report(p, prof)
    assert res.empty
    assert simulate_datalake_domain_restore_requirements(p, prof).empty
    assert detect_datalake_restore_gaps(res).empty
    assert summarize_datalake_restore_simulation(res) == {"summary": "done"}
