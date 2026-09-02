
from local_closure.maintenance_calendar import build_closure_maintenance_calendar_rehearsal
from local_closure.closure_config import get_default_local_closure_profile

def test_maint():
    p = get_default_local_closure_profile()
    df, summary = build_closure_maintenance_calendar_rehearsal(p)
    assert not df.empty
