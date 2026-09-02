from local_incident_response.safety_event_register import build_safety_event_register
from local_incident_response.incident_config import get_default_local_incident_response_profile

def test_build_safety_event_register():
    profile = get_default_local_incident_response_profile()
    df, summary = build_safety_event_register(profile)
    assert not df.empty
    assert "total_events" in summary
