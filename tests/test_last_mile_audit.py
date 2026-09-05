from pathlib import Path
from local_project_completion.last_mile_audit import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_last_mile_audit():
    prof = get_default_local_project_completion_profile()
    text, sum1 = build_last_mile_audit_binder(Path("."), prof)
    df1, sum2 = build_last_mile_audit_checklist_registry(prof)
    df2, sum3 = build_last_mile_audit_evidence_index(Path("."), prof)
    assert "Not an official audit" in sum1["note"]
    assert not df1.empty
    assert not df2.empty
