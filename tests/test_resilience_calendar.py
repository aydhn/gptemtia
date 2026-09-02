import pandas as pd
from local_dr.profile import LocalDRProfile
from local_dr.resilience_calendar import *

def test_resilience_calendar():
    prof = LocalDRProfile()
    df = pd.DataFrame()
    res, info = build_resilience_exercise_calendar(df, df, prof)
    assert res.empty
    assert build_restore_drill_review_schedule(df, prof).empty
    assert build_tabletop_review_schedule(df, prof).empty
    assert summarize_resilience_calendar(res) == {"summary": "done"}
