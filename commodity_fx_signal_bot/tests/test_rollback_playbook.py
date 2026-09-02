from local_incident_response.rollback_playbook import build_rollback_decision_playbook
from local_incident_response.incident_config import get_default_local_incident_response_profile

def test_build_rollback_decision_playbook():
    profile = get_default_local_incident_response_profile()
    text, summary = build_rollback_decision_playbook(profile)
    assert len(text) > 0
