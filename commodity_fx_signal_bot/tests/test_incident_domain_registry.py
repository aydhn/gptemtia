from local_incident_response.incident_domain_registry import build_incident_domain_registry
from local_incident_response.incident_config import get_default_local_incident_response_profile

def test_build_incident_domain_registry():
    profile = get_default_local_incident_response_profile()
    df, summary = build_incident_domain_registry(profile)
    assert not df.empty
    assert "total_domains" in summary
