import pandas as pd
from pathlib import Path
from local_dr.profile import LocalDRProfile
from local_dr.incident_rehearsal_binder import *

def test_incident_rehearsal_binder(tmp_path):
    prof = LocalDRProfile()
    df = pd.DataFrame()
    t, info = build_incident_rehearsal_binder(df, df, df, prof)
    assert t == "Binder Content"
    assert len(build_incident_rehearsal_sections(df, df, df)) == 2
    p = tmp_path / "binder.md"
    save_incident_rehearsal_binder(t, p)
    assert p.read_text() == "Binder Content"
    assert summarize_incident_rehearsal_binder(t) == {"summary": "binder done"}
