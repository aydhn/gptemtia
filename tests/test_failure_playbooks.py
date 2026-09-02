import pandas as pd
from local_dr.profile import LocalDRProfile
from local_dr.failure_playbooks import *

def test_failure_playbooks():
    prof = LocalDRProfile()
    df = pd.DataFrame([{"mode": "test"}])
    res, info = build_failure_mode_playbook_index(df, prof)
    assert not res.empty
    assert build_failure_playbook_for_mode(df.iloc[0], prof) == {"mode": "test"}
    assert build_failure_playbook_markdown(df.iloc[0], prof) == "# Playbook: test"
    assert summarize_failure_playbooks(res) == {"summary": "done"}
